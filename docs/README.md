# Documentos e referências do projeto

## Artigo e leitura principal

- [Notebook-artigo](../notebooks/00_artigo.ipynb): narrativa principal, com dados, método, uma seção por pergunta, resultados disponíveis e conclusões provisórias.
- [Adequação ao enunciado](adequacao_artigo.md): exigências do professor, localização no artigo e pendências reais.
- [Resultados registrados](resultados_registrados.json): transcrição de duas tabelas já calculadas, com commit, células e hashes de origem. O artigo lê esse registro fixo; uma nova execução dos notebooks de apoio não o atualiza automaticamente.

Os notebooks 01–03 são material de apoio à reprodução do processamento. A revisão editorial de 15/10/2026 preservou suas células computacionais e resultados, centralizando a narrativa no artigo. Ela não avançou as análises de sentimento, retornos ou robustez.

## Documentos acadêmicos fornecidos ao grupo

O grupo utiliza três documentos acadêmicos que **não estão incluídos como PDFs neste repositório** nesta atualização. Os arquivos originais devem ser obtidos com os integrantes do grupo; não se deve interpretar estes resumos como substitutos dos documentos oficiais.

| Documento do grupo | Conteúdo |
| --- | --- |
| `AED20262_projeto.pdf` | Enunciado da disciplina: entregas, critérios de avaliação, formato de notebook-artigo e apresentações. |
| `proposta_etapa1.pdf` | Proposta do grupo: problema, cinco empresas, fontes, FinBERT e sete perguntas. **A existência do arquivo não demonstra, por si só, aprovação ou entrega formal.** |
| `cronograma_planejamento_atualizado.pdf` | Planejamento interno datado de 06/10/2026, com metas para limpeza, sentimento, integração, visualizações e apresentação. |

## Marcos de referência

- **01/10:** proposta de uma página (confirmar entrega e feedback).
- **29/10:** intermediária: notebook-artigo ainda que incompleto, repositório, hipóteses, visualizações, análises e apresentação de cinco minutos.
- **Semana A2:** entrega final com notebook, repositório, apresentação de dez minutos e declaração de contribuições. O intervalo 23–30/11 é a janela informada pelo grupo, não a confirmação do dia exato.

## Arquivos gerados localmente pelo notebook

Os arquivos `resumo_limpeza_noticias.csv`, `cobertura_noticias_anual.csv`, `cobertura_precos.csv`, `dicionario_dados.csv`, `manifesto_limpeza.json` e `registro_limpeza.md` são **gerados ao executar o notebook**, e não estão disponíveis para download neste GitHub. A pasta `data/processed/` também não é versionada.

A documentação do notebook e do README descreve quais verificações foram realizadas e como reproduzi-las.



## FinBERT e revisão inicial — 15/10/2026

- [Guia e relatório da revisão](finbert.md): método, resultados, limitações e próximos passos.
- [Notebook 02](../notebooks/02_sentimento_finbert.ipynb): classificação e agregado empresa/data.
- [Amostra revisada](revisao_manual/amostra_50_cf0a9799_e1f584a3.csv): 50 rótulos, observações e revisor, preservados como fornecidos pelo grupo.
- [Registro da execução](execucoes/finbert_2026-10-15.json): revisão do modelo, hashes, contagens e estado da revisão.

Os CSVs completos `noticias_com_sentimento.csv` e `sentimento_diario_noticias.csv` são gerados localmente em `data/processed/`. O cache permanece em `data/cache/`. O manifesto corrente, o dicionário e o resumo por empresa também são gerados localmente e ignorados pelo Git. O registro datado acima é uma cópia da execução validada, com a revisão preenchida. A amostra humana versionada não é sobrescrita ao executar novamente o notebook.


## Integração e retornos — 15/10/2026

- [Guia da integração](integracao.md): unidade de análise, snapshot, calendário, bordas e resultados.
- [Notebook 03](../notebooks/03_integracao_retornos.ipynb): oito células executadas sem erros.
- [Configuração](config_integracao.json): regras e hashes das entradas fixadas.
- [Dicionário dos novos campos](dicionario_integracao.csv).
- [Registro datado](execucoes/integracao_2026-10-15.json): versões, hashes, contagens e auditorias.

O painel completo contém 3.770 pares empresa/pregão de 2017–2019. As seis notícias com retorno em janeiro de 2020 são preservadas como margem; as janelas incompletas são sinalizadas. As bases e os relatórios correntes são gerados localmente conforme o guia.

Os registros de execução são históricos: `integracao_retornos: pendente` no registro do FinBERT descreve o momento de encerramento daquela etapa. O registro da integração posterior documenta sua conclusão. Esses registros não foram reescritos para simular uma nova execução.
