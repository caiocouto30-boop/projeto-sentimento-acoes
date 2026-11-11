"""Executa em ordem as células Python e salva saídas reais, sem servidor Jupyter."""
import ast
import base64
from contextlib import redirect_stdout, redirect_stderr
import io
import json
import os
from pathlib import Path
import time

def executar():
    raiz=Path(__file__).resolve().parents[1]
    arquivo=raiz/'notebooks/00_artigo.ipynb'
    nb=json.loads(arquivo.read_text(encoding='utf-8'))
    globals_nb={'__name__':'__main__'}
    cwd=Path.cwd();contagem=0;inicio=time.time()
    try:
        os.chdir(raiz)
        for c in nb['cells']:
            if c['cell_type']!='code':continue
            contagem+=1;source=''.join(c['source']);mod=ast.parse(source)
            ultimo=mod.body.pop() if mod.body and isinstance(mod.body[-1],ast.Expr) else None
            stdout,stderr=io.StringIO(),io.StringIO()
            with redirect_stdout(stdout),redirect_stderr(stderr):
                exec(compile(mod,'<artigo:'+c['id']+'>','exec'),globals_nb)
                value=eval(compile(ast.Expression(ultimo.value),'<artigo:'+c['id']+'>','eval'),globals_nb) if ultimo else None
                mime={'text/plain':repr(value)} if value is not None else None
                if value is not None and hasattr(value,'_repr_html_'):
                    mime['text/html']=value._repr_html_()
                    if hasattr(value,'q'):
                        figura=raiz/'figures/analise_final'/f'{value.q}.png'
                        if figura.exists():mime['image/png']=base64.b64encode(figura.read_bytes()).decode('ascii')
            outputs=[]
            for name,buf in [('stdout',stdout),('stderr',stderr)]:
                if buf.getvalue():outputs.append(dict(output_type='stream',name=name,text=buf.getvalue()))
            if mime:outputs.append(dict(output_type='execute_result',execution_count=contagem,metadata={},data=mime))
            c.update(execution_count=contagem,outputs=outputs)
        nb['metadata']['execucao_final']={'celulas_executadas':contagem,'duracao_segundos':round(time.time()-inicio,2),'metodo':'Python, células em ordem, namespace único, AST; sem nova inferência FinBERT'}
        arquivo.write_text(json.dumps(nb,ensure_ascii=False,indent=1),encoding='utf-8')
    finally:os.chdir(cwd)
    return {'celulas':contagem,'segundos':round(time.time()-inicio,2),'arquivo':str(arquivo),'bytes':arquivo.stat().st_size}

if __name__=='__main__':print(json.dumps(executar(),ensure_ascii=False,indent=2))
