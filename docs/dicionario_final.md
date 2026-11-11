# Medidas acrescentadas na versão final

As variáveis originais conservam as definições dos dicionários de dados e integração. O arquivo original `base_integrada_pregoes.csv` permanece preservado.

| Variável | Unidade | Definição |
| --- | --- | --- |
| `polarizacao_liquida` | Empresa/pregão | Módulo da média dos escores individuais. É o cálculo chamado `intensidade_sentimento` na base original, em [0, 1]. |
| `intensidade_media` | Empresa/pregão | Média dos módulos dos escores individuais, em [0, 1]. Evita cancelamento entre sinais opostos. |
| `assunto` | Associação manchete–empresa | Tema sugerido por regras lexicais, usando somente a manchete. Não é classificação humana ou resumo do artigo completo. |
| `key` | Empresa/data civil ou empresa/pregão | Chave de consulta para recuperar as manchetes efetivamente associadas ao ponto do gráfico. |

Os escores individuais são `P(positivo) − P(negativo)`. Pela desigualdade triangular, a intensidade média é maior ou igual à polarização líquida. Isso também é conferido na verificação.

Os temas usam uma ordem explícita de regras: resultados e projeções, avaliação de analistas, regulação e processos, dividendos e capital, negócios e acordos, produtos e serviços, cotação e negociação. Sem correspondência, o tema é genérico. Títulos mistos podem receber apenas o primeiro tema reconhecido. As regras estão em `assunto()` de `tools/analise_final.py` e não usam retornos ou probabilidades de sentimento.
