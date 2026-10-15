# Integração com pregões e retornos — etapa 17–19/10

Etapa iniciada e executada em **15/10/2026**. O [notebook 03](../notebooks/03_integracao_retornos.ipynb) associa as manchetes ao primeiro pregão estritamente posterior, calcula retornos ajustados e exporta uma base com uma linha por empresa/pregão. A classificação FinBERT e a revisão humana existentes foram preservadas.

## Resultado verificado

| Verificação | Resultado |
|---|---:|
| Associações notícia/empresa preservadas e mapeadas | 6.552 |
| Pares empresa/data civil de origem | 2.569 |
| Pares empresa/pregão com notícias, incluindo margem | 2.392 |
| Pregões que recebem notícias de várias datas | 152 |
| Painel de 2017–2019: cinco empresas × 754 pregões | 3.770 |
| Pares do painel com notícias no recorte | 2.390 |
| Pares do painel sem notícias no recorte | 1.380 |
| Pares com notícias e janela completa para a análise principal | 2.387 |
| Notícias sem pregão ou sem retorno | 0 |
| Sessões ausentes ou extras em relação ao calendário XNYS | 0 |

As oito células de código foram executadas em ordem no kernel Python (AED Sentimento), sem erros. Nove casos de datas conhecidas cobrem dia útil, fim de semana, feriado, fechamento extraordinário e virada do ano. A auditoria independente conferiu o calendário contra comunicados históricos da ICE/NYSE. O [registro datado](execucoes/integracao_2026-10-15.json) documenta versões, hashes e contagens. A revisão por outro integrante continua recomendada para a entrega do grupo.

## Unidade e regras

1. Calcular os retornos na série completa de preços com margem, antes do recorte: `retorno_pct = 100 × (adj_close / adj_close_anterior − 1)`. O retorno absoluto é seu módulo; ambos estão em porcentagem. A primeira cotação do snapshot fica sem retorno por não possuir antecedente, fora do painel principal.
2. Associar cada manchete ao primeiro pregão com data estritamente maior que `news_date`, usando as sessões observadas da própria empresa após a validação externa do calendário. Preservar a data original e conferir `trade_date_anterior ≤ news_date < trade_date`.
3. Reagrupar todas as manchetes mapeadas por `stock + trade_date`. Usar médias das probabilidades com peso igual por manchete, escore positivo menos negativo, intensidade como módulo do escore e classe por maior probabilidade média. Tratar empates com tolerância `1e-8`. Não calcular uma média simples de médias diárias com contagens diferentes.
4. Construir o painel de pregões 2017–2019. Onde não há manchetes, preencher somente contagens com zero e registrar `sem_noticias_no_recorte`. Escores, probabilidades e classe ficam ausentes. Ausência no corpus não é classe neutra.
5. Para comparações principais com retornos, usar `tem_noticias & elegivel_analise_principal`. O filtro de ao menos três notícias usa a contagem por empresa/pregão. A tabela por manchete é de auditoria e não representa uma amostra de retornos independentes.

Manchetes compartilhadas entre empresas são mantidas. Uma manchete repetida em datas diferentes não é excluída automaticamente, pois a chave de limpeza inclui a data. Séries temporais e manchetes compartilhadas implicam dependência entre unidades; o projeto é exploratório.

## Bordas do recorte

No primeiro pregão de 2017, a janela desde o pregão anterior começa em dezembro de 2016, fora do recorte de notícias. Os cinco pares desse pregão são preservados e marcados com `janela_noticias_completa=False`; três deles têm notícias no recorte. Por isso há 2.387 pares com notícias elegíveis na análise principal, entre os 2.390 observados no painel.

Seis notícias de **31/12/2019**, três NFLX e três NVDA, apontam para **02/01/2020**. Foram preservadas na tabela por notícia e nos dois agregados de margem, com `retorno_no_recorte=False` e janela incompleta, pois notícias de 01/01/2020 não pertencem ao recorte de entrada. Esses dois grupos ficam fora do painel principal e disponíveis para sensibilidade.

O alinhamento usa a data civil disponibilizada pela fonte. Não transforma datas sem horário em horários confiáveis, nem distingue publicação antes/depois da negociação. O retorno pode refletir notícias anteriores, informações ausentes e movimentos já descritos nas manchetes; não há identificação causal.

## Snapshot e calendário

Adotamos integralmente a coleta Yahoo/yfinance registrada em **09/10/2026 às 21:42:24 UTC**: 15/12/2016–10/01/2020, 772 sessões por empresa. O CSV tratado tem SHA-256 `86bf50f857b80899c760a46fb919dd1d72b8e6fe1c80374a4d82f066bbde0d1d`. A configuração e o manifesto também registram o hash do snapshot bruto e os parâmetros da coleta. Nenhum preço foi baixado novamente ou interpolado nesta etapa.

O notebook compara cada série com **XNYS**, de `exchange-calendars==4.13.2`. A revisão independente comparou as 772 datas com dias úteis menos a lista histórica de feriados ICE/NYSE, incluindo **05/12/2018**, sem diferenças. Os oito pregões reduzidos de 2017–2019 estão presentes nas cinco ações; seu fechamento antecipado não altera a regra por data adotada.

- [Calendário ICE/NYSE 2017–2019](https://ir.theice.com/press/news-details/2016/NYSE-Group-announces-2018-and-2019-holiday-and-early-closings-calendar/default.aspx).
- [Calendário ICE/NYSE 2018–2020](https://ir.theice.com/press/news-details/2017/NYSE-Group-Announces-2018-2019-and-2020-Holiday-and-Early-Closings-Calendar/default.aspx).
- [Calendário com 26/12/2016](https://ir.theice.com/press/news-details/2016/NYSE-Group-Announces-2017-Holiday-and-Early-Closings-Calendar/default.aspx).
- [Fechamento extraordinário de 05/12/2018](https://ir.theice.com/press/news-details/2018/New-York-Stock-Exchange-to-Honor-President-George-H-W-Bush/default.aspx).
- [Biblioteca exchange_calendars](https://github.com/gerrymanoim/exchange_calendars).

## Executar e encontrar os resultados

O pacote local inclui as entradas fixadas e pode começar diretamente pelo notebook 03. Em um clone novo, as etapas 01 e 02 geram as entradas. Para reproduzir exatamente esta execução, obtenha os dados do pacote do grupo e confira os hashes em `docs/config_integracao.json`. Se outra coleta divergir, a primeira célula interrompe a execução. Uma nova coleta só deve ser assumida explicitamente, conforme a explicação dessa célula; o manifesto registrará os novos hashes.

Instale as dependências de `requirements.txt`, abra o Jupyter na pasta do projeto e selecione **Python (AED Sentimento)**. Execute `notebooks/03_integracao_retornos.ipynb` do início ao fim. Este notebook não precisa de rede quando as entradas e a biblioteca de calendário já estão disponíveis.

| Arquivo gerado localmente | Uso |
|---|---|
| `data/processed/base_integrada_pregoes.csv` | Painel principal: 3.770 pares empresa/pregão; filtro de elegibilidade explícito. |
| `data/processed/sentimento_por_pregao.csv` | 2.392 grupos com notícias e retorno, incluindo os dois grupos de margem. |
| `data/processed/noticias_pregao_retornos.csv` | 6.552 associações com datas e valores preservados para rastreabilidade. |
| `data/processed/retornos_cotacoes.csv` | Série completa de preços e retornos, incluindo margem. |
| `docs/mapa_datas_pregoes.csv` | Correspondência dos 2.569 pares empresa/data civil. |
| `docs/resumo_integracao_por_empresa.csv` | Contagens por empresa. |
| `docs/auditoria_calendario.csv` | Diferenças contra XNYS; vazio nesta execução. |
| `docs/casos_calendario.csv` | Nove casos conhecidos e suas respostas. |
| `docs/grupos_varias_datas.csv` | 152 pregões que recebem várias datas de notícias. |
| `docs/noticias_retorno_fora_recorte.csv` | Seis notícias com retorno em janeiro de 2020. |
| `docs/manifesto_integracao.json` | Hashes, versões e auditoria da execução corrente. |

O [dicionário de integração](dicionario_integracao.csv) explica os novos campos. No GitHub ficam o notebook, a configuração, o dicionário, este guia e o registro datado. Bases completas e relatórios correntes são gerados localmente e não são versionados.

## Próxima etapa — 20–23/10

Produzir gráficos e interpretações das perguntas 1 a 6 e a primeira comparação da pergunta 7. A integração está concluída; as associações ainda não foram interpretadas. Registrem as hipóteses exploratórias antes de comparar resultados e definam o critério de manchetes retrospectivas. Esse filtro ainda está pendente.
