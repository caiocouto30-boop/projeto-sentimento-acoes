"""Análise reproduzível da entrega final. Entradas são snapshots preservados."""
from pathlib import Path
import hashlib
import json
import re
import numpy as np
import pandas as pd
from robustez import construir_cenarios, marcar_textos, resumir_retencao

RAIZ = Path(__file__).resolve().parents[1]
EMPRESAS = ['BAC', 'JNJ', 'KO', 'NFLX', 'NVDA']
CLASSES = ['negativo', 'neutro', 'positivo', 'empate']

def spearman(df, x, y):
    pares = df[[x, y]].dropna()
    if len(pares) < 3 or (pares.nunique() < 2).any():
        return np.nan
    return pares[x].rank(method='average').corr(pares[y].rank(method='average'))

def assunto(manchete):
    """Tema lexical, não resumo do artigo. Usa só o título, sem retornos."""
    regras = [
        ('Resultados e projeções', r'\b(?:earnings|revenues?|sales|guidance|eps|quarters?|profits?|fiscal|subscribers?)\b'),
        ('Avaliação de analistas', r'analyst|price target|upgrade|downgrade|rating|maintains|reiterates|initiates|overweight|underweight'),
        ('Regulação e processos', r'lawsuit|court|judge|fda|legal|regulat|investigat|settlement|recall|talc|opioid|justice'),
        ('Dividendos e capital', r'dividend|buyback|repurchase|offering|capital|debt|bond'),
        ('Negócios e acordos', r'acquir|acquisi|merger|deal|partner|agreement|stake|invest'),
        ('Produtos e serviços', r'launch|product|chip|gpu|gaming|stream|show|series|film|movie|drug|trial|beverage|drink'),
        ('Cotação e negociação', r'shares|stock|trading|market|nasdaq|dow|rally|sell.off|price|resistance|support'),
    ]
    return next((tema for tema, padrao in regras if re.search(padrao, str(manchete), re.I)),
                'Notícia corporativa ou de mercado')

def resumo_classes(df):
    return df.groupby(['stock', 'classe_sentimento']).retorno_pct.agg(
        n='size', media='mean', mediana='median', minimo='min', maximo='max',
        q1=lambda s: s.quantile(.25), q3=lambda s: s.quantile(.75)).reset_index()

def preparar():
    data = RAIZ / 'data/processed'
    noticias = pd.read_csv(data/'noticias_com_sentimento.csv', parse_dates=['news_date'])
    painel = pd.read_csv(data/'base_integrada_pregoes.csv', parse_dates=['trade_date', 'trade_date_anterior'])
    mapa = pd.read_csv(data/'noticias_pregao_retornos.csv', parse_dates=['news_date', 'trade_date', 'trade_date_anterior'])
    principal = painel.loc[painel.tem_noticias & painel.elegivel_analise_principal].copy()
    principal['ano'] = principal.trade_date.dt.year
    # Mantemos a definição original e acrescentamos outra pergunta de medida.
    # |média(s)| mede polarização líquida; média(|s|) mede intensidade sem cancelamento.
    intensidade = mapa.assign(abs_escore=mapa.escore_sentimento.abs()).groupby(
        ['stock','trade_date'], as_index=False).agg(intensidade_media=('abs_escore','mean'))
    principal = principal.merge(intensidade, on=['stock','trade_date'], validate='one_to_one')
    principal['polarizacao_liquida'] = principal.intensidade_sentimento
    diario = noticias.groupby(['stock','news_date'], as_index=False).agg(
        escore_sentimento=('escore_sentimento','mean'), n_noticias=('headline','size'))
    diario['key'] = diario.stock + '|' + diario.news_date.dt.strftime('%Y-%m-%d')
    principal['key'] = principal.stock + '|' + principal.trade_date.dt.strftime('%Y-%m-%d')
    noticias['assunto'] = noticias.headline.map(assunto)
    mapa['assunto'] = mapa.headline.map(assunto)
    marcacao = marcar_textos(noticias)
    cenarios, elegiveis = construir_cenarios(mapa, principal, marcacao)
    # Recalcular média(|s|) com as notícias efetivamente retidas em cada cenário.
    por_hash = marcacao.set_index('headline_hash').marcacao
    elegiveis['marcacao'] = elegiveis.headline_hash.map(por_hash)
    for nome, df in cenarios.items():
        textos = elegiveis
        if 'Sem retrospectivas/ambíguas' in nome:
            textos = textos.loc[textos.marcacao.eq('sem_indicio_explicito')]
        elif 'Sem retrospectivas' in nome:
            textos = textos.loc[textos.marcacao.ne('retrospectiva_explicita')]
        med = textos.assign(abs_escore=textos.escore_sentimento.abs()).groupby(
            ['stock','trade_date'], as_index=False).agg(intensidade_media=('abs_escore','mean'))
        df = df.drop(columns=['intensidade_media'], errors='ignore').merge(
            med, on=['stock','trade_date'], validate='one_to_one')
        df['polarizacao_liquida'] = df.intensidade_sentimento
        cenarios[nome] = df
    return dict(noticias=noticias,painel=painel,mapa=mapa,principal=principal,
                diario=diario,marcacao=marcacao,cenarios=cenarios)

def tabelas(d):
    n,p,a,diario = d['noticias'],d['painel'],d['principal'],d['diario']
    indice = pd.MultiIndex.from_product([EMPRESAS,pd.date_range('2017-01-01','2019-12-01',freq='MS')],names=['stock','mes'])
    mensal = n.assign(mes=n.news_date.dt.to_period('M').dt.to_timestamp()).groupby(['stock','mes']).size().reindex(indice,fill_value=0).rename('n').reset_index()
    composicao = pd.crosstab(n.stock,n.classe_finbert).reindex(index=EMPRESAS,columns=CLASSES,fill_value=0)
    intensidade = pd.DataFrame([{'stock':e,'n':len(g),
        'rho_quantidade_abs':spearman(g,'n_noticias','retorno_absoluto_pct'),
        'rho_polarizacao_abs':spearman(g,'polarizacao_liquida','retorno_absoluto_pct'),
        'rho_intensidade_media_abs':spearman(g,'intensidade_media','retorno_absoluto_pct')}
        for e,g in a.groupby('stock')])
    correlacoes=[]
    for e,g in a.groupby('stock'):
        for periodo,h in [('2017–2019',g)]+[(str(ano),h) for ano,h in g.groupby('ano')]:
            correlacoes.append(dict(stock=e,periodo=periodo,n=len(h),rho=spearman(h,'escore_sentimento','retorno_pct')))
    metricas=[('escore_sentimento','retorno_pct','Escore × retorno'),
              ('polarizacao_liquida','retorno_absoluto_pct','Polarização × |retorno|'),
              ('n_noticias','retorno_absoluto_pct','Quantidade × |retorno|'),
              ('intensidade_media','retorno_absoluto_pct','Intensidade média × |retorno|')]
    sensibilidade=pd.DataFrame([dict(cenario=c,stock=e,metrica=m,n=len(g),rho=spearman(g,x,y))
        for c,df in d['cenarios'].items() for e,g in df.groupby('stock') for x,y,m in metricas])
    extremos=[]
    for minimo in [1,3]:
        for e,g in diario.loc[diario.n_noticias.ge(minimo)].groupby('stock'):
            for extremo,asc in [('mínimo',True),('máximo',False)]:
                row=g.sort_values(['escore_sentimento','news_date'],ascending=[asc,True]).iloc[0].to_dict()
                extremos.append(dict(**row,extremo=extremo,minimo_noticias=minimo))
    return {'q1_mensal':mensal,'q1_anual':n.assign(ano=n.news_date.dt.year).groupby(['stock','ano']).size().rename('n').reset_index(),
        'q2_classes':composicao.reset_index(),'q3_diario':diario,'q3_extremos':pd.DataFrame(extremos),
        'q4_retornos_classes':resumo_classes(a),'q5_associacoes':intensidade,'q6_correlacoes':pd.DataFrame(correlacoes),
        'q7_sensibilidade':sensibilidade,'q7_retencao_empresa_ano':resumir_retencao(d['cenarios']),
        'q7_resumo_cenarios':pd.DataFrame([dict(cenario=c,pregoes=len(df),noticias=int(df.n_noticias.sum()),retencao_pct=100*len(df)/len(a)) for c,df in d['cenarios'].items()])}

def validar(d):
    """Conferências independentes das junções e dos números da análise."""
    n,p,m,a = [d[k] for k in ['noticias','painel','mapa','principal']]
    assert (len(n),len(p),len(m),len(a)) == (6552,3770,6552,2387)
    assert n.source_id.is_unique and m.source_id.is_unique
    assert not n.duplicated(['stock','news_date','headline']).any()
    assert not p.duplicated(['stock','trade_date']).any()
    assert set(n.source_id)==set(m.source_id)
    assert p.loc[~p.tem_noticias,['escore_sentimento','classe_sentimento']].isna().all().all()
    assert (m.news_date<m.trade_date).all() and (m.trade_date_anterior<=m.news_date).all()
    assert np.allclose(n[['p_positivo','p_negativo','p_neutro']].sum(axis=1),1,atol=1e-6)
    assert np.allclose(n.escore_sentimento,n.p_positivo-n.p_negativo,atol=1e-8)
    precos=pd.read_csv(RAIZ/'data/raw/cotacoes_yahoo_margem.csv',parse_dates=['trade_date']).sort_values(['stock','trade_date'])
    precos['retorno_recalculado']=precos.groupby('stock')['Adj Close'].pct_change(fill_method=None)*100
    conf=p.merge(precos[['stock','trade_date','retorno_recalculado']],on=['stock','trade_date'],validate='one_to_one')
    assert np.allclose(conf.retorno_pct,conf.retorno_recalculado,atol=1e-8)
    for e,g in m.groupby('stock'):
        sessoes=precos.loc[precos.stock.eq(e),'trade_date'].to_numpy()
        pos=np.searchsorted(sessoes,g.news_date.to_numpy(),side='right')
        assert (sessoes[pos]==g.trade_date.to_numpy()).all()
    agg=m.groupby(['stock','trade_date']).escore_sentimento.agg(['size','mean']).reset_index()
    conf=a.merge(agg,on=['stock','trade_date'],validate='one_to_one')
    assert (conf['size']==conf.n_noticias).all() and np.allclose(conf['mean'],conf.escore_sentimento,atol=1e-8)
    assert (a.intensidade_media+1e-10>=a.polarizacao_liquida).all()
    assert a.intensidade_media.between(0,1+1e-10).all()
    esperado=[2387,783,2271,697,2243,670]
    assert [len(x) for x in d['cenarios'].values()]==esperado
    # Igualdade entre cache FinBERT e notícias classificadas.
    cache=pd.read_csv(RAIZ/'data/raw/finbert_probabilidades.csv')
    cc=n.merge(cache,on='headline_hash',validate='many_to_one',suffixes=('','_cache'))
    for c in ['p_positivo','p_negativo','p_neutro']:
        assert np.allclose(cc[c],cc[c+'_cache'],atol=1e-8)
    # Limpeza refeita a partir do recorte bruto.
    bruto=pd.read_csv(RAIZ/'data/raw/noticias_recorte_original.csv')
    bruto['headline']=bruto.headline.str.replace(r'\s+',' ',regex=True).str.strip()
    bruto['news_date']=pd.to_datetime(bruto.date.str[:10])
    limpo=bruto.sort_values('Unnamed: 0').drop_duplicates(['stock','news_date','headline'])
    assert len(bruto)==6556 and len(limpo)==len(n)
    assert set(limpo['Unnamed: 0'])==set(n.source_id)
    return {'status':'aprovado','noticias':len(n),'pares_painel':len(p),'pares_principais':len(a),
        'pares_cenarios':esperado,'escopo':'limpeza, cache, integração, retornos, agregação e análise; sem nova inferência FinBERT'}

def registros(df):
    return json.loads(df.to_json(orient='records',date_format='iso',double_precision=10))

def exportar(d,t):
    pasta=RAIZ/'docs/analise_final';pasta.mkdir(parents=True,exist_ok=True)
    for nome,df in t.items(): df.to_csv(pasta/(nome+'.csv'),index=False,date_format='%Y-%m-%d',float_format='%.10g')
    d['marcacao'].to_csv(RAIZ/'docs/retrospectivas/marcacao_textos.csv',index=False)
    medidas=d['principal'][['stock','trade_date','intensidade_media','polarizacao_liquida']]
    medidas.to_csv(RAIZ/'data/processed/medidas_intensidade_final.csv',index=False,date_format='%Y-%m-%d')
    verificacao=validar(d)
    (pasta/'verificacao.json').write_text(json.dumps(verificacao,ensure_ascii=False,indent=2),encoding='utf-8')
    return verificacao

if __name__=='__main__':
    dados=preparar();t=tabelas(dados);print(json.dumps(exportar(dados,t),ensure_ascii=False,indent=2))
