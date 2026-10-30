# Protocolo da marcação de retrospectivas

Esta é a definição operacional utilizada na pergunta 7 da entrega intermediária. O alvo é **relato explícito de cotação ou oscilação de preço já observada**, inclusive em outra ação citada no texto. A unidade de classificação é a manchete inteira, como no FinBERT; o resultado é devolvido às associações originais.

## Regra fixada

O arquivo [regra_fixada.json](regra_fixada.json) identifica a versão 1.0 e o hash de [retrospectivas.py](../../tools/retrospectivas.py). Os critérios foram construídos com manchetes, sem probabilidades ou retornos como entrada, e fixados antes do cálculo dos novos cenários. Isso não constitui pré-registro formal: os resultados da análise principal já eram conhecidos.

As regras reconhecem negociação descrita como observada (`shares are trading lower`), cotações em alta/baixa, verbos de movimento com referência explícita a ações, variação percentual vinculada a uma empresa, máximas/mínimas observadas e resumos intradiários de mercado. Não basta mencionar ações, metas de preço ou uma expectativa de alta. Agendas como `before market open` e `after market close` não descrevem, por si só, oscilações. Variações de vendas, lucros e preços de produtos também não bastam.

| Marcação | Significado | Cenários principais |
| --- | --- | --- |
| `retrospectiva_explicita` | Ao menos uma regra identifica movimento observado | Excluída nos cenários sem retrospectivas identificadas pela regra |
| `ambigua` | Há sinal lexical não conclusivo: pode ser previsão, operação da empresa, análise ou movimento não reconhecido pela regra | Mantida |
| `sem_indicio_explicito` | Nenhuma regra reconhece relato explícito | Mantida; não significa ausência comprovada de retrospectiva |

São 6.019 textos: 586 explícitos, 297 com sinais não conclusivos e 5.136 sem indício reconhecido. Eles correspondem a 621, 317 e 5.614 associações, respectivamente. A [marcação completa](marcacao_textos.csv) registra texto, hash, categoria, regra, trecho reconhecido e origem automática.

## Revisão e alcance

Os critérios e exemplos de fronteira foram revistos pelo assistente de IA. Foram inspecionados relatos explícitos, sinais não conclusivos e falsos positivos de agendas de resultados durante a definição. Isso não é revisão humana do trio nem validação independente do classificador. Não se presume que todos os textos tenham sido lidos individualmente. Os [casos de controle](casos_controle.csv) verificam situações determinísticas; não estimam precisão ou revocação.

A regra é conservadora e pode deixar retrospectivas implícitas e relatos explícitos não reconhecidos pelos padrões na base. Por isso, os cenários são descritos como “sem retrospectivas identificadas pela regra”; não se presume a eliminação de todas as retrospectivas. Notícias mistas, erros de redação e vínculos indiretos de ticker também podem produzir marcações incorretas. O filtro considera o texto inteiro; uma retrospectiva sobre outra empresa pode levar à exclusão de todas as associações daquele texto.

## Aplicação

Primeiro restringimos às mesmas janelas elegíveis de 2017–2019. Depois retiramos as manchetes marcadas, reagregamos as três probabilidades com peso igual por manchete e recalculamos classe, escore, intensidade e quantidade por empresa/pregão. Só então aplicamos o mínimo de três. Um pregão que perde todas as notícias deixa a comparação, sem receber neutralidade artificial. Os retornos permanecem os mesmos.

O gráfico apresenta quatro cenários. Duas variantes adicionais retiram também `ambigua`, para avaliar a sensibilidade ao alcance do filtro. Essa exclusão ampliada pode retirar notícias não retrospectivas e não constitui uma identificação mais correta por definição. Tamanhos e perdas por empresa/ano constam de `docs/analise_visual/q7_retencao_empresa_ano.csv`.

O código, a regra e a marcação são reproduzíveis. Uma validação humana independente e o aperfeiçoamento semântico ficam como aprofundamentos para a etapa final, com eventual nova versão das regras identificada separadamente.
