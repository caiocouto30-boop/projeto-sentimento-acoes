# Medidas da versão final

As variáveis originais conservam as definições dos dicionários de dados e integração. Os três arquivos de entrada em `data/processed/` permanecem preservados.

| Variável | Unidade | Definição |
| --- | --- | --- |
| `intensidade_liquida` | Empresa/pregão | Módulo da média dos escores individuais; é o cálculo chamado `intensidade_sentimento` na base original. |
| `intensidade_media` | Empresa/pregão | Média dos módulos dos escores individuais; evita a compensação entre sinais opostos. |
| `manchete_1`, `manchete_2`, `manchete_3` | Empresa/data civil | Até três manchetes para o tooltip da Q3, ordenadas pelo módulo do escore individual. |
| `outras_manchetes` | Empresa/data civil | Quantidade de títulos além dos três apresentados no tooltip. |
| `retencao_pct` | Empresa/cenário | Percentual de pares retidos em relação à amostra principal da empresa. |
| `delta_rho` | Empresa/cenário/associação | Diferença descritiva entre o coeficiente do cenário e o coeficiente principal. |

O escore individual é `P(positivo) − P(negativo)`. Pela desigualdade triangular, a intensidade média é maior ou igual à intensidade líquida, com ambas em [0, 1]. Essa relação é conferida na execução. As medidas não esgotam o conceito de intensidade emocional de uma notícia.

A Q7 recalcula as intensidades a partir das manchetes efetivamente retidas em cada cenário. A diferença de coeficientes e a mudança de sinal não são testes de significância.
