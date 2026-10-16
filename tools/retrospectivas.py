"""Regra textual conservadora: identifica relatos explícitos de preço já observado.

Usa somente a manchete. Não consulta probabilidades, empresa, datas ou retornos.
Casos ambíguos ficam na análise principal de exclusão de retrospectivas explícitas.
"""
import re

VERSAO_REGRA = '1.0'
ADVERBIOS = r'(?:(?:are|is|was|were|now|currently|still|already|have been|has been|slightly|sharply|modestly|notably|also|all|mostly)\s+)*'
VERBOS = r'(?:rises?|risen|rising|rose|falls?|falling|fell|jump(?:s|ed|ing)?|drop(?:s|ped|ping)?|gain(?:s|ed|ing)?|loses?|losing|lost|climb(?:s|ed|ing)?|slid(?:es?|ing)?|slump(?:s|ed|ing)?|surg(?:es?|ed|ing)|rall(?:ies|ied|ying)|plung(?:es?|ed|ing)|tumbl(?:es?|ed|ing)|soar(?:s|ed|ing)?|spik(?:es?|ed|ing)|rebound(?:s|ed|ing)?|declin(?:es?|ed|ing)|advanc(?:es?|ed|ing)|sinks?|sinking|sank|sunk|dips?|dipped|dipping|opened|closed|finished)'
EMPRESAS = r'(?:\$?(?:BAC|JNJ|KO|NFLX|NVDA)|Nvidia|Netflix|Bank of America|BofA|Johnson\s*(?:&|and)\s*Johnson|Coca[- ]Cola)'
PADROES = [
    ('negociacao_observada', r'\b(?:shares|stocks?|share prices?)\b[^;!?]{0,220}?\b(?:trading|moving|trades?)\s+(?:higher|lower|up|down)\b'),
    ('movimento_intradiario', r'\b(?:shares|stocks?)\s+(?:tick(?:s|ed|ing)?|ticker|edge(?:s|d)?|move(?:s|d)?|trade(?:s|d)?)\s+(?:(?:slightly|sharply)\s+)?(?:up|down|higher|lower)\b'),
    ('maxima_minima_listada', r'\bstocks?\s+(?:(?:that|which)\s+)?(?:made|hit|set|broke|makes?|making)\s+(?:new |fresh |all[- ]time |52[- ](?:week|wk) |record |session |multi[- ]year )*(?:highs?|lows?)\b'),
    ('cotacao_observada', rf'\b(?:shares|stocks?|share prices?)\s+{ADVERBIOS}(?:up|down|higher|lower)\b'),
    ('movimento_de_acao', rf'\b(?:shares|stocks?|share prices?)\s+{ADVERBIOS}{VERBOS}\b'),
    ('variacao_percentual_empresa', rf'\b{EMPRESAS}(?:[’\']s)?\s+(?:(?:Inc\.?|Corp\.?|Corporation)\s+)?{ADVERBIOS}(?:up|down|higher|lower|{VERBOS})\s+(?:(?:about|over|nearly|around|roughly|more than|less than|as much as)\s+)?[~+−-]?\d[\d.,]*\s*(?:%|percent\b)'),
    ('maxima_empresa', rf'\b{EMPRESAS}(?: Inc\.?)?\s+(?:makes?|hits?|reaches)\s+(?:a |new |fresh |all[- ]time |52[- ](?:week|wk) |record )+(?:highs?|lows?)\b'),
    ('negociacao_empresa', rf'\b{EMPRESAS}\s+(?:trades?|inches?|edges?)\s+(?:higher|lower|up|down)\b'),
    ('cotacao_atual_na_frase', r'\bshares\b[^;!?]{0,100}?\b(?:now|still|currently)\s+(?:up|down)\s+[~+−-]?\d[\d.,]*\s*%'),
    ('resumo_intradiario', r'\bmid[- ](?:day|afternoon|morning) market update\s*:'),
    ('referencia_mercado', rf'\b(?:markets|stock market|nasdaq|dow|s&p(?: 500)?|(?:technology|financial|bank|tech) stocks?)\s+{ADVERBIOS}(?:up|down|higher|lower|mixed|{VERBOS})\b'),
    ('maxima_minima_observada', r'\b(?:shares|stocks?|share prices?)\s+(?:hits?|reach(?:es|ed)?|touch(?:es|ed)?|at|near|sets?)\s+(?:a |an |new |fresh |all[- ]time |52[- ](?:week|wk) |record |session |multi[- ]year )*(?:highs?|lows?)\b'),
]
PADROES = [(nome, re.compile(texto, re.I)) for nome, texto in PADROES]
FUTURO = re.compile(r'\b(?:could|may|might|would|should|will|can|if|sees?|expects?|predicts?|forecasts?|potential|poised|likely|set to|expected to|why not|what if)\b', re.I)
SINAIS = re.compile(rf'\b(?:shares?|stocks?|{EMPRESAS})\b.{{0,85}}\b(?:up|down|higher|lower|{VERBOS}|rally|sell[- ]off|highs?|lows?|price action)\b', re.I)

def classificar(manchete):
    texto = str(manchete).strip()
    for nome, padrao in PADROES:
        achado = padrao.search(texto)
        if not achado:
            continue
        trecho = achado.group(0)
        # "Stock falls short" pode tratar de resultados, não da cotação.
        if re.search(r'\bfalls? short\b', texto, re.I):
            return 'ambigua', 'queda_pode_ser_resultado_operacional', trecho
        prefixo = texto[max(0, achado.start()-75):achado.start()]
        if nome == 'negociacao_observada':
            antes_negociacao = re.split(r'\b(?:trading|moving|trades?)\b', trecho, maxsplit=1, flags=re.I)[0]
            if FUTURO.search(antes_negociacao):
                return 'ambigua', 'negociacao_em_contexto_prospectivo', trecho
        # Uma negociação explicitamente observada continua retrospectiva se a
        # explicação também mencionar expectativas ou planos futuros.
        if nome != 'negociacao_observada' and (FUTURO.search(prefixo) or texto.endswith('?')):
            return 'ambigua', 'previsao_ou_pergunta', trecho
        return 'retrospectiva_explicita', nome, trecho
    achado = SINAIS.search(texto)
    if achado:
        return 'ambigua', 'contexto_de_preco_sem_relato_inequivoco', achado.group(0)
    return 'sem_indicio_explicito', 'nenhuma_regra_explicita', ''
