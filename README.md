# Sentimento de notícias e retornos de cinco ações dos EUA

Projeto final de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**, professor João Rulff.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

Investigamos associações entre manchetes financeiras e retornos de NVDA, NFLX, BAC, JNJ e KO em 2017–2019. O estudo combina notícias do Kaggle, probabilidades de um FinBERT pronto e cotações ajustadas do Yahoo Finance, com análise descritiva e visual.

## Materiais da entrega final

Abra o **[notebook-artigo](notebooks/00_artigo.ipynb)**. As transformações pandas, medidas, gráficos Altair, tabelas e interpretações estão nas próprias células. O [HTML](artigo_interativo.html) é uma exportação do notebook salvo.

| Arquivo | Uso |
| --- | --- |
| [notebooks/00_artigo.ipynb](notebooks/00_artigo.ipynb) | Artigo final: 46 células, sendo 15 de código |
| [Apresentação de dez minutos](apresentacao/apresentacao.pdf) | Oito slides em PDF para projeção |
| [Roteiro de apresentação](apresentacao/roteiro.md) | Tempos, divisão de fala e demonstração da Q3 |
| [Declaração de contribuições](DECLARACAO_CONTRIBUICOES.md) | Atividades de cada integrante e revisão conjunta |
| [notebooks/01_preparacao_dados.ipynb](notebooks/01_preparacao_dados.ipynb) | Preparação original, FinBERT e integração |
| [docs/README.md](docs/README.md) | Método, dados, origem e reprodução |
| [docs/analise_final/](docs/analise_final/) | Tabelas e verificações da análise final |

Para ler as manchetes, [baixe o artigo interativo](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/raw/refs/heads/main/artigo_interativo.html) e abra o HTML no navegador. Passe o mouse nos seguintes pontos.

| Figura | O que o marcador representa | O que aparece no ponto |
| --- | --- | --- |
| Q3, série temporal | Empresa e data civil | Até três manchetes reais do dia e a contagem das demais |
| Q4, círculos fora dos bigodes | Pregão com retorno extremo dentro da empresa e classe | Manchete de exemplo, data, empresa, quantidade e retorno |
| Q5 e Q6, dispersões | Empresa e pregão | Manchete de exemplo da janela e dados do pregão |

Nos pregões com uma notícia, o título é o dessa notícia. Com várias, o exemplo é o título de maior módulo do escore individual, com desempate pela ordem no arquivo de origem. As caixas da Q4 resumem distribuições, e os símbolos da Q7 representam coeficientes calculados sobre vários pregões.

Na Q5, o seletor alterna **intensidade líquida = |média(sᵢ)|** e **intensidade média = média(|sᵢ|)**, mantendo os mesmos 2.387 pares. A Q7 recalcula as medidas com os textos retidos em cada cenário e apresenta retenção e coeficientes por empresa.

## Reprodução

O ambiente verificado usa **Python 3.11.16, Altair 6.3.0, pandas 3.0.6 e NumPy 2.4.6**. Clone ou baixe o repositório completo e, na raiz, execute:

```text
python -m pip install -r requirements-notebook.txt
python -m notebook
```

Selecione o ambiente Python correspondente, abra `notebooks/00_artigo.ipynb`, execute as células em ordem e salve. Os dados e as probabilidades incluídos permitem começar diretamente pelo artigo, sem novo treinamento ou coleta de preços. A preparação integral em `01_preparacao_dados.ipynb` usa dependências adicionais de `requirements.txt` e pode precisar de internet para tokenizador ou pesos caso falte cache.

Também é possível executar, conferir e exportar pelo terminal:

```text
python tools/executar_artigo.py
python tools/verificar_notebook.py
python tools/exportar_artigo.py
```

O executor abre um kernel Jupyter novo por padrão. Para reproduzir a execução a partir da pasta do notebook, use `python tools/executar_artigo.py --pasta notebooks`. As saídas salvas no repositório foram produzidas em IPython. A execução independente em Jupyter reproduziu as 15 células e passou no verificador. [Registro da execução](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/actions/runs/44964338148).

O exportador lê o notebook salvo e gera o HTML, sem reconstruir suas células. O verificador compara as tabelas do notebook com cálculos independentes, incluindo os 120 coeficientes dos seis cenários de robustez. Veja [o registro de verificação](docs/analise_final/verificacao_notebook.json).

O HTML incorpora a biblioteca das sete figuras. Em um teste com o Chrome offline, os marcadores de Q3 a Q6 mostraram as manchetes correspondentes. [Teste no navegador](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/actions/runs/44964401509/job/137030055149). No Jupyter, marque o notebook como confiável para ativar as saídas interativas do Altair. Essas saídas podem precisar de internet.

## Resultados e alcance

H1 recebe apoio descritivo: a cobertura é desigual. H2 não recebe apoio uniforme nas duas definições de intensidade. H3 encontra variação descritiva entre empresas e anos, sem demonstrar diferenças estruturais. Os retornos por classe se sobrepõem e as correlações são pequenas. Os filtros alteram a composição e alguns sinais, sem estabelecer causalidade ou capacidade preditiva.

Os snapshots e a revisão humana anterior foram preservados. A regra de retrospectivas permanece automática, conservadora e sem validação humana independente. Consulte [os dados](data/README.md), [a origem da revisão](docs/origem_notebook.json) e [as alterações metodológicas](docs/correcao_notebook.md).
