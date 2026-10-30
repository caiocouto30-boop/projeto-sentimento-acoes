# Integração com pregões e retornos

A última parte do [notebook de preparação](../notebooks/01_preparacao_dados.ipynb) associa notícias e cotações e gera as bases utilizadas pelo [artigo](../notebooks/00_artigo.ipynb). Ela preserva as previsões FinBERT e a revisão humana.

## Regras do método

1. Conferir as datas das cinco séries com o calendário **XNYS**, de `exchange-calendars`, incluindo o fechamento extraordinário de 05/12/2018. Não interpolar preços.
2. Calcular na série completa, antes do recorte, `retorno_pct = 100 × (adj_close / adj_close_anterior − 1)`. O retorno absoluto é o módulo dessa medida, também em porcentagem.
3. Associar cada manchete ao **primeiro pregão estritamente posterior** à sua data civil. Conferir `trade_date_anterior ≤ news_date < trade_date` e manter a data original.
4. Agregar por empresa/pregão com peso igual por manchete: médias das três probabilidades, escore positivo menos negativo e classe por maior probabilidade média. Empates usam tolerância `1e-8`.
5. Construir o painel de 2017–2019. Sem notícias, preencher apenas contagens com zero; probabilidades, escore e classe permanecem ausentes. Para a análise principal, usar `tem_noticias & elegivel_analise_principal`.

O mínimo de três notícias é aplicado por empresa/pregão. Manchetes compartilhadas entre empresas são mantidas. A tabela por manchete serve à rastreabilidade; suas linhas não são observações independentes de retorno.

## Amostras e bordas

| Unidade | Quantidade |
| --- | ---: |
| Associações notícia/empresa mapeadas | 6.552 |
| Pares empresa/data civil da notícia | 2.569 |
| Grupos empresa/pregão com notícias, incluindo margem | 2.392 |
| Painel: cinco empresas × 754 pregões | 3.770 |
| Pares do painel com notícias | 2.390 |
| Pares elegíveis com notícias na análise principal | 2.387 |

No primeiro pregão de 2017, a janela começa em dezembro de 2016, antes do recorte de notícias. Os cinco pares desse pregão são preservados, mas marcados como janela incompleta; três têm notícias no recorte. Isso explica a passagem de 2.390 para 2.387 pares elegíveis.

Seis notícias de 31/12/2019, três NFLX e três NVDA, apontam para 02/01/2020. Permanecem na tabela por notícia e nos dois grupos de margem, com retorno fora do recorte e janela incompleta. Não entram no painel principal.

## Entradas, saídas e limites

O snapshot incluído tem 772 sessões por empresa entre 15/12/2016 e 10/01/2020, coletadas do Yahoo Finance via `yfinance`. Ele e seus parâmetros são conservados em [data/raw/](../data/README.md); a [proveniência](proveniencia.json) registra hashes e origens. A preparação atual não faz nova coleta.

As bases versionadas são [base_integrada_pregoes.csv](../data/processed/base_integrada_pregoes.csv), com o painel, e [noticias_pregao_retornos.csv](../data/processed/noticias_pregao_retornos.csv), com a correspondência por notícia. Os demais intermediários de retornos e agregação são gerados localmente. O [dicionário](dicionario_integracao.csv) explica os campos; os [registros históricos](execucoes/) documentam as versões anteriores, sem substituir as instruções atuais.

O alinhamento por data não recupera horários de publicação nem distingue notícias de antes ou depois da negociação. O retorno pode refletir informações anteriores, ausentes ou já descritas pela manchete. As séries e manchetes compartilhadas também geram dependência entre observações. As conclusões são exploratórias e não identificam causalidade.
