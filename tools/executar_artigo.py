"""Executa as células do artigo, preservando o notebook como fonte principal."""
from pathlib import Path
import argparse
import json
import os
import time
os.environ.setdefault('MKL_THREADING_LAYER','SEQUENTIAL')
import nbformat

RAIZ=Path(__file__).resolve().parents[1]

def executar(pasta='raiz',modo='kernel'):
    caminho=RAIZ/'notebooks/00_artigo.ipynb'
    nb=nbformat.read(caminho,as_version=4)
    cwd=RAIZ/'notebooks' if pasta=='notebooks' else RAIZ
    inicio=time.time()
    if modo=='kernel':
        from nbclient import NotebookClient
        NotebookClient(nb,kernel_name='python3',timeout=180,startup_timeout=30,
            resources={'metadata':{'path':str(cwd)}}).execute()
        metodo='nbclient, kernel Jupyter python3'
    else:
        from IPython.core.interactiveshell import InteractiveShell
        from IPython.utils.capture import capture_output
        from traitlets.config import Config
        cfg=Config({'HistoryManager':{'enabled':False,'hist_file':':memory:'}})
        shell=InteractiveShell.instance(config=cfg)
        shell.history_manager.enabled=False
        anterior=Path.cwd();contagem=0
        try:
            os.chdir(cwd)
            for celula in nb.cells:
                if celula.cell_type!='code':continue
                contagem+=1
                with capture_output(stdout=True,stderr=True,display=True) as cap:
                    resultado=shell.run_cell(celula.source,store_history=False,silent=False)
                if resultado.error_before_exec or resultado.error_in_exec:
                    raise RuntimeError(f'Erro na célula {celula.id}: '+str(resultado.error_before_exec or resultado.error_in_exec))
                outputs=[]
                for nome,valor in [('stdout',cap.stdout),('stderr',cap.stderr)]:
                    if valor:outputs.append(nbformat.v4.new_output('stream',name=nome,text=valor))
                for out in cap.outputs:
                    outputs.append(nbformat.v4.new_output('display_data',data=out.data,metadata=out.metadata))
                celula.execution_count=contagem;celula.outputs=outputs
        finally:
            os.chdir(anterior)
        metodo='IPython InteractiveShell no mesmo processo; sem processo de kernel separado'
    nb.metadata['execucao_final']={'metodo':metodo,'diretorio_execucao':pasta,
        'celulas_executadas':sum(c.cell_type=='code' for c in nb.cells),
        'duracao_segundos':round(time.time()-inicio,2)}
    nbformat.validate(nb)
    nbformat.write(nb,caminho)
    return dict(nb.metadata['execucao_final'],arquivo=str(caminho))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pasta',choices=['raiz','notebooks'],default='raiz')
    parser.add_argument('--modo',choices=['kernel','ipython'],default='kernel')
    args=parser.parse_args()
    print(json.dumps(executar(args.pasta,args.modo),ensure_ascii=False,indent=2))
