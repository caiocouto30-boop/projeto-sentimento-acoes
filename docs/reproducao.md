# Reprodução

O procedimento atual está no README da raiz. A fonte principal é `notebooks/00_artigo.ipynb`; execute e salve o notebook antes de exportar. `tools/exportar_artigo.py` usa nbconvert e não modifica células.

Use `requirements-notebook.txt` para a análise e as visualizações Altair. `requirements.txt` preserva as dependências da preparação original. As tabelas são geradas pela última célula em `docs/analise_final/`. `tools/verificar_notebook.py` compara os resultados dessas células com os cálculos independentes.

As saídas distribuídas foram executadas no IPython no mesmo processo. A execução convencional em kernel separado e a revisão visual devem ser repetidas pelo grupo no seu Jupyter. O modo exato está em `metadata.execucao_final` do notebook e em `analise_final/verificacao_notebook.json`.
