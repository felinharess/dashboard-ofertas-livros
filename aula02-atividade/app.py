"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def montar_tabela(livros):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": livro["nota"] * "⭐",
            "Preço": f"£ {livro["preco"]:.2f}",
            "Faixa": classificar_preco(livro["preco"])
        }
        tabela.append(linha)
    return tabela

def classificar_preco(preco):
    """Classifica um preço em libras em uma faixa de texto."""
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa(livros):
    """Conta quantos livros existem em cada faixa de preço: {"Caro": 403, ...}"""
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contagem:
            contagem[faixa] = contagem[faixa] + 1
        else:
            contagem[faixa] = 1

    return contagem

def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")
    livros = dados.carregar_livros()
   
    
    tabela = montar_tabela(livros)

    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", f"£{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])
    
    pesquisa = st.text_input("Digite o livro")
    livros, contador =  dados.filtrar_livros(pesquisa)
    if len(livros) == 0:
        st.markdown(
    """
    <div style="background-color: #F2D36B; padding: 10px; border-radius: 5px;">
        <span style="color: #000000; font-weight: bold;">
            Livro não encontrado!
        </span>
    </div>
    """,
    unsafe_allow_html=True
    )   
        

    else:
        tabela = montar_tabela(livros)
        st.write(f"{contador} livros filtrados" if contador != 1000 else "")
        st.dataframe(tabela)


if __name__ == "__main__":
    main()