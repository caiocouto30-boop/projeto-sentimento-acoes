# FinBERT: classificação e revisão inicial

Relatório de apoio à seção 3.2 do [artigo principal](../notebooks/00_artigo.ipynb). A narrativa acadêmica e o estado das sete perguntas estão centralizados no artigo.

A etapa computacional está concluída: foram classificadas **6.552 associações entre manchetes e empresas**, correspondentes a **6.019 textos distintos**, e gerado o sentimento de **2.569 pares empresa/data da notícia**. A revisão inicial de 50 manchetes também está preenchida e registrada. Esta etapa usa o modelo pronto `ProsusAI/finbert`, sem treinamento adicional.

## Reproduzir em um clone novo

1. Instale as dependências de `requirements.txt` no ambiente Python escolhido e selecione esse ambiente como kernel do Jupyter. Disponibilize os dados de origem conforme as instruções do projeto.
2. Execute `notebooks/01_preparacao_inicial.ipynb` em ordem para gerar `data/processed/noticias_limpas.csv`.
3. Execute `notebooks/02_sentimento_finbert.ipynb` em ordem. O download do modelo é permitido por padrão; a primeira execução precisa de internet para obter os pesos e o tokenizador. Ambos usam a revisão fixa `4556d13015211d73dccd3fdd39d39232506f3e43`. Depois do download, é possível usar somente o cache local. O notebook pode executar em CPU.
4. O notebook salva as probabilidades em `data/cache/`, com identificação do texto e da configuração utilizada, e reutiliza resultados compatíveis. Esse cache é local. Os CSVs grandes de entrada e resultados não são versionados; são gerados pelas etapas anteriores e pelo próprio notebook.

As saídas principais são `noticias_com_sentimento.csv`, com probabilidades, classe e escore por associação original, e `sentimento_diario_noticias.csv`, com as médias por empresa e data civil da notícia. O escore é `P(positivo) − P(negativo)`; a classe diária usa a maior probabilidade média, com empates explícitos. Dias sem notícias não recebem classe neutra.

## Revisão humana registrada

A [amostra preenchida](revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) contém **50 rótulos válidos, 50 observações e identificação do revisor `caio` em todos os casos**. Os IDs, manchetes e campos automáticos foram conferidos contra a amostra original e permaneceram intactos. Não há casos marcados como `ambiguo`.

Foram observadas **39 concordâncias e 11 divergências**, ou **78% de concordância nesta amostra**. A seleção foi dirigida: 30 casos para cobertura de empresa/classe, 10 de baixa margem, 5 de manchetes compartilhadas e 5 de complementação aleatória. Essa proporção não estima a acurácia geral do FinBERT na base. Trata-se de um diagnóstico com um revisor, em arquivo que também apresenta as previsões do modelo.

Na matriz abaixo, as **linhas representam o rótulo humano** e as **colunas representam a classe do modelo**:

| Humano / Modelo | Positivo | Negativo | Neutro |
|---|---:|---:|---:|
| Positivo | 11 | 0 | 3 |
| Negativo | 0 | 8 | 0 |
| Neutro | 2 | 6 | 20 |

Exemplos reais de divergências:

| `source_id` | Manchete | Modelo | Humano |
|---|---|---|---|
| 134474 | Benzinga's Top Upgrades, Downgrades For August 29, 2019 | Negativo | Neutro |
| 930882 | Seeing Notable Block Trade In Nvidia; 1M Shares At $100.40 | Negativo | Neutro |
| 929628 | Oppenheimer Bullish On Nvidia, Cautious On AMD, Intel | Neutro | Positivo |

Os dois primeiros exemplos foram considerados informativos pelo revisor. O terceiro combina uma avaliação favorável à Nvidia com cautela sobre outras empresas; a observação humana destaca a Nvidia. Esse caso ilustra a diferença entre interpretar o tom da manchete inteira e interpretar o tom relativo a uma empresa específica. A mesma atenção vale para boletins que combinam notícias de várias empresas. As divergências devem ser discutidas com esse critério em vista, sem tratá-las automaticamente como erros comprovados do modelo.

As **classes automáticas foram preservadas**. Os rótulos humanos documentam o diagnóstico e não substituem automaticamente as previsões da base inteira. Não foi estabelecido um limiar de aprovação do modelo.

## Preservar as anotações

O CSV humano é versionado em `docs/revisao_manual/`. O leitor do notebook aceita arquivos UTF-8 separados por vírgula ou ponto e vírgula, inclusive após salvar no Excel. Para continuar a revisão, edite apenas `rotulo_humano`, `observacao` e `revisor`; preserve IDs, textos e demais campos. Uma nova execução mantém o arquivo existente e lê as anotações salvas. Rótulos aceitos: `positivo`, `negativo`, `neutro` e `ambiguo`.

## Próximos passos

A [integração com pregões e retornos](integracao.md) foi concluída pelo notebook 03, preservando as previsões e a revisão desta etapa. As visualizações e interpretações estão no [artigo](../notebooks/00_artigo.ipynb). A pergunta 7 já compara a exclusão de retrospectivas explícitas e os filtros combinados, segundo o [protocolo textual](retrospectivas/README.md). Essa marcação é separada da revisão humana de sentimento.
