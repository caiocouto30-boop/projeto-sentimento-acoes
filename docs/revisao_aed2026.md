# Adequação da entrega intermediária ao AED2026

Versão preparada em 16/10/2026 para o Marco 2 de 29/10. Referências: enunciado `AED20262_projeto.pdf`, páginas 1–2, proposta de sete perguntas e planejamento interno do grupo.

## Parecer

O material escrito e computacional está preparado para a intermediária. O artigo reúne as sete perguntas com transformações, gráficos, interpretações e conclusões provisórias. A pergunta 7 agora compara filtros separados e combinados; sua resposta fica limitada à regra textual automática e conservadora implementada. Slides e ensaio estão fora desta tarefa, conforme solicitado pelo usuário.

| Requisito do Marco 2 | Evidência |
| --- | --- |
| Notebook Jupyter em forma de artigo e link do repositório | Abertura de `notebooks/00_artigo.ipynb` |
| Título, problema, contexto, motivação e síntese dos achados | Resumo e seção 1 |
| Dados definidos, atributos e unidades corretas | Seções 2–3; cinco empresas, 2017–2019, Kaggle e Yahoo |
| Hipóteses e progressão das perguntas | H1–H3 e seções 4–10 |
| Transformações, visualizações e análise por pergunta | Código pandas, sete gráficos Altair e interpretação junto a cada resultado |
| Conclusão com síntese, recomendações e limitações | Seção 11 |
| Código e documentação versionados | README, quatro notebooks, auxiliares, dicionários, regras e tabelas |
| Apresentação de cinco minutos | Continua sendo exigência da disciplina; excluída desta tarefa pelo usuário |

O enunciado permite um artigo ainda incompleto na intermediária. Esta versão responde às sete perguntas segundo as definições adotadas, sem afirmar validação final ou aprovação pelo professor. O grupo informou que ainda não recebeu comentários anteriores; não há feedback disponível para incorporar.

## Análises concluídas nesta preparação

- Quatro cenários principais da Q7, com 2.387, 783, 2.271 e 697 pares, respectivamente.
- Reagregação após excluir 621 associações com retrospectivas explícitas; limiar de três aplicado à nova contagem.
- Duas variantes adicionais para sinais textuais não conclusivos, com 2.243 e 670 pares.
- Retenção por empresa/ano, distribuição de classes e três coeficientes por empresa/cenário.
- Extremos diários com pelo menos três manchetes e inspeção de todos os textos desses dez grupos.
- Atualização do resumo, método, pergunta 7, conclusões, tabelas, figuras e HTML.

## Limites e etapa final

A marcação de retrospectivas é automática, com critérios revistos pelo assistente de IA, sem validação humana independente. Ela não identifica exaustivamente toda retrospectiva e pode errar. Quantidade de manchetes não garante relevância para o ticker. A revisão humana de sentimento original e os dados de preparação permanecem intactos.

Para a final: validar a marcação com o grupo, aprofundar vínculos de ticker e dependência temporal, incorporar comentários recebidos e preparar os itens orais e a declaração factual de contribuições. Essas atividades não foram simuladas como concluídas. A execução automatizada não comprova compreensão ou participação equilibrada do trio.

A [verificação da intermediária](verificacao_intermediaria.json) registra a execução e as conferências desta versão. O [guia de entrega](../ENTREGA_29_10.md) indica o material a encaminhar; não houve envio formal à disciplina.
