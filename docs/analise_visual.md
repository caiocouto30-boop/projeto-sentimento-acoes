# Análise visual

O [artigo](../notebooks/00_artigo.ipynb) concentra os cálculos finais, os sete gráficos interativos e suas interpretações.

| Perguntas | Unidade e amostra |
| --- | --- |
| 1–2 | 6.552 associações manchete–empresa |
| 3 | 2.569 pares empresa/data civil; extremos gerais e extremos com três ou mais manchetes |
| 4–6 | 2.387 pares empresa/pregão com notícias e janela completa |
| 7 | Principal: 2.387; mínimo de três: 783; sem retrospectivas explícitas: 2.271; combinado: 697 |

Spearman é a correlação dos postos médios; grupos constantes ou insuficientes ficam sem coeficiente. O ano é o do pregão de resposta. As escalas são comuns e os retornos extremos são preservados. Ausência no corpus permanece sem sentimento. Intensidade é o módulo do escore médio, que permite compensação de tons opostos.

## Robustez

O [protocolo textual](retrospectivas/README.md) fixa a regra e identifica as marcações como automáticas. Nos cenários de exclusão, as probabilidades são reagregadas por empresa/pregão antes de recalcular classe, escore, intensidade e contagem. Só depois se aplica o mínimo de três. O filtro ampliado de sinais não conclusivos é uma sensibilidade adicional, com 2.243 ou 670 pares.

A retirada de retrospectivas não cria uma relação uniforme entre empresas. Alguns sinais mudam após restringir quantidade, com grupos menores e retenção desigual. Essa sensibilidade não demonstra significância, causalidade ou desempenho preditivo. A falta de validação humana independente da marcação limita a resposta à Q7.

## Saídas

A última célula do artigo exporta as tabelas em `docs/analise_visual/`, incluindo os seis cenários, retenção por empresa/ano, distribuições por classe e os textos dos extremos com suporte. A marcação dos 6.019 textos está em `docs/retrospectivas/marcacao_textos.csv`. A base dos cenários fica localmente em `data/processed/base_robustez_cenarios.csv`.

O exportador `tools/exportar_artigo.py` gera o HTML offline, as sete imagens e um manifesto com hashes. O notebook conserva imagem e especificação para cada gráfico. A narrativa deve ser conferida se as entradas mudarem.

Referências técnicas: [agregações pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html), [postos](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html) e [interações Altair](https://altair-viz.github.io/user_guide/interactions/parameters.html).
