"""Compara os resultados do notebook com a verificação independente da análise."""
from pathlib import Path
import json
import os
os.environ.setdefault('MKL_THREADING_LAYER','SEQUENTIAL')
import numpy as np
import pandas as pd
import nbformat
from analise_final import preparar,tabelas
from verificar_final import verificar

RAIZ=Path(__file__).resolve().parents[1]

def verificar_notebook():
    verificacao=verificar()
    esperado=tabelas(preparar());pasta=RAIZ/'docs/analise_final'
    for nome,chaves in [('q5_associacoes',['stock','n']),('q6_correlacoes',['stock','periodo'])]:
        obtido=pd.read_csv(pasta/(nome+'.csv'))
        ref=esperado[nome]
        comp=obtido.merge(ref,on=chaves,validate='one_to_one',suffixes=('_nb','_ref'))
        assert len(comp)==len(ref)
        for campo in ref.select_dtypes('number').columns:
            if campo in chaves:continue
            assert np.allclose(comp[campo+'_nb'],comp[campo+'_ref'],atol=1e-8),campo
    obtido=pd.read_csv(pasta/'q7_sensibilidade_completa.csv')
    ref=esperado['q7_sensibilidade']
    comp=obtido.merge(ref,on=['stock','cenario','metrica'],validate='one_to_one',suffixes=('_nb','_ref'))
    assert len(comp)==120 and (comp.n_nb==comp.n_ref).all()
    assert np.allclose(comp.rho_nb,comp.rho_ref,atol=1e-8)
    medidas=pd.read_csv(RAIZ/'data/processed/medidas_intensidade_final.csv')
    assert len(medidas)==2387 and (medidas.intensidade_media+1e-10>=medidas.intensidade_liquida).all()
    nb=nbformat.read(RAIZ/'notebooks/00_artigo.ipynb',as_version=4);nbformat.validate(nb)
    codigos=[c for c in nb.cells if c.cell_type=='code']
    assert len(codigos)==15 and [c.execution_count for c in codigos]==list(range(1,16))
    assert all('Vista(' not in c.source and 'Plotly' not in c.source for c in codigos)
    specs=[]
    for c in codigos:
        for out in c.outputs:
            assert out.output_type!='error'
            if out.get('data',{}).get('application/vnd.vegalite.v6+json'):
                specs.append(out.data['application/vnd.vegalite.v6+json'])
    assert len(specs)==7,len(specs)
    q3=json.dumps(specs[2],ensure_ascii=False);q5=json.dumps(specs[4],ensure_ascii=False)
    assert all(f'manchete_{i}' in q3 for i in [1,2,3])
    assert 'medida_intensidade' in q5 and 'intensidade_media' in q5 and 'intensidade_liquida' in q5
    assert specs[6]['columns']==2
    resultado={'status':'aprovado','celulas_totais':len(nb.cells),'celulas_codigo':len(codigos),
        'graficos_altair_com_especificacao_valida':len(specs),'coeficientes_robustez_conferidos':len(comp),
        'calculos_consistentes_com_verificacao_independente':True,'execucao':dict(nb.metadata.execucao_final),
        'renderizacao_visual':'pendente; os gráficos e seletores devem ser conferidos no Jupyter ou HTML',
        'verificacao_independente':verificacao}
    (pasta/'verificacao_notebook.json').write_text(json.dumps(resultado,ensure_ascii=False,indent=2),encoding='utf-8')
    return resultado

if __name__=='__main__':print(json.dumps(verificar_notebook(),ensure_ascii=False,indent=2))
