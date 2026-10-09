# Sentimento das notícias e comportamento de ações dos EUA

Análise exploratória da relação entre o sentimento de notícias financeiras e o comportamento de ações dos EUA (2017–2019).

Projeto de **Análise Exploratória de Dados e Visualização**, FGV EMAp, 2026.2.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

## Objetivo e recorte

Investigar como o tom das manchetes financeiras se relaciona com retornos e oscilações de NVIDIA (NVDA), Netflix (NFLX), Bank of America (BAC), Johnson & Johnson (JNJ) e Coca-Cola (KO), de 2017 a 2019. O foco está nas visualizações e na interpretação descritiva. Notícias podem acompanhar expectativas ou relatar movimentos já ocorridos; as comparações serão interpretadas como associações, sem atribuição de causalidade.

## Situação desta versão

Preparação local em 09/10/2026: documentação organizada, esqueleto do notebook criado e bibliotecas verificadas no ambiente `aed-sentimento`. **A limpeza, a classificação de sentimento e a integração das bases ainda não foram executadas.** O notebook contém somente verificações do ambiente e das pastas, com as análises futuras descritas em texto.

Esta cópia local ainda não foi enviada ao GitHub. Alterações remotas dependem de confirmação do usuário.

## Documentos de referência

- [Enunciado da disciplina](docs/AED20262_projeto.pdf): entregas, prazos e avaliação.
- [Proposta do grupo](docs/proposta_etapa1.pdf): integrantes, recorte, fontes, método e sete perguntas.
- [Cronograma atualizado](docs/cronograma_planejamento_atualizado.pdf): planejamento datado de 06/10/2026.

Os documentos foram copiados sem alterações. As contagens de **6.556 notícias e 754 pregões por empresa** aparecem na proposta como resultado de uma inspeção anterior; **não foram auditadas nesta preparação** e deverão ser conferidas na etapa de dados.

## Fontes dos dados

| Fonte | Conteúdo | Obtenção planejada |
| --- | --- | --- |
| [Kaggle: Daily Financial News for 6000+ Stocks](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests) | `raw_analyst_ratings.csv`, com manchete, URL, publisher, data e ticker | Download do arquivo original; manter em `data/raw/` quando começar a etapa de dados |
| [Yahoo Finance via yfinance](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html) | Fechamento ajustado e volume diários | Coleta reproduzível, com margem antes e depois do recorte e registro da data e dos parâmetros |

As bases permanecem locais e são ignoradas pelo Git conforme o `.gitignore` existente. Não incluir credenciais do Kaggle no repositório. Ao iniciar a coleta, registrar fonte, data, versão e resumo criptográfico dos arquivos para reprodução.

## Perguntas de domínio

1. Como a cobertura de notícias se distribui entre as cinco empresas e ao longo do período?
2. Quais empresas apresentam maiores proporções de manchetes positivas, neutras e negativas?
3. Como o sentimento agregado varia ao longo do tempo e quais períodos concentram extremos?
4. Como se distribuem os retornos do pregão seguinte a dias com sentimento positivo, neutro ou negativo?
5. Dias com mais notícias ou sentimento mais intenso são seguidos por maiores oscilações, medidas pelo retorno absoluto?
6. As associações entre sentimento e retorno apresentam direção e intensidade semelhantes entre empresas e anos?
7. Os padrões permanecem ao excluir manchetes que relatam oscilações já ocorridas e ao considerar apenas dias com pelo menos três notícias?

## Método planejado

1. **Inspeção e limpeza, em etapa futura:** conferir colunas, datas, ausências e duplicatas; filtrar o recorte e registrar motivos e contagens das exclusões, preservando os originais. Manchetes compartilhadas entre empresas exigem tratamento documentado.
2. **Sentimento:** aplicar o modelo pronto [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert), sem treinamento. Guardar probabilidades de positivo, neutro e negativo, classe e escore `P(positivo) - P(negativo)`. Revisar aproximadamente 50 exemplos distribuídos por empresas e classes, sem tratar essa revisão como medida formal de precisão.
3. **Agregação:** obter média do escore e contagem por empresa/data. Definir previamente a regra de classe diária e o tratamento de empates. Dias sem notícias permanecem sem notícia; não representam sentimento neutro.
4. **Cotações:** preservar fechamento ajustado e volume; explicitar parâmetros como `auto_adjust=False` para manter a coluna `Adj Close`. Conferir a estrutura das colunas retornadas e eventuais falhas de coleta antes de usar os dados.
5. **Alinhamento:** usar o primeiro pregão **estritamente posterior** à data registrada da notícia, com o calendário observado e conferência de possíveis lacunas. Preservar a data original e a data do pregão associado. Não converter datas para UTC de modo a mudar inadvertidamente o dia registrado.
6. **Retornos:** `100 × (fechamento ajustado / fechamento ajustado do pregão anterior - 1)`; retorno absoluto é o valor absoluto dessa variação percentual. Não preencher lacunas de preços automaticamente.
7. **Unidade de análise:** diferentes datas de notícias podem apontar para o mesmo pregão. Definir e documentar a agregação por empresa/pregão antes das comparações, evitando tratar o mesmo retorno repetido como observações independentes.
8. **Visualização e robustez:** seguir as sete perguntas, informar período, unidades e amostras; comparar os filtros da pergunta 7 sem selecionar exclusões conforme o resultado obtido.






