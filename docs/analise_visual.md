# Análise visual

O [artigo](../notebooks/00_artigo.ipynb) é a fonte única dos cálculos finais e dos gráficos. A implementação estática anterior foi retirada do percurso ativo por duplicar a análise; permanece no histórico Git.

| Perguntas | Unidade e amostra |
| --- | --- |
| 1–2 | 6.552 associações manchete–empresa |
| 3 | 2.569 pares empresa/data civil; mínimo e máximo por empresa, com desempate pela primeira data |
| 4–6 | 2.387 pares empresa/pregão com notícias e janela completa |
| 7 | Amostra principal comparada ao subconjunto com três ou mais notícias: 783 pares |

Spearman é a correlação dos postos médios; grupos constantes ou insuficientes ficam sem coeficiente. O ano é o do pregão de resposta. Retornos extremos são preservados. As comparações são descritivas e não incluem testes de significância ou identificação causal.

A intensidade é o módulo do escore médio, permitindo compensação entre tons opostos. Não equivale à média das intensidades individuais. Dias sem notícias permanecem sem sentimento.

## Saídas

A última célula do artigo grava onze tabelas em `docs/analise_visual/` e os textos dos extremos em `data/processed/manchetes_extremos_analise.csv`. O exportador `tools/exportar_artigo.py` usa as especificações salvas para gerar o HTML offline e sete imagens em `figures/analise_visual/`. Também atualiza a imagem estática de cada gráfico no notebook.

A narrativa descreve a versão de referência e deve ser conferida quando as entradas mudarem. As manchetes no cursor são exemplos selecionados por maior módulo do escore individual, com desempate por identificador; não sintetizam sozinhas o grupo.

## Pendências analíticas

Concluir a definição operacional e a revisão de retrospectivas sem consultar o impacto nos retornos. Após excluir manchetes, reagrupar probabilidades, classe, escore e contagem por empresa/pregão; só então reaplicar o mínimo de três. Comparar os filtros separados e combinados e informar perdas por empresa/ano. Rever também vínculos indiretos de ticker e extremos com maior suporte.

Referências: [postos](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html), [boxplots](https://altair-viz.github.io/user_guide/marks/boxplot.html) e [exportação Altair](https://altair-viz.github.io/user_guide/saving_charts.html).
