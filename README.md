# Sentimento de notícias e retornos de cinco ações dos EUA

Projeto final de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**, professor João Rulff.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

Investigamos associações entre manchetes financeiras e retornos de NVDA, NFLX, BAC, JNJ e KO em 2017–2019. O estudo combina notícias do Kaggle, probabilidades de um FinBERT pronto e cotações ajustadas do Yahoo Finance, com análise descritiva e visual.

## Documento principal

Abra o **[notebook-artigo](notebooks/00_artigo.ipynb)**. As transformações pandas, medidas, gráficos Altair, tabelas e interpretações estão nas próprias células. O [HTML](artigo_interativo.html) é uma exportação do notebook salvo.

| Arquivo | Uso |
| --- | --- |
| [notebooks/00_artigo.ipynb](notebooks/00_artigo.ipynb) | Artigo final: 46 células, sendo 15 de código |
| [notebooks/01_preparacao_dados.ipynb](notebooks/01_preparacao_dados.ipynb) | Preparação original, FinBERT e integração |
| [docs/README.md](docs/README.md) | Método, dados, origem e reprodução |
| [docs/analise_final/](docs/analise_final/) | Tabelas e verificações da análise final |

Na Q3, o hover mostra empresa, data, escore médio, quantidade e até três manchetes completas. O tamanho dos pontos representa a quantidade de notícias; o seletor e a seleção de datas conservam a exploração da série temporal. Os títulos são exemplos ordenados pelo módulo do escore individual; não representam isoladamente a média do grupo.

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

O executor padrão usa um kernel Jupyter. Na verificação desta revisão, as 15 células foram executadas no IPython InteractiveShell, com saídas reais e sete especificações Altair válidas; a tentativa de iniciar um processo separado de kernel não terminou no ambiente restrito. O modo usado está disponível com `python tools/executar_artigo.py --modo ipython`. Use `--pasta notebooks` para repetir a execução com esse diretório de trabalho.

O exportador lê o notebook salvo e gera o HTML, sem reconstruir suas células. O verificador compara as tabelas do notebook com cálculos independentes, incluindo os 120 coeficientes dos seis cenários de robustez. Veja [o registro de verificação](docs/analise_final/verificacao_notebook.json).

Confie no notebook no Jupyter para ativar suas saídas HTML. A renderização Altair pode carregar bibliotecas JavaScript de uma CDN. O GitHub pode não executar os gráficos: use Jupyter ou baixe o HTML e abra no navegador com conexão.

## Resultados e alcance

H1 recebe apoio descritivo: a cobertura é desigual. H2 não recebe apoio uniforme nas duas definições de intensidade. H3 encontra variação descritiva entre empresas e anos, sem demonstrar diferenças estruturais. Os retornos por classe se sobrepõem e as correlações são pequenas. Os filtros alteram a composição e alguns sinais, sem estabelecer causalidade ou capacidade preditiva.

Os snapshots e a revisão humana anterior foram preservados. A regra de retrospectivas permanece automática, conservadora e sem validação humana independente. Consulte [os dados](data/README.md), [a origem da revisão](docs/origem_notebook.json) e [as alterações metodológicas](docs/correcao_notebook.md).

## Antes do envio

Conferir visualmente tooltips, zoom e seletores no Jupyter; reproduzir por outro integrante; preparar e ensaiar a apresentação de dez minutos; registrar as contribuições efetivas; confirmar a data e o procedimento da Semana A2. A presença dos arquivos não comprova envio à disciplina.
