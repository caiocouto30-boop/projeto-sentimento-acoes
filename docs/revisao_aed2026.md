# Revisão conforme o enunciado AED2026

Revisão de 16/10/2026, a partir do repositório no commit `d45c4ffabadf50c3806127c8a5f55d01b2403bbb`. Base documental: `AED20262_projeto.pdf`, especialmente páginas 1–2; proposta do grupo; cronograma interno. Os dois últimos orientam o recorte e a execução, sem acrescentar exigências do professor.

## Parecer

O projeto está alinhado ao objetivo da disciplina: exploração de dados, medidas descritivas, visualizações e narrativa. O uso de um modelo pronto como ferramenta de preparação não deslocou o foco para treinamento. As primeiras seis perguntas têm respostas iniciais coerentes com os dados; a sétima permanece parcial. **A estrutura da intermediária está atendida, mas isso não equivale à entrega completa ou à aprovação do professor. A versão final ainda exige trabalho.**

## Correspondência com o enunciado

| Exigência | Evidência atual | Situação |
| --- | --- | --- |
| Equipe de três integrantes | Autoria no artigo e README | Identificada; participação equilibrada precisa ser demonstrada pelo grupo |
| Dados públicos com atributos e dimensão temporal | Kaggle + Yahoo Finance, cinco empresas em três anos | Atendida |
| Proposta de uma página, problema, dados e 5–8 perguntas | Proposta original com sete perguntas | Conteúdo conferido; envio e retorno não verificados |
| Notebook em forma de artigo com link do repositório | `notebooks/00_artigo.ipynb` | Atendida |
| Título, introdução, contexto, motivação e síntese | Abertura e seção 1 | Atendida |
| Descrição e abstração dos dados | Seções 2–3: manchete, associação, data civil e pregão | Atendida |
| Transformações, gráficos e interpretação por pergunta | Seções 4–10, com código pandas e Altair | Atendida para Q1–Q6; Q7 explicitamente parcial |
| Conclusão, recomendações e limitações | Seção 11 | Atendida como conclusão provisória |
| Intermediária em 29/10 e apresentação de cinco minutos | Artigo preparado para leitura | Apresentação não localizada |
| Final: notebook com retorno incorporado e repositório documentado | Código e instruções presentes | Depende de concluir análises e incorporar comentários recebidos |
| Final: apresentação de dez minutos e declaração de contribuições | Não localizadas | Pendentes |

O enunciado permite um artigo ainda incompleto na intermediária e não exige PDF, ABNT, treinamento de modelo, testes de significância ou análise causal. A revisão não adiciona essas obrigações. Para a final, o enunciado informa **Semana A2**; datas internas não substituem a confirmação da disciplina.

## Correção metodológica

Foram conferidos o recorte, as exclusões, a chave empresa/data/manchete, a preservação de textos compartilhados e a revisão humana. A classificação usa probabilidades e revisão de modelo fixadas; concordância em 50 casos dirigidos não é apresentada como acurácia geral.

As notícias apontam ao primeiro pregão estritamente posterior. Os retornos são calculados no fechamento ajustado com margem, e a agregação por empresa/pregão evita contar o mesmo retorno uma vez por manchete. Ausência de notícia permanece sem classe ou escore. Janelas incompletas são sinalizadas; as comparações usam 2.387 pares elegíveis. Retorno absoluto é tratado como magnitude diária, sem confundi-lo com volatilidade formal.

Mapas de cobertura, proporções, séries, boxplots e dispersões correspondem às perguntas. As escalas, denominadores, extremos e tamanhos dos grupos são explícitos. As correlações pequenas e mudanças de sinal não são interpretadas como significância, capacidade preditiva ou causalidade.

## Alterações necessárias

- Encurtadas as células de texto, mantendo decisões, transformações e limites junto ao código.
- Corrigidas mensagens que ainda descreviam análises já realizadas como pendentes.
- Concentradas visualizações e tabelas no artigo. Retirado o notebook 04, que duplicava essa análise; os cálculos exclusivos de exportação e os resumos por classe foram incorporados ao artigo.
- Retirados resumos antigos sem uso e relatos editoriais sobrepostos; mantidos os registros datados e a revisão humana.
- Removido o gráfico de cobertura duplicado da preparação; a etapa continua exportando contagens para auditoria, e a pergunta 1 apresenta o gráfico.
- Simplificados README e regras de exclusão do Git; retiradas as dependências de Matplotlib e Seaborn, que deixaram de ser usadas.
- Atualizado o exportador para produzir HTML offline e imagens dos gráficos atuais.
- Corrigido o formato de saída dos gráficos no Jupyter: o renderizador anterior produzia uma chave MIME incompatível com a validação do notebook; agora HTML e especificação JSON válida são salvos juntos.
- Corrigido um caso limite na seleção da revisão: uma quantidade solicitada igual a zero não pode adicionar uma manchete.

O processamento que protege originais, confere probabilidades, valida calendário e preserva anotações foi mantido. A versão anterior permanece no histórico Git; uma cópia integral foi preservada durante a revisão.

## Pendências reais

1. Concluir a pergunta 7: definir e revisar retrospectivas, reagrupar após exclusão e comparar filtros separados e combinados. Isso é um compromisso da proposta do grupo, não uma exigência genérica adicional do enunciado.
2. Conferir vínculos indiretos de ticker e extremos apoiados em poucas manchetes; aprofundar a leitura por empresa/ano.
3. Outro integrante reproduzir e revisar o trabalho. A execução automatizada não comprova participação equilibrada ou compreensão do trio.
4. Preparar as apresentações, incorporar o retorno do professor e redigir a declaração com contribuições efetivamente realizadas.

## Validação desta revisão

Os quatro notebooks foram executados em processos IPython independentes, somando **39 células sem erros**. A preparação partiu do CSV bruto e do snapshot local; o notebook 02 carregou o modelo e reutilizou o cache completo de 6.019 textos. Não houve nova coleta de preços nem nova inferência do corpus.

Foram aprovadas **142 verificações**, incluindo igualdade das oito bases de processamento com a referência, reprodução dessas bases, conservação das anotações humanas, chaves, fórmulas, mapeamento e equivalência numérica das onze tabelas. Os sete gráficos foram renderizados e inspecionados visualmente. O HTML foi exportado com bibliotecas incorporadas; os controles não foram retestados no navegador nesta revisão, pois o navegador conectado não conseguiu acessar o servidor local.

O texto Markdown dos notebooks passou de 13.068 para 4.305 palavras; o README, de 1.317 para 485. A redução concentra-se em repetições e explicações operacionais extensas. Os registros detalhados estão em [verificação](verificacao_revisao.json). A conclusão acadêmica permanece provisória até as pendências serem tratadas.
