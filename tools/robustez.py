"""Transformações da pergunta 7; nenhuma função altera as bases de entrada."""
import numpy as np
import pandas as pd
from retrospectivas import classificar, VERSAO_REGRA

CENARIOS = ['Principal', 'Mínimo 3', 'Sem retrospectivas', 'Sem retrospectivas + mínimo 3']
EXTRAS = ['Sem retrospectivas/ambíguas', 'Sem retrospectivas/ambíguas + mínimo 3']

def marcar_textos(noticias):
    textos = noticias[['headline_hash', 'headline']].drop_duplicates().copy()
    assert textos['headline_hash'].is_unique
    textos[['marcacao', 'regra', 'trecho']] = pd.DataFrame(
        textos['headline'].map(classificar).tolist(), index=textos.index)
    textos['versao_regra'] = VERSAO_REGRA
    textos['origem_marcacao'] = 'regra automática; critérios revistos por assistente IA; sem validação humana independente'
    return textos.sort_values('headline_hash').reset_index(drop=True)

def agregar_por_pregao(manchetes, retornos):
    agregado = manchetes.groupby(['stock', 'trade_date'], as_index=False).agg(
        n_noticias=('source_id', 'size'), p_positivo=('p_positivo', 'mean'),
        p_negativo=('p_negativo', 'mean'), p_neutro=('p_neutro', 'mean'))
    probabilidades = agregado[['p_positivo', 'p_negativo', 'p_neutro']].to_numpy()
    empates = np.isclose(probabilidades, probabilidades.max(axis=1, keepdims=True),
                        atol=1e-8, rtol=0).sum(axis=1) > 1
    agregado['classe_sentimento'] = np.where(empates, 'empate',
        np.array(['positivo', 'negativo', 'neutro'])[probabilidades.argmax(axis=1)])
    agregado['escore_sentimento'] = agregado['p_positivo'] - agregado['p_negativo']
    agregado['intensidade_sentimento'] = agregado['escore_sentimento'].abs()
    campos = ['stock', 'trade_date', 'retorno_pct', 'retorno_absoluto_pct', 'ano']
    return agregado.merge(retornos[campos], on=['stock', 'trade_date'], validate='one_to_one')

def construir_cenarios(mapeadas, principal, marcacao):
    # Primeiro limitar às mesmas janelas elegíveis, depois excluir textos.
    elegiveis = mapeadas.merge(principal[['stock', 'trade_date']],
        on=['stock', 'trade_date'], validate='many_to_one')
    elegiveis = elegiveis.merge(marcacao[['headline_hash', 'marcacao']],
        on='headline_hash', validate='many_to_one')
    assert len(elegiveis) == int(principal['n_noticias'].sum())
    mantidas = elegiveis.loc[elegiveis['marcacao'].ne('retrospectiva_explicita')]
    conservadoras = elegiveis.loc[elegiveis['marcacao'].eq('sem_indicio_explicito')]
    sem_retro = agregar_por_pregao(mantidas, principal)
    sem_ambiguas = agregar_por_pregao(conservadoras, principal)
    cenarios = {
        'Principal': principal.copy(),
        'Mínimo 3': principal.loc[principal['n_noticias'].ge(3)].copy(),
        'Sem retrospectivas': sem_retro,
        'Sem retrospectivas + mínimo 3': (
            sem_retro.loc[sem_retro['n_noticias'].ge(3)].copy()
        ),
    }
    cenarios.update({
        'Sem retrospectivas/ambíguas': sem_ambiguas,
        'Sem retrospectivas/ambíguas + mínimo 3': (
            sem_ambiguas.loc[sem_ambiguas['n_noticias'].ge(3)].copy()
        ),
    })
    return cenarios, elegiveis

def resumir_retencao(cenarios):
    principal = cenarios['Principal']
    linhas = []
    for cenario, df in cenarios.items():
        for (empresa, ano), referencia in principal.groupby(['stock', 'ano']):
            grupo = df.loc[df['stock'].eq(empresa) & df['ano'].eq(ano)]
            linhas.append({'cenario': cenario, 'stock': empresa, 'ano': ano,
                'n_principal': len(referencia), 'n_retidos': len(grupo),
                'retencao_pct': 100 * len(grupo) / len(referencia),
                'noticias_principal': int(referencia['n_noticias'].sum()),
                'noticias_retidas': int(grupo['n_noticias'].sum())})
    return pd.DataFrame(linhas)
