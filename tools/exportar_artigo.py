"""Exporta o notebook salvo para HTML; não gera nem substitui suas células."""
from pathlib import Path
import os
os.environ.setdefault('MKL_THREADING_LAYER','SEQUENTIAL')
import nbformat
from nbconvert import HTMLExporter

def exportar():
    raiz=Path(__file__).resolve().parents[1]
    nb=nbformat.read(raiz/'notebooks/00_artigo.ipynb',as_version=4)
    nbformat.validate(nb)
    if any(c.cell_type=='code' and c.execution_count is None for c in nb.cells):
        raise RuntimeError('Execute e salve o notebook antes de exportar.')
    html,_=HTMLExporter(template_name='classic').from_notebook_node(nb)
    destino=raiz/'artigo_interativo.html'
    destino.write_text(html,encoding='utf-8')
    return destino

if __name__=='__main__':print(exportar())
