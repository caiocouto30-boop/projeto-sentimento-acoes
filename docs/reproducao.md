# Reprodução

O procedimento atual está no README da raiz. A fonte principal é `notebooks/00_artigo.ipynb`; execute e salve o notebook antes de exportar. `tools/exportar_artigo.py` usa nbconvert e não modifica células.

Use `requirements-notebook.txt` para a análise e as visualizações Altair. `requirements.txt` preserva as dependências da preparação original. As tabelas são geradas pela última célula em `docs/analise_final/`. `tools/verificar_notebook.py` compara os resultados dessas células com os cálculos independentes.

As saídas distribuídas foram executadas no IPython no mesmo processo. A execução convencional em kernel separado e a revisão visual devem ser repetidas pelo grupo no seu Jupyter. O modo exato está em `metadata.execucao_final` do notebook e em `analise_final/verificacao_notebook.json`.

O exportador incorpora o conteúdo de `vendor/vega-bundle.js` uma vez por HTML. Esse arquivo reúne Vega, Vega-Lite e Vega-Embed e foi recuperado da primeira figura do [HTML da versão original](https://github.com/caiocouto30-boop/projeto-sentimento-acoes/blob/620f468968c957cdb3336b14d7dd4a08770f1764/artigo_interativo.html). As especificações e os títulos vêm das saídas da execução atual do notebook.
