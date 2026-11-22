# Revisão final do notebook

O notebook é o documento principal do artigo. A revisão parte da estrutura da versão registrada no commit `620f468968c957cdb3336b14d7dd4a08770f1764`, recuperada da exportação HTML original fornecida pelo grupo.

Foram mantidas as sete perguntas, as etapas da Q3 e Q7 e a construção dos gráficos em Altair. As transformações pandas e medidas ficam visíveis nas próprias células. Os gráficos Q1 e Q2 conservam o código de construção original. O arquivo final tem 46 células, sendo 15 de código.

## Alterações

1. Q3: tooltip com empresa, data, escore médio, quantidade e até três manchetes, com indicação da quantidade adicional. Preservados o seletor de empresa, o zoom, a identificação de extremos e o tamanho pela contagem.
2. Q5: preservada a definição original `abs(mean(s))`, chamada intensidade líquida. Acrescentada `mean(abs(s))`, com tabela comparativa e seletor na mesma amostra.
3. Q7: a intensidade média é recalculada após as exclusões. Tabelas apresentam n principal, n retido, retenção, coeficientes e diferença em relação à referência. Os quatro painéis de associação usam duas colunas.
4. Texto e reprodução: conclusões revisadas, síntese de H1–H3 e exportação do notebook salvo por nbconvert.

## Verificações e limites

As saídas salvas no repositório foram produzidas em IPython. Em uma segunda execução, um kernel Jupyter novo executou as 15 células na pasta `notebooks/`. O verificador conferiu as tabelas Q5 e Q6 e os 120 coeficientes de robustez. O exportador gerou o HTML com as sete figuras. [Execução em Jupyter](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/actions/runs/44964338148).

No HTML distribuído, o teste em Chrome com a rede desligada moveu o ponteiro sobre os marcadores de Q3 a Q6 e comparou o texto visível do balão com o título do ponto. Na Q3, selecionar a Netflix e arrastar a faixa de datas reduziu o painel de 720 para 224 pontos. Na Q5, o teste alternou a medida de intensidade. Na Q6, clicar em NFLX em 2019 atualizou a dispersão para esse recorte. Na Q7, os quatro cenários apareceram nas marcas renderizadas. [Teste no navegador](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/actions/runs/44964401509/job/137030055149).

As diferenças de sinal e de coeficiente são descritivas. A análise não testa diferenças estruturais entre empresas ou anos.

Não houve novo treinamento do FinBERT, nova coleta de preços ou nova anotação humana. A validação humana independente das retrospectivas e dos vínculos de ticker permanece uma limitação.

## Revisão das manchetes em 21/11

Na Q3, o agrupamento usa a empresa e a data civil. Na Q4, Q5 e Q6, usa a empresa e o pregão ao qual a notícia foi associada. Os círculos da Q4 representam os retornos fora dos bigodes de 1,5 IQR. O verificador confere as manchetes de cada grupo com as bases originais. Na Q7, cada símbolo resume uma correlação.
