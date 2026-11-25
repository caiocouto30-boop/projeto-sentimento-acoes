# Análise visual

O [artigo](../notebooks/00_artigo.ipynb) concentra os cálculos finais, os sete gráficos interativos e suas interpretações.

| Perguntas | Unidade e amostra |
| --- | --- |
| 1–2 | 6.552 associações manchete–empresa |
| 3 | 2.569 pares empresa/data civil; extremos gerais e extremos com três ou mais manchetes |
| 4–6 | 2.387 pares empresa/pregão com notícias e janela completa |
| 7 | Principal: 2.387; mínimo de três: 783; sem retrospectivas identificadas pela regra: 2.271; combinado: 697 |

Spearman é a correlação dos postos médios; grupos constantes ou insuficientes ficam sem coeficiente. O ano é o do pregão de resposta. As escalas são comuns e os retornos extremos são preservados. Ausência no corpus permanece sem sentimento. A Q5 compara o módulo do escore médio com a média dos módulos individuais nos mesmos pregões. A segunda medida preserva a intensidade de títulos com sinais opostos.

## Robustez

O [protocolo textual](retrospectivas/README.md) fixa a regra e identifica as marcações como automáticas. Nos cenários de exclusão, as probabilidades são reagregadas por empresa/pregão antes de recalcular classe, escore, intensidade e contagem. Só depois se aplica o mínimo de três. O filtro ampliado de sinais não conclusivos é uma sensibilidade adicional, com 2.243 ou 670 pares.

A amostra sem retrospectivas identificadas pela regra não apresenta uma relação uniforme entre empresas. Alguns sinais mudam após restringir quantidade, com grupos menores e retenção desigual. Essa sensibilidade não demonstra significância, causalidade ou desempenho preditivo. A regra pode deixar passar relatos explícitos de preço já observado; sua falta de validação humana independente limita a resposta à Q7.

## Saídas

A última célula do artigo exporta as tabelas em [analise_final/](analise_final/), incluindo os seis cenários, retenção por empresa/ano, distribuições por classe e os textos dos extremos com suporte. A marcação dos 6.019 textos está em `docs/retrospectivas/marcacao_textos.csv`. As tabelas históricas em [analise_visual/](analise_visual/) servem de referência ao verificador.

O exportador `tools/exportar_artigo.py` gera o HTML com as sete figuras interativas e suas bibliotecas embutidas para uso offline. A formatação das fórmulas no HTML pode exigir internet. O notebook conserva a especificação de cada gráfico. A narrativa deve ser conferida se as entradas mudarem.

Referências técnicas: [agregações pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html), [postos](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html) e [interações Altair](https://altair-viz.github.io/user_guide/interactions/parameters.html).
