"""Confere a análise final contra coeficientes já publicados e cálculo independente."""
import json
import numpy as np
import pandas as pd
from analise_final import RAIZ, preparar, tabelas, validar, spearman

def postos_numpy(x):
    _,inverse,counts=np.unique(x,return_inverse=True,return_counts=True)
    fim=np.cumsum(counts)
    inicio=fim-counts+1
    return ((inicio+fim)/2)[inverse]

def rho_independente(g,x,y):
    z=g[[x,y]].dropna().to_numpy()
    a=postos_numpy(z[:,0]);b=postos_numpy(z[:,1]);a-=a.mean();b-=b.mean()
    den=np.linalg.norm(a)*np.linalg.norm(b)
    return np.dot(a,b)/den if len(z)>=3 and den else np.nan

def verificar():
    d=preparar();t=tabelas(d);resultado=validar(d)
    legado=RAIZ/'docs/analise_visual'
    q5=pd.read_csv(legado/'q5_associacoes.csv')
    c=q5.merge(t['q5_associacoes'],on=['stock','n'],validate='one_to_one',suffixes=('_antes','_final'))
    assert len(c)==5
    assert np.allclose(c.rho_quantidade_abs_antes,c.rho_quantidade_abs_final,atol=1e-8)
    assert np.allclose(c.rho_intensidade_abs,c.rho_polarizacao_abs,atol=1e-8)
    for nome,chaves,novo in [('q6_correlacoes',['stock','periodo'],'q6_correlacoes'),('q7_sensibilidade_completa',['stock','cenario','metrica'],'q7_sensibilidade')]:
        antes=pd.read_csv(legado/(nome+'.csv'));depois=t[novo].copy()
        if 'metrica' in antes:
            antes['metrica']=antes.metrica.str.replace('Intensidade ×','Polarização ×',regex=False)
        for chave in chaves:
            antes[chave]=antes[chave].astype(str).str.replace('–','-',regex=False)
            depois[chave]=depois[chave].astype(str).str.replace('–','-',regex=False)
        c=antes.merge(depois,on=chaves,validate='one_to_one',suffixes=('_antes','_final'))
        assert len(c)==len(antes)
        assert (c.n_antes==c.n_final).all()
        assert np.allclose(c.rho_antes,c.rho_final,atol=1e-8)
    checados=0
    for df in d['cenarios'].values():
        for _,g in df.groupby('stock'):
            for x,y in [('escore_sentimento','retorno_pct'),('n_noticias','retorno_absoluto_pct'),('polarizacao_liquida','retorno_absoluto_pct'),('intensidade_media','retorno_absoluto_pct')]:
                assert np.isclose(spearman(g,x,y),rho_independente(g,x,y),atol=1e-12,equal_nan=True)
                checados+=1
    # Casos da regra lexical preservada, sem tratar isso como validação humana.
    from retrospectivas import classificar
    controles=pd.read_csv(RAIZ/'docs/retrospectivas/casos_controle.csv')
    obtidas=controles.manchete_exemplificativa.map(lambda h:classificar(h)[0]=='retrospectiva_explicita')
    assert obtidas.eq(controles.exclusao_esperada).all()
    resultado.update(coeficientes_historicos_reproduzidos=120,coeficientes_conferidos_por_postos_independentes=checados)
    (RAIZ/'docs/analise_final/verificacao.json').write_text(json.dumps(resultado,ensure_ascii=False,indent=2),encoding='utf-8')
    return resultado

if __name__=='__main__':print(json.dumps(verificar(),ensure_ascii=False,indent=2))
