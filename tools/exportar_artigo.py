"""Exporta as sete figuras salvas no notebook para leitura e hover offline."""
import json
from pathlib import Path

from bs4 import BeautifulSoup
import nbformat
from nbconvert import HTMLExporter

RAIZ = Path(__file__).resolve().parents[1]


def exportar():
    caminho = RAIZ / 'notebooks/00_artigo.ipynb'
    notebook = nbformat.read(caminho, as_version=4)
    nbformat.validate(notebook)
    if any(c.cell_type == 'code' and c.execution_count is None for c in notebook.cells):
        raise RuntimeError('Execute e salve o notebook antes de exportar.')

    graficos = []
    for celula in notebook.cells:
        for saida in celula.get('outputs', []):
            dados = saida.get('data', {})
            spec = dados.get('application/vnd.vegalite.v6+json')
            if spec is None:
                continue
            graficos.append(spec)
            dados['text/html'] = f'<div id="grafico-q{len(graficos)}"></div>'
    if len(graficos) != 7:
        raise ValueError('O artigo executado deve conter as sete figuras.')

    html, _ = HTMLExporter(template_name='classic').from_notebook_node(notebook)
    pagina = BeautifulSoup(html, 'html.parser')
    for link in pagina.find_all('a', href=True):
        href = link['href']
        if href.startswith('../docs/'):
            link['href'] = href[3:]
        elif href == '01_preparacao_dados.ipynb':
            link['href'] = 'notebooks/' + href

    estilo = pagina.new_tag('style')
    estilo.string = '#vg-tooltip-element td.value { white-space: pre-wrap; overflow-wrap: anywhere; max-width: min(600px, 70vw); text-align: left; }'
    pagina.head.append(estilo)
    runtime = pagina.new_tag('script')
    runtime.string = '(function(){' + (RAIZ / 'vendor/vega-bundle.js').read_text(encoding='utf-8') + '})();'
    pagina.body.append(runtime)
    for numero, spec in enumerate(graficos, start=1):
        script = pagina.new_tag('script')
        payload = json.dumps(spec, ensure_ascii=False, separators=(',', ':')).replace('<', r'\u003c')
        script.string = f'vegaEmbed("#grafico-q{numero}", {payload}, {{renderer:"svg", actions:false}});'
        pagina.body.append(script)

    destino = RAIZ / 'artigo_interativo.html'
    destino.write_text(str(pagina), encoding='utf-8', newline='\n')
    return destino


if __name__ == '__main__':
    print(exportar())

