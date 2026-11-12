# Sentimento das notícias e retornos de ações dos EUA

Projeto final de **Análise Exploratória de Dados e Visualização, FGV EMAp, 2026.2**, professor João Rulff.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

Análise exploratória de NVDA, NFLX, BAC, JNJ e KO em 2017–2019. O estudo usa 6.552 associações manchete–empresa, probabilidades FinBERT já calculadas e cotações ajustadas do Yahoo Finance. Não envolve novo treinamento, recomendação financeira ou identificação causal.

## Arquivos de entrega

| Arquivo | Uso |
| --- | --- |
| [notebooks/00_artigo.ipynb](notebooks/00_artigo.ipynb) | Notebook final em formato de artigo, com as sete perguntas e saídas salvas |
| [artigo_interativo.html](artigo_interativo.html) | Leitura e exploração offline, sem Python |
| [apresentacao/apresentacao_final_entrega.pptx](apresentacao/apresentacao_final_entrega.pptx) | Dez slides editáveis, gráficos nativos e notas de fala |
| [apresentacao/roteiro_10_minutos.md](apresentacao/roteiro_10_minutos.md) | Distribuição de 600 segundos, incluindo demonstração das notícias |
| [DECLARACAO_CONTRIBUICOES.md](DECLARACAO_CONTRIBUICOES.md) | Declaração editável para registrar a divisão efetiva do trio |

Baixe e descompacte o projeto. Abra o HTML em navegador recente. No hover de um ponto aparecem títulos e assuntos. Clique para consultar todas as notícias do agregado, com datas, fonte e link. O assunto é uma sugestão lexical sobre a manchete, não um resumo do artigo completo. A busca permite consultar as notícias sem depender do mouse. Os links externos precisam de internet, mas os gráficos e títulos preservados funcionam offline.

No Jupyter, confie no notebook para executar as saídas HTML interativas. O GitHub pode preferir as imagens PNG salvas como alternativa estática. Cada seção também tem tabelas e análise escrita.

## Reprodução da análise final

Ambiente da execução verificada: Python 3.12.14, pandas 3.0.1 e NumPy 2.3.5. Na raiz do projeto:

```text
python -m pip install -r requirements-analise.txt
python tools/exportar_artigo.py
python tools/verificar_final.py
```

O primeiro comando de exportação refaz tabelas e HTML e executa todas as células Python do artigo, em ordem, com um único namespace. Não inicia um servidor Jupyter. As saídas são reais e podem ser abertas no Jupyter. As imagens incluídas representam a renderização verificada dos mesmos gráficos; mudanças nos dados ou nas codificações também exigem atualizá-las, usando o procedimento em [docs/reproducao.md](docs/reproducao.md).

Para abrir e executar manualmente, use seu ambiente Jupyter ou instale `notebook` e execute `python -m notebook`. O artigo não precisa de acesso ao modelo, tokenizador ou Yahoo Finance para reutilizar as entradas incluídas.

## Preparação original e fontes

O [notebook de preparação](notebooks/01_preparacao_dados.ipynb) preserva limpeza, FinBERT e integração da versão anterior. Sua execução completa usa [requirements.txt](requirements.txt) e pode precisar de internet para obter o tokenizador fixado. Só há inferência nova se faltarem probabilidades no cache. Essa etapa não foi reexecutada com novos pesos na finalização.

A verificação final refaz a limpeza do recorte, confere cache e escores, verifica primeiro pregão posterior, recalcula retornos do snapshot e confere agregações e cenários. A [revisão humana de 50 manchetes](docs/revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) foi preservada, sem acrescentar rótulos inventados.

Dados: [Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests), Yahoo Finance via yfinance e [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert/tree/4556d13015211d73dccd3fdd39d39232506f3e43). A [proveniência original](docs/proveniencia.json) registra a preparação anterior. A finalização tem seu [registro próprio](docs/proveniencia_final.json), com hashes e referência à versão de origem.

## Achados e mudanças finais

H1, sobre cobertura desigual, recebe apoio descritivo. H2, sobre intensidade do sentimento e oscilação posterior, não apresenta apoio uniforme. H3 encontra variação descritiva entre empresas e anos, sem teste confirmatório de diferenças. Retornos por classe se sobrepõem e a associação entre quantidade e oscilação é fraca.

Preservamos o módulo do escore médio, agora chamado **polarização líquida**, e acrescentamos **média dos módulos individuais** para avaliar intensidade sem cancelamento. Essa comparação adicional não é um novo teste confirmatório. As medidas e os cenários de robustez são reagregados após excluir manchetes.

O [registro de alterações](docs/mudancas_final.md) relaciona o retorno do professor e os critérios do enunciado às mudanças. Os gráficos usam Plotly.js, com uma biblioteca compartilhada no HTML offline e consulta centralizada das notícias. O código das transformações está em [tools/analise_final.py](tools/analise_final.py), e a narrativa e o exportador em [tools/montar_entrega.py](tools/montar_entrega.py).

## Pendências do grupo antes do envio

Preencher as contribuições efetivas, revisar o conteúdo em conjunto e ensaiar a fala. Confirmar o dia exato e o procedimento de entrega da Semana A2. Os arquivos não comprovam envio formal, aprovação ou reprodução por outro integrante.
