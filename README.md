# Sentimento de notícias e retornos de ações dos EUA

Projeto de **Análise Exploratória de Dados e Visualização — FGV EMAp, 2026.2**, professor João Rulff.  
**Integrantes:** Caio Ladislau do Couto, Alice Barros Lourencini Palaoro e Mateus Henrique da Costa Resende.

Investigamos associações entre o tom de manchetes e os retornos de **NVDA, NFLX, BAC, JNJ e KO em 2017–2019**, com medidas descritivas e gráficos interativos. O FinBERT é utilizado pronto, sem treinamento adicional.

## Leitura e organização

O [**notebook-artigo**](notebooks/00_artigo.ipynb) reúne dados, método, sete perguntas, gráficos e conclusões. Para explorar os controles sem Python, baixe o [**artigo HTML**](artigo_interativo.html) e abra no navegador. Os gráficos têm suas bibliotecas embutidas para uso offline; a formatação das fórmulas pode exigir internet. O GitHub exibe as imagens salvas do notebook.

| Notebook | Função |
| --- | --- |
| [00_artigo](notebooks/00_artigo.ipynb) | Análise, visualizações e tabelas das sete perguntas |
| [01_preparacao_dados](notebooks/01_preparacao_dados.ipynb) | Limpeza, FinBERT e integração com pregões e retornos, em uma execução |

Os [dados incluídos](data/README.md) permitem começar diretamente pelo artigo. A [documentação](docs/README.md) explica as decisões e limitações; a [proveniência](docs/proveniencia.json) registra origens, configurações e hashes.

## Reprodução

Use **Python 3.11**. Na pasta do projeto:

```text
python -m pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt
python -m ipykernel install --user --name aed-sentimento --display-name "Python (AED Sentimento)"
python -m notebook
```

Selecione **Python (AED Sentimento)**. Para refazer gráficos e tabelas, execute **00_artigo** em ordem. Para refazer também os dados, execute **01_preparacao_dados** inteiro em um único kernel e depois **00_artigo**. Salve o artigo executado e rode `python tools/exportar_artigo.py` para atualizar o HTML e as imagens.

A preparação usa o recorte bruto de 6.556 associações, o snapshot de cotações e as probabilidades FinBERT incluídos. A primeira execução pode precisar de internet para obter o tokenizador fixado. Os pesos do modelo são necessários apenas se houver textos sem probabilidades no cache. A [revisão humana](docs/revisao_manual/amostra_50_cf0a9799_e1f584a3.csv) é preservada. Outra coleta ou outra configuração de modelo exige conferir resultados e narrativa; as versões registradas não constituem um lock multiplataforma.

## Resultados e situação acadêmica

A cobertura é desigual, os retornos por classe se sobrepõem e as correlações são pequenas. A pergunta 7 compara a amostra principal (2.387 pares), o mínimo de três notícias (783), a amostra sem retrospectivas identificadas pela regra (2.271) e o filtro combinado (697), com reagregação. Os filtros alteram a composição e alguns sinais, sem um padrão uniforme entre empresas. As conclusões são exploratórias, sem interpretação causal.

O artigo tem a estrutura solicitada para a intermediária de **29/10**, com respostas exploratórias às sete perguntas. A etapa também exige uma apresentação de **cinco minutos** por grupo, cuja realização não é comprovada pelo repositório. A [regra de retrospectivas](docs/retrospectivas/README.md) é automática e conservadora e pode deixar passar relatos explícitos de preço já observado. Sua validação humana independente é uma melhoria metodológica recomendada, distinta da revisão humana de sentimento já realizada.

Para a entrega final na **Semana A2**, devem ser incorporados os comentários recebidos, preparada a apresentação de **dez minutos** e declaradas as contribuições efetivas dos integrantes. A presença dos arquivos não comprova envio formal ou aprovação pelo professor.
