# Adequação ao formato de artigo

Revisão editorial de 15/10/2026, baseada no enunciado `AED20262_projeto.pdf`, páginas 1–2, na proposta de uma página e no planejamento interno de 06/10/2026. Os documentos foram fornecidos no projeto; seus originais foram preservados e não foram adicionados ao repositório.

## O que o professor solicita

O Marco 2 pede um **notebook Jupyter em forma de artigo, ainda que incompleto**, com link do repositório. A narrativa deve incluir título informativo; introdução com problema, contexto, motivação e síntese dos achados; descrição dos dados; uma seção por pergunta; e conclusão com síntese, recomendações e limitações. Para as perguntas, o enunciado orienta apresentar transformações, visualizações e análise que responda à questão. A entrega também envolve uma apresentação de cinco minutos.

O enunciado não exige PDF nem um estilo específico como ABNT ou template de periódico. O artefato principal desta revisão é o [notebook-artigo](../notebooks/00_artigo.ipynb). A separação entre artigo e notebooks de apoio é uma decisão de organização: mantém a narrativa legível e o código detalhado acessível.

## Correspondência na revisão editorial de 15/10/2026

| Exigência | Local | Situação |
| --- | --- | --- |
| Título informativo e repositório | Abertura do artigo | Incluídos, com autores e identificação acadêmica |
| Introdução, contexto, motivação e síntese | Resumo e seção 1 | Redigidos apenas com o que já foi realizado |
| Dados e abstração correta | Seção 2 | Fontes, período, atributos e distinção entre associação, texto, data civil e pregão |
| Transformações, limpezas e derivações | Seção 3 e notebooks 01–03 | Método consolidado; código e saídas originais preservados |
| Uma seção por pergunta | Seções 4–10 | Sete perguntas da proposta, com estado de execução explícito |
| Visualização e análise da cobertura | Seção 4 | Figura existente, tabela anual, leitura e limites |
| Visualizações e respostas das demais perguntas | Seções 5–10 | Ainda incompletas; a revisão editorial não as executou |
| Conclusão com síntese, recomendações e limites | Seção 11 | Conclusão provisória restrita à cobertura e à preparação |
| Referências e reprodução | Seção 12, referências e README | Fontes, registros datados e dois níveis de reprodução explicitados |
| Apresentação de cinco minutos | Fora do escopo desta revisão | Não criada ou verificada |
| Entrega final e contribuições | Marco 3 | Continuam futuras; nenhuma contribuição foi atribuída sem evidência |

Ter a estrutura organizada não significa que toda a entrega intermediária ou final esteja concluída. O próprio enunciado admite um artigo ainda incompleto; as lacunas analíticas estão identificadas, sem resultados simulados ou conclusões presumidas.

## Mudanças realizadas e limites

- Criado `00_artigo.ipynb` como ponto de entrada, com texto acadêmico contínuo e resultados salvos.
- Consolidada a narrativa antes espalhada pelos notebooks, removendo do notebook 01 as seções duplicadas de perguntas e conclusão e apontando para o artigo.
- Corrigidos trechos que ainda descreviam integração e retornos como pendentes; preservados os registros históricos de execução.
- Mantidas todas as células computacionais, saídas e explicações da preparação, assim como a revisão humana e a figura original.
- Publicadas em `resultados_registrados.json` as duas pequenas tabelas já exibidas nas saídas, com commit, célula e hash de origem. Nenhuma nova inferência ou comparação estatística foi executada.
- Acrescentadas a `requirements.txt` três dependências já utilizadas no notebook 01: yfinance, matplotlib e seaborn, nas versões registradas no ambiente existente.

O cronograma interno sugere primeiras respostas às perguntas 1–6 e uma comparação da 7 antes de 29/10. Essa meta de planejamento não é uma exigência adicional atribuível ao professor. Da mesma forma, a janela 23–30/11 foi informada pelo grupo, enquanto o enunciado especifica apenas Semana A2.

## Verificações desta revisão

O artigo foi validado como notebook e suas quatro células de leitura foram executadas em ordem, sem erros, usando somente arquivos versionados. Foram conferidos os totais, a correspondência dos resumos com as saídas de origem, os links locais e a preservação das células computacionais dos três notebooks de apoio. A leitura renderizada foi revisada para conferir tabelas, fórmulas, títulos e figura.

As etapas de limpeza, inferência e integração não foram executadas novamente nesta revisão. A validação editorial não substitui a reprodução integral por outro integrante a partir dos dados e snapshots necessários.


## Atualização de 16/10/2026 — etapa visual de 20–23/10

As seções 4–9 do artigo agora apresentam primeiras respostas às perguntas 1–6, com gráficos, transformações e limitações. A seção 10 apresenta a comparação inicial da pergunta 7; retrospectivas e filtros combinados seguem pendentes. Resumo, introdução, conclusões e instruções de reprodução foram atualizados. O notebook 04 contém o processamento em 12 células executadas, com resultados e explicações das transformações.

Esta atualização não cria a apresentação nem declara concluída a entrega acadêmica. A tabela anterior documenta o estado da revisão de 15/10, não o estado atual das análises.
