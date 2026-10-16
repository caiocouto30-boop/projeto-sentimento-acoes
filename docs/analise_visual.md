# Análise visual — etapa de 20–23/10

Executada antecipadamente em **16/10/2026**, continuando a integração de 17–19/10. O [notebook 04](../notebooks/04_analise_visual.ipynb) contém 12 células de código executadas, explicação de cada transformação e resultados. O [artigo](../notebooks/00_artigo.ipynb) reúne a interpretação acadêmica.

## O que foi entregue

- Nove figuras com fonte, unidade, período, escalas comparáveis e tamanhos amostrais.
- Onze tabelas de apoio, configuração prévia dos cálculos e manifesto de execução.
- Primeiras respostas às perguntas 1–6 e comparação inicial da 7 com mínimo de três notícias.

## Decisões de análise

As hipóteses H1–H3 já estavam documentadas. A [configuração](config_analise_visual.json) fixou entradas, filtro e regra de extremos antes dos novos cálculos, sem alegar pré-registro formal. Não houve exclusão por valor do retorno, winsorização ou ajuste do limite de notícias conforme o sinal encontrado.

Perguntas 1–2 usam 6.552 associações manchete–empresa; a 3 usa 2.569 pares empresa/data civil. Perguntas 4–6 usam `tem_noticias & elegivel_analise_principal`, com 2.387 pares empresa/pregão. A sensibilidade seleciona `n_noticias >= 3` dentro desse conjunto: 783 pares. Não usa contagem por data civil, nem repete retornos por manchete.

Spearman é a correlação de Pearson dos postos médios. Grupos constantes ou com menos de três pares não recebem coeficiente. As comparações são descritivas: não incluem testes de significância, intervalos de confiança, identificação causal nem avaliação preditiva. O ano é o do pregão de resposta. Ausência de notícias não é neutralidade.

## Primeiras respostas

| Pergunta | Achado e limite principal |
| --- | --- |
| 1 | NFLX reúne 2.344 associações e KO 644; cobertura desigual no corpus. |
| 2 | Neutro é a classe mais frequente nas cinco empresas; KO tem 61,8% neutras, JNJ 29,3% positivas e NVDA 24,0% negativas. |
| 3 | Os dez extremos diários selecionados têm uma manchete cada. Há retrospectivas e um título sobre PACCAR associado a BAC; textos foram preservados. |
| 4 | Distribuições se sobrepõem; não há ordem de medianas por sentimento comum às cinco empresas. |
| 5 | Intensidade × retorno absoluto: ρ entre −0,010 e +0,055, sem apoio descritivo claro a H2 nesta definição. |
| 6 | Escore × retorno no período completo: ρ entre −0,041 e +0,058. Mudanças anuais de sinal não demonstram diferenças estruturais. |
| 7 | Restam 32,8% dos pares; retenção desigual e alguns sinais mudam. Robustez completa não demonstrada. |

## Rastreabilidade e reprodução

O [manifesto](analise_visual/manifesto.json) registra versões, hashes das três entradas, contagens e tabelas. As bases completas continuam locais e não são versionadas. O pacote entregue inclui as oito tabelas tratadas da etapa anterior e pode iniciar no notebook 04; ele não contém o CSV bruto nem todos os pesos/caches necessários para repetir 01 e 02.

1. Use o ambiente `aed-sentimento`, ou Python 3.11 e as dependências registradas em `requirements.txt`.
2. Abra Jupyter a partir da pasta do projeto; selecione o kernel do ambiente.
3. Execute 04 do começo ao fim. Entradas divergentes interrompem a execução; investigar a diferença precede qualquer atualização explícita da configuração.
4. Compare resumos e hashes. Se os resultados mudarem, atualize o texto e as figuras do artigo, que não se reescrevem automaticamente.

| Saída | Uso |
| --- | --- |
| `figures/analise_visual/*.png` | Figuras exportadas e usadas no artigo. |
| `docs/analise_visual/*.csv` | Onze tabelas, incluindo cobertura, extremos, distribuição de retornos e coeficientes. |
| `data/processed/manchetes_extremos_analise.csv` | Textos, identificadores e URLs dos extremos; presente no pacote local. |
| `docs/analise_visual/manifesto.json` | Registro da execução e hashes das tabelas. |
| `docs/validacao_analise_visual.json` | Conferência numérica por operações alternativas e preservação dos originais. |

## Lista de análises a melhorar

1. **Retrospectivas:** o conceito do cronograma é texto que relata movimento de preço já ocorrido. Definir regra operacional, exemplos positivos/negativos e casos ambíguos; revisar sem consultar o efeito sobre retornos; guardar marcação e motivo. Não aplicar exclusão guiada pelo resultado.
2. **Filtros separados e combinados:** após remover manchetes, recalcular probabilidades médias, classe, escore, intensidade e contagens por pregão. Aplicar mínimo de três sobre os textos restantes e informar perdas por empresa/ano.
3. **Extremos:** revisar casos com várias manchetes e vínculos indiretos de ticker, incluindo BAC/PACCAR, sem apagar os registros originais.
4. **Sensibilidade e composição:** examinar grupos por ano e reconhecer que restrição de quantidade altera cobertura e amplitude da variável. As duas amostras são sobrepostas.
5. **Revisão do grupo:** outro integrante deve reproduzir as etapas a partir dos snapshots e revisar a narrativa. Preparação de slides e ensaio seguem a janela de 27–28/10; não foram realizados nesta etapa.

Fontes dos cálculos: dados tratados e snapshot da integração. Referências técnicas: [pandas corr](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html), [pandas rank](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html) e [Matplotlib boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html), consultadas em 16/10/2026.
