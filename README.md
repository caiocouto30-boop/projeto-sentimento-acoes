# Sentimento das notícias e comportamento de ações dos EUA

Projeto de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**.

**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

## Objetivo

Investigar **associações descritivas**, sem atribuição de causalidade, entre o tom de manchetes financeiras e os retornos/magnitude das oscilações diárias de NVIDIA (NVDA), Netflix (NFLX), Bank of America (BAC), Johnson & Johnson (JNJ) e Coca-Cola (KO), no período **2017–2019**.

## Estado do projeto — 15/10/2026

A preparação e a auditoria das **notícias e cotações** foram concluídas na execução registrada do notebook. Os números abaixo vêm das saídas salvas e **ainda não foram reproduzidos independentemente por outro integrante**.

| Verificação | Resultado registrado |
| --- | ---: |
| Notícias no recorte antes da limpeza | 6.556 |
| Duplicatas excedentes removidas | 4 |
| Associações manchete–empresa após limpeza | **6.552** |
| Pregões em 2017–2019, por empresa | **754** |
| Lacunas de preços entre as cinco séries na coleta registrada | 0 |

A distribuição das notícias após limpeza foi: **NFLX 2.344**, **NVDA 1.647**, **JNJ 1.046**, **BAC 871** e **KO 644**.

![Mapa de calor da cobertura mensal de notícias após limpeza](figures/cobertura_noticias_mensal.png)

**Pendente:** FinBERT, agregação diária de sentimento, integração ao primeiro pregão estritamente posterior, cálculo dos retornos, análise das perguntas 2 a 7 e revisão cruzada da execução. A presença de resultados salvos não substitui a execução do notebook do início ao fim.

## Organização do repositório

- `notebooks/01_preparacao_inicial.ipynb` — versão **explicada e atual**, com limpeza, verificações, gráfico e resultados registrados.
- `figures/cobertura_noticias_mensal.png` — figura produzida pelo notebook.
- `data/raw/` — CSV original e snapshots de cotações, **não versionados**.
- `data/processed/` — dados tratados e arquivos de auditoria, **não versionados**.
- `docs/README.md` — referências e localização dos documentos acadêmicos. O notebook também gera relatórios locais em `docs/`, ignorados pelo Git.
- `requirements.txt` — dependências do projeto (versões não integralmente fixadas).

## Fontes dos dados

1. [Daily Financial News for 6000+ Stocks — Kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests): baixar `raw_analyst_ratings.csv` e colocar em `data/raw/raw_analyst_ratings.csv`. A versão usada na execução registrada tem SHA-256 `609289a49dc8af2bd28a8466dffd9663521237026f1040c0f238010b29135fb6`.
2. [Yahoo Finance via yfinance](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html): coleta diária de 15/12/2016 até 11/01/2020 (**fim exclusivo**), com `Adj Close` e `Volume`. O notebook usa snapshot local validado por hash, ou coleta os dados se não houver snapshot. A versão da fonte pode mudar; registre divergências em vez de impor contagens artificiais.
3. [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert): modelo pronto previsto para a próxima etapa, **ainda não aplicado**.

**Não adicione ao GitHub o CSV original, snapshots grandes, tokens, credenciais ou arquivos `.env`.**

## Como executar

1. Clone o repositório e entre na pasta do projeto.
2. Use **Python 3.11**. Crie e ative um ambiente virtual (ou um ambiente Conda equivalente) e instale as dependências:
   ```bash
   python -m venv .venv
   # Ative o ambiente: Windows PowerShell: .venv\Scripts\Activate.ps1
   # Linux/macOS: source .venv/bin/activate
   python -m pip install -r requirements.txt
   python -m ipykernel install --user --name aed-sentimento --display-name "Python (AED Sentimento)"
   ```
3. Baixe o CSV original para `data/raw/`, conforme acima.
4. Inicie `jupyter notebook` e abra `notebooks/01_preparacao_inicial.ipynb`. Execute as células **em ordem**, a partir do começo.
5. Na ausência de `data/raw/cotacoes_yahoo_margem.csv` e do JSON de metadados correspondente, a célula de coleta tentará acessar o Yahoo Finance. Para reprodução exata, o grupo deve disponibilizar o snapshot original fora do Git e verificar o SHA-256. **Não substitua silenciosamente um snapshot por outro.**
6. Confira as asserções, os arquivos em `data/processed/`, os relatórios em `docs/` e a figura em `figures/`. Registre diferenças de versões e de dados.

**Versões observadas na execução salva:** Python 3.11.16, pandas 3.0.6, numpy 2.4.6, matplotlib 3.11.2, seaborn 0.13.2, yfinance 1.7.0, ipykernel 7.4.0. Não constituem um arquivo de dependências completamente travado.

## Método e cautelas

As notícias foram filtradas por empresa e data; manchetes vazias e duplicatas por `stock + news_date + headline` foram auditadas, preservando identificadores e rastreabilidade. Registros relacionados a mais de uma empresa foram mantidos e sinalizados.

A análise de retornos deverá associar cada notícia ao **primeiro pregão estritamente posterior**, pois os horários não são confiáveis. Vários dias de notícia podem corresponder ao mesmo pregão; a unidade de análise dos retornos será **empresa × pregão**, sem duplicação artificial de observações. Dias sem notícias não equivalem a sentimento neutro.

O retorno absoluto mede a magnitude percentual da mudança diária; **não é uma estimativa de volatilidade estatística**. Notícias podem descrever movimentos já ocorridos, de modo que associações futuras não serão interpretadas como causalidade.

## Perguntas e entregas

As sete perguntas de domínio estão no notebook, começando pela cobertura de notícias e avançando para composição e evolução do sentimento, retornos, diferenças entre empresas/anos e robustez. A pergunta 1 já possui resposta parcial; as demais seguem pendentes.

- **29/10/2026:** entrega intermediária, notebook em formato de artigo e apresentação de cinco minutos.
- **Semana A2:** entrega final, notebook, repositório documentado, apresentação de dez minutos e declaração de contribuições. A janela 23–30/11 foi informada pelo grupo; a data exata deve ser confirmada. Meta interna: 22/11.

Consulte [a relação dos documentos de referência](docs/README.md). Registrem as contribuições e revisões de cada integrante.
