# Sentimento de notícias e retornos de ações dos EUA

Projeto de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**, professor João Rulff.  
**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

Investigamos associações entre o tom de manchetes e os retornos de **NVDA, NFLX, BAC, JNJ e KO em 2017–2019**, com medidas descritivas e gráficos interativos. O FinBERT é utilizado pronto, sem treinamento adicional.

## Leitura

O [**notebook-artigo**](notebooks/00_artigo.ipynb) reúne dados, método, sete perguntas, transformações, gráficos e conclusões. Para explorar os controles sem Python, baixe o [**artigo HTML**](artigo_interativo.html) e abra no navegador; ele funciona offline. O GitHub exibe as imagens salvas do notebook.

A cobertura é desigual, os retornos por classe se sobrepõem e as correlações são pequenas. Os filtros de retrospectivas e quantidade alteram a composição e alguns sinais, sem um padrão uniforme entre empresas. As conclusões são exploratórias, sem interpretação causal.

## Organização

| Notebook | Função |
| --- | --- |
| [00_artigo](notebooks/00_artigo.ipynb) | Análise, gráficos e exportação das tabelas |
| [01_preparacao_inicial](notebooks/01_preparacao_inicial.ipynb) | Limpeza de notícias e validação das cotações |
| [02_sentimento_finbert](notebooks/02_sentimento_finbert.ipynb) | Classificação, cache e revisão qualitativa |
| [03_integracao_retornos](notebooks/03_integracao_retornos.ipynb) | Calendário, alinhamento temporal e retornos |

[Documentação](docs/README.md): fontes, decisões, registros e [revisão conforme o enunciado](docs/revisao_aed2026.md).

## Reprodução

Use **Python 3.11**. Na pasta do projeto:

```text
python -m pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt
python -m ipykernel install --user --name aed-sentimento --display-name "Python (AED Sentimento)"
python -m notebook
```

Selecione o kernel **Python (AED Sentimento)** e execute **01 → 02 → 03 → 00**, reiniciando o kernel entre notebooks. Para refazer o HTML e as imagens, salve o artigo executado e rode `python tools/exportar_artigo.py`.

- **Notícias:** baixe `raw_analyst_ratings.csv` do [Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests) e coloque em `data/raw/`.
- **Preços:** o notebook 01 reutiliza `cotacoes_yahoo_margem.csv` com seus metadados em `data/raw/`; sem snapshot, coleta via [yfinance](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html). Para repetir os valores desta versão, use o snapshot do pacote local e os hashes da [configuração](docs/config_integracao.json). Outra coleta pode alterar ajustes históricos e deve ser documentada.
- **Modelo:** o notebook 02 baixa a revisão fixada de [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) no primeiro uso e reaproveita probabilidades compatíveis. A [revisão humana](docs/revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) é preservada.

O pacote local inclui as bases preparadas para iniciar diretamente pelo artigo. CSVs completos, snapshots e pesos ficam fora do GitHub. As versões registradas são as do ambiente utilizado; `requirements.txt` não é um lock multiplataforma. Mudanças nas entradas exigem conferir os resultados e atualizar a narrativa.

## Situação acadêmica

O artigo atende à estrutura solicitada para a intermediária de **29/10**: dados definidos, hipóteses, uma seção por pergunta e conclusões provisórias. As sete perguntas têm respostas exploratórias. A pergunta 7 compara a principal (2.387 pares), mínimo de três (783), exclusão de retrospectivas explícitas (2.271) e filtro combinado (697), com reagregação. A [regra textual](docs/retrospectivas/README.md) é automática e conservadora, sem validação humana independente. O [guia de entrega](ENTREGA_29_10.md) reúne os arquivos e delimita o escopo; slides e ensaio ficaram fora desta tarefa.

Para a final na **Semana A2**, ainda são necessários a validação humana da marcação, o aprofundamento da análise e a incorporação do retorno do professor quando recebido, a apresentação de dez minutos e a declaração factual de contribuições do trio. A revisão não comprova entrega formal ou aprovação pelo professor.
