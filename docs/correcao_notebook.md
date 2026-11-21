# Revisão final do notebook

O notebook é o documento principal do artigo. A revisão parte da estrutura da versão registrada no commit `620f468968c957cdb3336b14d7dd4a08770f1764`, recuperada da exportação HTML original fornecida pelo grupo.

Foram mantidas as sete perguntas, as etapas da Q3 e Q7 e a construção dos gráficos em Altair. As transformações pandas e medidas ficam visíveis nas próprias células. Os gráficos Q1 e Q2 conservam o código de construção original. O arquivo final tem 46 células, sendo 15 de código.

## Alterações

1. Q3: tooltip com empresa, data, escore médio, quantidade e até três manchetes, com indicação da quantidade adicional. Preservados o seletor de empresa, o zoom, a identificação de extremos e o tamanho pela contagem.
2. Q5: preservada a definição original `abs(mean(s))`, chamada intensidade líquida. Acrescentada `mean(abs(s))`, com tabela comparativa e seletor na mesma amostra.
3. Q7: a intensidade média é recalculada após as exclusões. Tabelas apresentam n principal, n retido, retenção, coeficientes e diferença em relação à referência. Os quatro painéis de associação usam duas colunas.
4. Texto e reprodução: conclusões revisadas, síntese de H1–H3 e exportação do notebook salvo por nbconvert.

## Verificações e limites

As 15 células foram executadas no IPython InteractiveShell com Altair instalado. Foram produzidas sete especificações Vega-Lite válidas. As tabelas Q5 e Q6 e os 120 coeficientes de robustez foram comparados com cálculos independentes. O notebook foi validado com nbformat.

A execução em processo separado de kernel Jupyter não terminou no ambiente restrito da revisão. A inspeção visual de hover, zoom e seletores continua como conferência do grupo no Jupyter ou no HTML. Mudanças de sinal e de coeficiente são descritivas; não foram realizados testes confirmatórios de diferenças.

Não houve novo treinamento do FinBERT, nova coleta de preços ou nova anotação humana. A validação humana independente das retrospectivas e dos vínculos de ticker permanece uma limitação.

## Revisão das manchetes em 21/11

Na Q3, o agrupamento usa a empresa e a data civil. Na Q4, Q5 e Q6, usa a empresa e o pregão ao qual a notícia foi associada. Os círculos da Q4 representam os retornos fora dos bigodes de 1,5 IQR. O verificador confere as manchetes de cada grupo com as bases originais. Na Q7, cada símbolo resume uma correlação.
