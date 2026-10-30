# Dados e reprodução

As entradas e as três bases necessárias ao [artigo](../notebooks/00_artigo.ipynb) estão incluídas. Para reconstruí-las, execute o [notebook de preparação](../notebooks/01_preparacao_dados.ipynb) inteiro: limpeza → FinBERT → integração. As origens, configurações e hashes estão em [proveniência](../docs/proveniencia.json).

## Entradas preservadas em `raw/`

| Arquivo | Conteúdo |
| --- | --- |
| [noticias_recorte_original.csv](raw/noticias_recorte_original.csv) | 6.556 associações de cinco empresas em 2017–2019, antes da limpeza; campos originais, quatro duplicatas e posição `source_row` no CSV completo preservados |
| [cotacoes_yahoo_margem.csv](raw/cotacoes_yahoo_margem.csv) | Snapshot do Yahoo Finance, coletado via `yfinance`, com fechamento ajustado, volume e margem de 15/12/2016 a 10/01/2020 |
| [cotacoes_yahoo_margem.json](raw/cotacoes_yahoo_margem.json) | Fonte, data, parâmetros e hash do snapshot |
| [finbert_probabilidades.csv](raw/finbert_probabilidades.csv) | Probabilidades das três classes para os 6.019 textos distintos |
| [finbert_configuracao.json](raw/finbert_configuracao.json) | Modelo, revisão fixada, limite de tokens e versões usadas no cache |

O recorte vem de *Daily Financial News for 6000+ Stocks*, disponível no [Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests). O CSV completo tem 1.407.328 linhas; seu nome e hash constam da proveniência. Filtrar empresas e período não normaliza manchetes nem elimina duplicatas: essas operações permanecem visíveis no notebook.

O snapshot conserva a coleta original para evitar mudanças nos ajustes históricos. `yfinance` identifica a origem dos preços; não é usado pela preparação atual para baixar novas cotações.

## Bases incluídas em `processed/`

| Arquivo | Conteúdo |
| --- | --- |
| [noticias_com_sentimento.csv](processed/noticias_com_sentimento.csv) | 6.552 associações limpas, classificadas pelo FinBERT, com identificadores originais |
| [base_integrada_pregoes.csv](processed/base_integrada_pregoes.csv) | Painel de 3.770 pares empresa/pregão; 2.387 pares com notícias elegíveis para a análise principal |
| [noticias_pregao_retornos.csv](processed/noticias_pregao_retornos.csv) | Associações por notícia com pregão e retorno, incluindo a margem fora do painel |

A preparação também gera intermediários, como notícias limpas, cotações tratadas e agregados de sentimento. Eles ficam em `processed/`, são ignorados pelo Git e podem ser reconstruídos. As tabelas das perguntas ficam em `docs/analise_visual/` e são atualizadas pelo artigo. A revisão humana original fica em [docs/revisao_manual/](../docs/revisao_manual/), separada das previsões automáticas.
