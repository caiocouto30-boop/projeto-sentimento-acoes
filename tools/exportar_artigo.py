"""Exporta as saídas Altair salvas no artigo para um HTML com gráficos offline."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit, unquote
import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
import vl_convert as vlc
import base64
import hashlib
import json
from datetime import datetime, timezone

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / 'artigo_interativo.html'
notebook = nbformat.read(RAIZ / 'notebooks/00_artigo.ipynb', as_version=4)
alturas = [415, 350, 615, 675, 500, 690, 600]
figuras = RAIZ / 'figures/analise_visual'
figuras.mkdir(parents=True, exist_ok=True)
n = 0
for celula in notebook.cells:
    for saida in celula.get('outputs', []):
        dados = saida.get('data', {})
        especificacao = dados.get('application/vnd.vegalite.v6+json')
        if especificacao is None:
            continue
        png = vlc.vegalite_to_png(especificacao, scale=1.5)
        (figuras / f'q{n+1}.png').write_bytes(png)
        dados['image/png'] = base64.b64encode(png).decode('ascii')
        n += 1
if n != 7:
    raise ValueError('Execute e salve as nove células do artigo antes de exportar.')
(RAIZ / 'notebooks/00_artigo.ipynb').write_text(
    nbformat.writes(notebook), encoding='utf-8', newline='\n')

n = 0
for celula in notebook.cells:
    for saida in celula.get('outputs', []):
        dados = saida.get('data', {})
        especificacao = dados.get('application/vnd.vegalite.v6+json')
        if especificacao is None:
            continue
        html = vlc.vegalite_to_html(especificacao, bundle=True, renderer='svg')
        dados['text/html'] = (
            f'<iframe title="Gráfico interativo Q{n+1}" '
            f'style="border:0;width:100%;height:{alturas[n]}px" '
            f'srcdoc="{escape(html, quote=True)}"></iframe>'
        )
        n += 1
exportador = HTMLExporter()
exportador.exclude_input_prompt = True
exportador.exclude_output_prompt = True
conteudo, _ = exportador.from_notebook_node(notebook)
pagina = BeautifulSoup(conteudo, 'html.parser')
pagina.title.string = 'Sentimento das notícias — artigo interativo'
for link in pagina.find_all('a', href=True):
    href = link['href']
    if urlsplit(href).scheme or href.startswith('#'):
        continue
    arquivo = (RAIZ / 'notebooks' / unquote(href)).resolve()
    if arquivo.is_file():
        link['href'] = arquivo.relative_to(DESTINO.parent).as_posix()
DESTINO.write_text(str(pagina), encoding='utf-8', newline='\n')
manifesto = {
    'gerado_em_utc': datetime.now(timezone.utc).isoformat(),
    'notebook': 'notebooks/00_artigo.ipynb',
    'sha256_notebook': hashlib.sha256((RAIZ / 'notebooks/00_artigo.ipynb').read_bytes()).hexdigest(),
    'sha256_entradas': {nome: hashlib.sha256((RAIZ / 'data/processed' / nome).read_bytes()).hexdigest()
        for nome in ['noticias_com_sentimento.csv', 'base_integrada_pregoes.csv', 'noticias_pregao_retornos.csv']},
    'sha256_tabelas': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted((RAIZ / 'docs/analise_visual').glob('*.csv'))},
    'figuras': [f'figures/analise_visual/q{i}.png' for i in range(1, 8)]}
(RAIZ / 'docs/analise_visual/manifesto.json').write_text(
    json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(f'Artigo exportado com {n} gráficos e imagens: {DESTINO}')
