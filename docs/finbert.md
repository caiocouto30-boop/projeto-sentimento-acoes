# FinBERT: classificação e revisão humana

O [notebook de preparação](../notebooks/01_preparacao_dados.ipynb) classifica **6.552 associações**, correspondentes a **6.019 textos distintos**, com `ProsusAI/finbert`, sem treinamento adicional. Modelo e tokenizador usam a revisão fixa `4556d13015211d73dccd3fdd39d39232506f3e43`. O limite é 512 tokens, com truncamento registrado; a execução usa CPU e probabilidades em `float32`.

## Cache e medidas

O projeto inclui [probabilidades por texto](../data/raw/finbert_probabilidades.csv) e sua [configuração](../data/raw/finbert_configuracao.json). O notebook confere configuração, identificação dos textos e validade das probabilidades antes de reutilizá-las; classifica apenas textos faltantes. A primeira execução pode baixar o tokenizador, caso não esteja disponível localmente. Os pesos do modelo só são carregados se houver textos pendentes. Não é necessário refazer a inferência para ler ou executar o [artigo](../notebooks/00_artigo.ipynb).

O escore é `P(positivo) − P(negativo)`; a classe corresponde à maior probabilidade, com empates explícitos. Na agregação, usamos médias das probabilidades com peso igual por manchete; a classe agregada é a de maior média. Uma data sem notícias não recebe classe neutra. A [integração](integracao.md) faz a agregação definitiva por empresa/pregão, em vez de tomar uma média simples de médias de dias com quantidades diferentes de manchetes.

## Revisão humana preservada

A [amostra preenchida](revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) contém **50 rótulos válidos**, observações e identificação do revisor `caio`: **39 concordâncias e 11 divergências**, ou 78% nesta amostra. A seleção foi dirigida: 30 casos de cobertura empresa/classe, 10 de baixa margem, 5 de manchetes compartilhadas e 5 de complementação aleatória.

Essa proporção **não estima a acurácia geral**. Houve um revisor, e o arquivo apresenta as previsões automáticas. Além disso, o tom da manchete inteira pode diferir do tom relativo à empresa associada: um título pode favorecer Nvidia e expressar cautela sobre AMD ou Intel. As divergências são um diagnóstico qualitativo, não erros comprovados automaticamente.

Os rótulos humanos não substituem as classes automáticas. O notebook lê e verifica o arquivo existente sem sobrescrevê-lo. Para ampliar a revisão, preserve IDs, textos e campos automáticos; edite apenas `rotulo_humano`, `observacao` e `revisor`. Os rótulos aceitos são `positivo`, `negativo`, `neutro` e `ambiguo`.

A [marcação de retrospectivas](retrospectivas/README.md) é outra tarefa: usa uma regra textual automática para a pergunta 7 e não foi validada pela revisão de sentimento dessas 50 manchetes.
