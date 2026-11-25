# Roteiro da apresentação de dez minutos

Use os [oito slides em PDF](apresentacao.pdf). Para a demonstração do slide 4, deixe o artigo HTML aberto na Q3, selecione BAC e localize 4 de dezembro de 2018 antes de começar. O mesmo exemplo está reproduzido no slide para uso sem alternar de janela. Os tempos incluem as trocas de fala e a demonstração.

| Intervalo | Slide | Quem apresenta | Foco |
| --- | --- | --- | --- |
| 0:00–0:45 | 1 | Caio | Pergunta e resultado principal |
| 0:45–2:30 | 2 | Caio | Da manchete ao pregão |
| 2:30–3:45 | 3 | Alice | Cobertura e composição |
| 3:45–5:10 | 4 | Alice | Demonstração de um extremo |
| 5:10–6:20 | 5 | Mateus | Classe, retorno e diferenças entre empresas |
| 6:20–7:40 | 6 | Mateus | Quantidade e duas medidas de intensidade |
| 7:40–9:05 | 7 | Mateus | O que muda com os filtros |
| 9:05–10:00 | 8 | Caio | Respostas a H1, H2 e H3 e próximo passo |

## Slide 1 · Pergunta

“Se alguém vê uma manchete positiva sobre uma empresa, o que pode dizer sobre o retorno da ação no pregão seguinte? Investigamos essa pergunta com cinco empresas dos EUA entre 2017 e 2019. Encontramos uma diferença clara na quantidade de cobertura. Já na comparação com preços, os retornos de pregões com notícias positivas, neutras ou negativas se sobrepõem. Para entender o resultado, primeiro precisamos explicar o que conta como uma observação.”

## Slide 2 · Da manchete ao pregão

Mostre o exemplo da Netflix da esquerda para a direita. Em 5 de janeiro de 2017, uma manchete anunciou a série *Love Alarm*. O FinBERT atribui probabilidades às classes positiva, negativa e neutra. O escore é a probabilidade positiva menos a negativa. Por isso a classe mais provável dessa manchete pode ser neutra mesmo quando o escore é ligeiramente positivo.

Associe o título ao primeiro pregão **estritamente posterior** à data civil, 6 de janeiro. Duas manchetes entraram nessa janela. A média dos dois escores foi +0,334. Para definir a classe do grupo, calculamos a média das probabilidades de cada classe e escolhemos a maior. O grupo ficou positivo. Os fechamentos ajustados passaram de aproximadamente 13,181 para 13,107, um retorno de −0,561%.

Aponte onde as duas fontes se encontram. Extraímos as manchetes da base de Miguel Aenlle no Kaggle e usamos os fechamentos do Yahoo Finance. A unidade da comparação é um par empresa/pregão. Repetir o mesmo retorno em cada manchete daria mais peso aos dias de muita cobertura. A análise principal reuniu 2.387 pares com pelo menos uma notícia e janela completa. Passe a palavra à Alice para mostrar de onde vêm as diferenças de cobertura.

## Slide 3 · Cobertura e composição

Leia os dois extremos do gráfico. A Netflix teve 2.344 associações e a Coca-Cola, 644. A Netflix liderou nos três anos. Uma manchete que menciona duas empresas pode estar associada às duas, por isso as 6.552 associações correspondem a 6.019 textos distintos. É nesse sentido que H1, sobre cobertura desigual, recebe apoio.

Em seguida, explique a troca de denominador. Para comparar o tom entre empresas, calculamos o percentual sobre as manchetes de cada empresa. A classe neutra foi a mais frequente nas cinco. Ela alcançou 61,8% na Coca-Cola e 48,6% na NVIDIA. Uma classe pode ser a mais frequente mesmo representando menos da metade das observações.

## Slide 4 · Ler uma manchete no gráfico

Abra a Q3 e passe o mouse sobre o ponto preparado do Bank of America. Mostre a empresa, a **data civil**, a contagem de três notícias e os títulos. Leia ou traduza a manchete reproduzida no slide. Ela relata receio de recessão e queda das ações de bancos. Discuta o que isso muda na interpretação de um escore de −0,950. O texto fala do setor e já descreve preços em queda. A data sozinha não revela o que o mercado sabia no momento da publicação.

Explique por que olhamos o número de títulos em cada ponto. Sem exigir cobertura mínima, os dez extremos, um mínimo e um máximo por empresa, vieram todos de datas com apenas uma manchete. Com três ou mais, este continuou sendo um dia bastante negativo para o Bank of America. Para dias com mais de três títulos, o balão informa quantos ficaram além dos exemplos exibidos. Volte aos slides e passe a palavra ao Mateus.

## Slide 5 · Classe e retorno

Compare as duas linhas. Na Netflix, a mediana dos pregões de classe negativa foi −0,498% e a dos positivos ficou próxima de zero. Na NVIDIA, a mediana dos negativos foi positiva e a dos positivos foi negativa. A ordem muda e há sobreposição nas distribuições completas do artigo. Uma classe positiva, por si só, diz pouco sobre o retorno de um pregão específico.

A Q6 trata o escore como uma variável contínua. A correlação de Spearman compara as posições das observações nas duas variáveis. Se escores maiores acompanhassem consistentemente retornos maiores, esperaríamos um coeficiente positivo mais alto. No período completo, os valores por empresa ficaram entre −0,041 e +0,058. Nos recortes anuais vão de −0,153 a +0,123. A comparação é descritiva.

## Slide 6 · Duas medidas de intensidade

Agora a pergunta muda da direção do retorno para o **tamanho da oscilação**. Uma queda de 2% e uma alta de 2% têm o mesmo retorno absoluto. Use o exemplo de +0,8 e −0,8 para mostrar por que medimos intensidade de duas formas. Se tirarmos a média e depois o módulo, os sinais se cancelam. Se tirarmos o módulo de cada escore antes da média, ambos contam para a intensidade.

Leia a linha da Coca-Cola. A correlação entre quantidade e oscilação chega a +0,161. Para as duas intensidades, é +0,055 e +0,080. Nas cinco empresas, todos os coeficientes das duas colunas de intensidade têm módulo inferior a 0,081. Repetir a comparação nos mesmos pregões permite atribuir a diferença numérica à definição da medida. Os resultados oferecem pouco apoio a H2 nesse recorte.

## Slide 7 · Efeito dos filtros

Mostre primeiro a diferença entre as barras. Das 2.387 observações, restam 783 quando exigimos três títulos. Ao excluir apenas as retrospectivas identificadas pela regra, restam 2.271. Um pregão com duas notícias ainda pode ficar com uma depois da exclusão. Por isso a equipe recalculou o sentimento com os textos retidos e só depois aplicou o mínimo. Os dois filtros juntos conservaram 697 pares.

Para dar escala à mudança, volte à Coca-Cola. A correlação entre escore e retorno passa de +0,002 para −0,235, mas o segundo valor vem de apenas 55 pregões, contra 334 na amostra principal. O filtro muda quais dias comparamos. A regra textual também pode deixar passar manchetes retrospectivas. Esses dois limites importam antes de interpretar a mudança de sinal.

## Slide 8 · Conclusão

Retome as três hipóteses. H1 recebe apoio descritivo porque a cobertura varia bastante por empresa. H2 fica sem apoio uniforme nas duas medidas de intensidade. Em H3 observamos variação entre empresas e anos, mas o desenho do estudo não permite atribuí-la a diferenças estruturais. Os resultados se limitam a cinco empresas, uma fonte de manchetes e três anos.

“Se pudéssemos melhorar uma parte da coleta, começaríamos pelo horário de publicação e pela revisão dos títulos que já descrevem movimentos de preço. Assim seria possível distinguir melhor uma notícia que antecede um movimento de outra que apenas o relata.”
