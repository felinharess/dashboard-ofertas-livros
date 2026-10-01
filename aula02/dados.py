"""Leitura e tratamento dos arquivos CSV do projeto."""

import csv
from pathlib import Path


# Pasta onde este arquivo .py está.
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores ainda vêm como texto neste momento.
    """

    livros = []

    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                livros.append(linha)

    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")

    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo:", error)

    return livros


def converter_preco(preco):
    """Converte o preço do formato '£51.77' para float."""

    return float(preco.replace("£", ""))


def converter_nota(nota):
    """Converte a nota escrita por extenso para número."""

    nota = nota.strip().lower()

    if nota == "five":
        return 5
    elif nota == "four":
        return 4
    elif nota == "three":
        return 3
    elif nota == "two":
        return 2
    else:
        return 1


def preparar_livros(linhas):
    """Converte os dados do CSV para o formato usado pelo programa."""

    livros = []

    for linha in linhas:
        livro = {
            "titulo": linha["titulo"],
            "preco": converter_preco(linha["preco"]),
            "categoria": linha["categoria"],
            "nota": converter_nota(linha["nota"]),
            "url": linha["url"]
        }

        livros.append(livro)

    return livros


def carregar_livros():
    """Lê o CSV e prepara os dados para serem utilizados."""

    livros_originais = ler_livros()

    return preparar_livros(livros_originais)


def calcular_preco_medio(livros):
    """Calcula o preço médio dos livros."""

    if not livros:
        return 0

    soma = 0

    for livro in livros:
        # O preço já foi convertido para float em preparar_livros()
        soma += livro["preco"]

    preco_medio = soma / len(livros)

    return preco_medio


def contar_cinco_estrelas(livros):
    """Conta quantos livros possuem nota 5."""

    contador = 0

    for livro in livros:
        # A nota já foi convertida para int em preparar_livros()
        if livro["nota"] == 5:
            contador += 1

    return contador


def encontrar_mais_caro(livros):
    """Encontra o livro com o maior preço."""

    if not livros:
        return None

    mais_caro = livros[0]

    for livro in livros:
        # O preço já é float
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro

    return mais_caro


if __name__ == "__main__":
    livros = carregar_livros()

    print(f"{len(livros)} livros carregados")
    print("Primeiro livro:", livros[0])
