"""Exporta as saídas Altair salvas no artigo para um HTML com gráficos offline."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit, unquote
import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
import vl_convert as vlc

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / 'artigo_interativo.html'
notebook = nbformat.read(RAIZ / 'notebooks/00_artigo.ipynb', as_version=4)
alturas = [415, 350, 615, 675, 500, 690, 410]
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
if n != 7:
    raise ValueError('Execute e salve as oito células do artigo antes de exportar.')

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
DESTINO.write_text(str(pagina), encoding='utf-8')
print(f'Artigo exportado com {n} gráficos: {DESTINO}')
