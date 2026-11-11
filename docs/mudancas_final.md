# Revisão da entrega final

Versão preparada em 11/11/2026 a partir do repositório `caiocouto30-boop/projeto-sentimento-acoes`, referência `620f468968c957cdb3336b14d7dd4a08770f1764`.

## Correspondência com o enunciado

| Exigência ou critério | Implementação final |
| --- | --- |
| Notebook em formato de artigo | Título, resumo, motivação, dados, método, sete perguntas, conclusão, limitações e referências |
| Transformação, visualização e resposta por pergunta | Cada seção descreve sua unidade, transformação, gráfico, interpretação e limite |
| Retorno do professor | Hover com manchetes e tema; clique com lista completa, datas, fonte e URL; consulta por busca |
| Repositório com código e documentação | Módulos de análise e renderização, snapshots, probabilidades, verificações, dicionários e instruções |
| Apresentação de dez minutos | Dez slides editáveis, cinco gráficos nativos, notas e roteiro de 600 segundos |
| Declaração de contribuições | Documento editável, mantido sem atribuições presumidas por escolha do usuário |
| Design e acessibilidade | Escalas comuns, unidades, cores consistentes, formas nos cenários, rótulos, tabelas e consulta sem depender do hover |

## Alterações metodológicas e editoriais

1. Preservadas as hipóteses originais: H1 sobre cobertura, H2 sobre intensidade e retorno absoluto, H3 sobre diferenças entre empresas e anos. A conclusão distingue apoio descritivo de confirmação inferencial.
2. Mantido o alinhamento ao primeiro pregão estritamente posterior e um retorno por empresa/pregão. Sem notícias permanece sem sentimento.
3. Mantido o cálculo original `abs(mean(s))`, renomeado polarização líquida. Acrescentada `mean(abs(s))` como sensibilidade de intensidade, evitando cancelamento entre tons opostos. A definição original não foi apagada ou apresentada como equivalente à nova.
4. Recalculada a intensidade média dentro das notícias retidas em cada cenário, após exclusão e antes da restrição de quantidade.
5. Preservadas a regra automática de retrospectivas e suas limitações. Não houve nova validação humana independente, e o filtro não é apresentado como remoção de toda retrospectiva.
6. Temas lexicais não usam sentimento, retorno ou conteúdo completo de matérias. São sugestões para orientar a leitura das manchetes, sem alegação de resumo ou validação humana.
7. A implementação gráfica final usa Plotly.js e uma base compartilhada no HTML, com fórmulas legíveis sem serviço externo. A consulta completa evita limitar um agregado a uma manchete ilustrativa.

## Verificação e limites da finalização

A análise refaz a limpeza a partir de 6.556 registros, confere probabilidades de 6.019 textos, os vínculos das 6.552 associações, retornos calculados dos preços e as 2.387 janelas principais. Os cenários reproduzem 2.387, 783, 2.271, 697, 2.243 e 670 pares. Os coeficientes anteriores são comparados às saídas preservadas, e Spearman recebe uma conferência independente dos postos.

As células do notebook final são executadas em ordem em um processo Python, sem servidor Jupyter. A revisão também verifica a renderização local e os controles do HTML. A preparação anterior do modelo não foi refeita e não houve envio à disciplina, ensaio cronometrado nem declaração de que outro integrante reproduziu a análise.
