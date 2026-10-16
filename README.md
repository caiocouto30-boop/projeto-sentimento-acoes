# Sentimento das notícias e comportamento de ações dos EUA

Projeto de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**, professor João Rulff.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

## Leia o artigo

O [**notebook principal — artigo em desenvolvimento**](notebooks/00_artigo.ipynb) reúne introdução, dados, método, sete perguntas de domínio, resultados disponíveis, conclusões provisórias, limitações e referências. Esse é o ponto de entrada para a leitura acadêmica do projeto.

Investigamos associações descritivas entre o tom de manchetes financeiras e os retornos e oscilações de NVIDIA (NVDA), Netflix (NFLX), Bank of America (BAC), Johnson & Johnson (JNJ) e Coca-Cola (KO), em **2017–2019**, sem atribuir causalidade. A contribuição central é a visualização e a interpretação dos dados.

A etapa planejada para **20–23/10 foi executada antecipadamente em 16/10/2026**: gráficos e primeiras respostas às perguntas 1–6, além da sensibilidade inicial da pergunta 7. O artigo continua em desenvolvimento, com a exclusão de manchetes retrospectivas e os filtros combinados ainda pendentes.

## Estado registrado em 16/10/2026

| Componente | Resultado disponível |
| --- | --- |
| Limpeza | 6.556 associações no recorte; quatro duplicatas removidas; **6.552 mantidas** |
| Cotações | **754 pregões por empresa** em 2017–2019; 772 com margem |
| FinBERT | **6.019 textos distintos**, recompostos nas 6.552 associações |
| Agregado por data civil | **2.569 pares empresa/data da notícia** |
| Revisão qualitativa | 50 casos preenchidos por `caio`; **39 concordâncias e 11 divergências**, em amostra dirigida |
| Integração | **3.770 pares empresa/pregão**; 2.390 com notícias; **2.387 com notícias e janela completa** |
| Pergunta 1 | Mapa de cobertura, tabela anual e resposta descritiva disponíveis |
| Perguntas 2–3 | Proporções, séries diárias e leitura dos dez extremos disponíveis |
| Perguntas 4–6 | Boxplots, dispersões e correlações por empresa/ano com primeiras interpretações |
| Pergunta 7 | Comparação principal × mínimo de três: 2.387 → 783 pares; retrospectivas e combinação de filtros pendentes |

As 39 concordâncias em 50 casos não estimam a acurácia geral do modelo. Os rótulos humanos permanecem separados das previsões automáticas. Os registros datados preservam o estado ao término de cada etapa; a integração foi executada depois da etapa FinBERT.

## Organização e ordem de leitura

| Arquivo | Papel |
| --- | --- |
| [00_artigo.ipynb](notebooks/00_artigo.ipynb) | Texto principal, resultados salvos e delimitação do que ainda falta |
| [01_preparacao_inicial.ipynb](notebooks/01_preparacao_inicial.ipynb) | Apoio: limpeza, auditoria e cobertura, com explicações junto ao código |
| [02_sentimento_finbert.ipynb](notebooks/02_sentimento_finbert.ipynb) | Apoio: classificação, agregado por data civil e revisão humana |
| [03_integracao_retornos.ipynb](notebooks/03_integracao_retornos.ipynb) | Apoio: calendário, alinhamento, retornos e painel |
| [04_analise_visual.ipynb](notebooks/04_analise_visual.ipynb) | Apoio: nove gráficos, onze tabelas e sensibilidade inicial, com 12 células explicadas |
| [docs/README.md](docs/README.md) | Índice documental, relatórios e registros de execução |
| [resultados_registrados.json](docs/resultados_registrados.json) | Tabelas já calculadas, transcritas das saídas salvas, com origem verificável |

Os notebooks de apoio preservam todas as células de código e saídas existentes. O artigo centraliza a narrativa; não duplica nem substitui o processamento. As tabelas transcritas são um registro fixo da versão de referência, não uma base completa nem um relatório atualizado automaticamente.

## Como ler e executar o artigo

Abra `notebooks/00_artigo.ipynb` no GitHub ou no Jupyter. As saídas já estão salvas. Para reconstruir sua apresentação, execute as quatro células em ordem, a partir da raiz do projeto ou de `notebooks/`. Elas requerem Python, pandas e IPython, e leem somente arquivos versionados. Não precisam do CSV bruto, de internet ou do FinBERT.

Isso verifica a leitura dos resultados registrados; **não equivale a reproduzir o processamento integral**.

## Como reproduzir o processamento integral

1. Clone o repositório e entre na pasta do projeto. Utilize **Python 3.11** com as dependências de `requirements.txt`.
2. Se já tiver o ambiente Conda `aed-sentimento`, ative-o. Em outro computador, crie um ambiente Python e instale as dependências. Registre o kernel e abra o Jupyter a partir da pasta do projeto:

   ```text
   python -m pip install -r requirements.txt
   python -m ipykernel install --user --name aed-sentimento --display-name "Python (AED Sentimento)"
   python -m notebook
   ```

   O ambiente contém Python e bibliotecas; a pasta contém os arquivos; o kernel **Python (AED Sentimento)** deve apontar para o ambiente escolhido. `requirements.txt` registra a versão CPU do PyTorch; sua obtenção pode exigir o índice oficial de pacotes CPU, conforme a plataforma.

3. Baixe `raw_analyst_ratings.csv` do [dataset do Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests) e coloque-o em `data/raw/`.
4. Execute **01_preparacao_inicial.ipynb** em ordem. Sem snapshot, a coleta de cotações exige internet. Para reproduzir exatamente a execução datada, obtenha o snapshot do grupo e confira os hashes.
5. Execute **02_sentimento_finbert.ipynb** em ordem. O primeiro carregamento permite baixar a revisão fixada do modelo; o cache local permite reutilizar probabilidades compatíveis. A [amostra humana preenchida](docs/revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) é preservada; o leitor aceita vírgula ou ponto e vírgula.
6. Execute **03_integracao_retornos.ipynb** em ordem. Ele verifica as entradas fixadas e o calendário XNYS, e gera `base_integrada_pregoes.csv`. Outra coleta deve ser assumida explicitamente conforme as instruções do notebook; não desative uma conferência para contornar uma diferença não investigada.
7. Execute **04_analise_visual.ipynb** em ordem. Ele confere os hashes em `docs/config_analise_visual.json` e gera os resumos e imagens sem rede, coleta ou inferência. As entradas exatas estão no pacote local do grupo.
8. Confira os CSVs e manifestos locais. O artigo e `docs/resultados_registrados.json` descrevem a execução de referência: se as entradas ou resultados mudarem, reconcilie as contagens e atualize a narrativa e sua origem antes de publicar outra versão.

Os dados completos, o CSV original, os snapshots e os pesos **não estão versionados**. Os notebooks e registros existentes documentam execuções anteriores; a revisão editorial anterior executou as células de leitura do artigo. A etapa visual de 16/10 executou as 12 células do notebook 04; as etapas 01–03 não foram recalculadas. A reprodução integral por outro integrante continua pendente. `requirements.txt` reúne dependências diretas com versões observadas; não é um lock completo ou multiplataforma.

## Fontes e decisões metodológicas

- **Notícias:** [Daily Financial News for 6000+ Stocks](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests). SHA-256 do original utilizado: `609289a49dc8af2bd28a8466dffd9663521237026f1040c0f238010b29135fb6`.
- **Preços:** [Yahoo Finance via yfinance](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html), fechamento ajustado e volume, de 15/12/2016 a 10/01/2020. O snapshot é fixado por hash; outra coleta pode apresentar ajustes diferentes.
- **Sentimento:** [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert), revisão `4556d13015211d73dccd3fdd39d39232506f3e43`, sem treinamento adicional. Escore `P(positivo) − P(negativo)`; classe agregada pela maior probabilidade média, com empates explícitos.

Manchetes compartilhadas são preservadas. Dias sem notícias não são neutros. O notebook 02 agrega por data civil; o 03 mapeia ao primeiro pregão estritamente posterior e agrega por empresa/pregão, com peso igual por manchete. Para comparar sentimento e retorno, utilize `tem_noticias & elegivel_analise_principal`. Seis notícias com retorno em janeiro de 2020 são preservadas como margem. Retorno absoluto mede magnitude diária, não uma estimativa formal de volatilidade. Veja os relatórios de [sentimento](docs/finbert.md) e [integração](docs/integracao.md).

## Entregas acadêmicas

- **29/10/2026:** notebook em forma de artigo, ainda que incompleto, e apresentação de cinco minutos.
- **Semana A2:** notebook final, repositório, apresentação de dez minutos e declaração de contribuições. A janela 23–30/11 foi informada pelo grupo; o dia exato precisa ser confirmado. A meta de 22/11 é interna.

A estrutura do artigo já está organizada. Permanecem as melhorias listadas no [relatório visual](docs/analise_visual.md), a apresentação, o retorno do professor e a documentação das contribuições. A existência dos arquivos não demonstra envio ou aprovação de uma entrega.
