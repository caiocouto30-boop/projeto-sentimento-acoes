# Revisão pontual de simplicidade e interatividade — 16/10/2026

A revisão simplifica o percurso de leitura e acrescenta interatividade, preservando método e resultados. A versão de referência é a entrega acadêmica do commit `e51b22b29d5e792529140dbcffddc61f8431f0de`.

## O que mudou

O `00_artigo.ipynb` passou de quatro células que carregavam resumos/imagens a oito células diretas: uma de preparação e uma por pergunta. Cada pergunta apresenta transformação em pandas, gráfico Altair e interpretação. O aumento de código no artigo torna visíveis os cálculos antes espalhados no apoio; não representa um novo sistema de processamento.

Removemos do artigo as dependências de resumos JSON, carregamento de imagens PNG e travas SHA-256. Mantivemos quatro verificações curtas de significado: chave de notícia, chave de pregão, ausência de escore sem notícias e campos essenciais da amostra. A única função de análise compartilhada calcula Spearman pelos postos médios, sem exigir SciPy. A paleta por classe foi preservada.

O notebook 04 recebeu somente um aviso apontando para o artigo atual. Não duplicamos o novo código de visualização nele. As etapas 01–03, o processamento estático do 04, os dados, a revisão humana, as figuras anteriores e os registros históricos foram preservados. A simplificação se concentra no caminho de leitura e análise, sem reescrever a preparação que já funcionava.

| Pergunta | Visualização atual e interação |
| --- | --- |
| Q1 | Mapa mensal e barras totais ligados pela seleção de empresa; consulta de contagens |
| Q2 | Barras de 100%, com percentual, contagem e denominador no cursor |
| Q3 | Série de pontos com escolha de empresa, seleção de datas, extremos e manchete ilustrativa |
| Q4 | Boxplots por empresa/classe, com extremos preservados e resumos consultáveis |
| Q5 | Duas dispersões ligadas: seleção de pregões, filtro de empresa e dados/manchete no cursor |
| Q6 | Mapa de correlações que filtra a dispersão por empresa/ano; n e coeficiente explícitos |
| Q7 | Comparação das amostras principal e mínimo de três, com coeficientes e n no cursor |

As manchetes do cursor são exemplos selecionados pelo maior módulo do escore individual, com desempate por identificador de origem. Elas não substituem o conjunto de notícias que produziu o escore médio. Os filtros visuais não alteram as tabelas e a interpretação da amostra completa. Não modificamos a definição de intensidade, o alinhamento de pregões, as amostras nem o caráter descritivo dos resultados.

## Como usar

1. Para ler e explorar: baixe [artigo_interativo.html](../artigo_interativo.html) pelo GitHub e abra-o no navegador, ou abra o arquivo após clonar o projeto. Os sete gráficos têm bibliotecas e dados incorporados e funcionam sem internet; links externos de referência exigem conexão. O GitHub exibe o código do HTML, sem executar seus controles.
2. Para estudar ou refazer: abra `notebooks/00_artigo.ipynb` no Jupyter e execute as oito células na ordem. As três bases necessárias estão incluídas no pacote local. O CSV bruto e os pesos do FinBERT não são necessários para essa etapa.
3. Para refazer o HTML: após executar e salvar o notebook, execute `python tools/exportar_artigo.py` na pasta do projeto. O arquivo será criado na raiz do projeto. O exportador é opcional e mantém a lógica de exportação fora das células do artigo.

As novas dependências são `altair==6.3.0`, `vl-convert-python==1.9.0.post1` e `nbconvert==7.17.1`, acrescentadas a `requirements.txt`. O exportador usa também nbformat e BeautifulSoup, dependências instaladas pelo nbconvert. A linha de compatibilidade MKL do artigo evita o encerramento do cálculo de correlação observado no ambiente Windows do grupo; não muda os resultados matemáticos.

As saídas entregues contêm especificações interativas e imagens de apoio. O GitHub pode mostrar somente a imagem do notebook; use Jupyter ou HTML para os controles. O repositório inclui o artigo executado, o HTML, a documentação e o exportador. As bases completas e os materiais pessoais de estudo permanecem locais, cobertos pelas regras de exclusão existentes.

## Validação e limites

O artigo foi executado em sequência em um processo novo, com Python 3.11 e as dependências do ambiente `aed-sentimento`, acrescidas das bibliotecas de visualização em pasta isolada. As etapas de coleta, FinBERT e integração não foram reexecutadas.

A conferência compara as agregações e os coeficientes com as tabelas da entrega anterior, verifica a preservação das entradas e anotações humanas e renderiza os sete gráficos. Os controles de empresa da Q3/Q5 e a seleção de grupo na Q6 foram testados no navegador. O resultado detalhado acompanha a revisão em `validacao_revisao.md`.

Continuam pendentes a classificação revisada de retrospectivas, a reagregação após sua exclusão e os filtros combinados. Essas etapas exigem critérios e revisão do grupo; não foram presumidas como resolvidas pela melhoria visual.

Referências técnicas: [interações em Altair](https://altair-viz.github.io/user_guide/interactions/parameters.html) e [exportação com bibliotecas incorporadas](https://altair-viz.github.io/user_guide/saving_charts.html).
