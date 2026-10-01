"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import pandas 

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"
livros = pandas.read_csv(CAMINHO_LIVROS)

print(livros)
