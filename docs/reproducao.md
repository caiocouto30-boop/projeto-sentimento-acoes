# Reprodução da versão final

O caminho mais curto usa as três bases de `data/processed/`, incluídas no projeto. Instale as duas dependências de `requirements-analise.txt` e rode `python tools/exportar_artigo.py`, seguido de `python tools/verificar_final.py`. O segundo comando confere limpeza, cache, alinhamento, retornos e números da análise e compara os coeficientes com a versão anterior.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| `analise_final.py` | Agregações, intensidade média, correlações, tabelas e invariantes |
| `robustez.py`, `retrospectivas.py` | Regra de retrospectivas e reagregação dos cenários preservados |
| `montar_entrega.py` | Narrativa, HTML offline e fonte do notebook |
| `graficos_final.js` | Gráficos, filtros, hover, clique e consulta de manchetes |
| `executar_artigo.py` | Execução sequencial das células e gravação de saídas reais |
| `verificar_final.py` | Regressão dos resultados anteriores e Spearman por postos independentes |

## Figuras estáticas

As sete imagens em `figures/analise_final/` são exportações dos gráficos Plotly, não capturas de notícias externas. Ao alterar dados ou codificações, regenere o HTML e atualize essas imagens. No console de desenvolvimento do HTML, o seguinte comando exporta um gráfico:

```javascript
Plotly.downloadImage(document.getElementById('q1'), {
  format: 'png', scale: 2, filename: 'q1'
});
```

Repita para `q1` até `q7`, com empresa `Todas` e ano `Todos`, e salve os arquivos nessa pasta. Depois rode `python tools/executar_artigo.py` para embutir as alternativas PNG atualizadas. O notebook conserva também o gráfico interativo, independente da imagem.

## Notebook e navegador

As saídas interativas usam um iframe com conteúdo comprimido, a biblioteca Plotly incluída e a API nativa `DecompressionStream` de navegadores recentes. Confie no notebook no Jupyter para executar o HTML salvo. O HTML principal não depende desse mecanismo de compressão, nem de Python ou internet. O GitHub pode exibir apenas as imagens alternativas.

## Preparação integral

O notebook `01_preparacao_dados.ipynb` preserva o caminho original, com versões e modelo fixados. Ele pode obter o tokenizador e executar FinBERT se faltar cache. A finalização não treinou um modelo nem baixou novos preços. Os dados brutos, identificadores, quatro duplicatas e revisão humana foram preservados. Não substitua o snapshot por preços atuais sem refazer verificações e revisar a narrativa.
