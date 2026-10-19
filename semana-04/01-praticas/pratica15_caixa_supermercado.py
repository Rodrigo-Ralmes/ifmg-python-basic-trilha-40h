# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 15 - Caixa de supermercado
# Arquivo: pratica15_caixa_supermercado.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Implementar um sistema de caixa de supermercado utilizando dicionários,
# listas e tuplas. O sistema permite cadastrar ou atualizar produtos,
# listar produtos cadastrados, realizar vendas, atualizar o estoque,
# armazenar o histórico das vendas e emitir um relatório com o total geral.
#
# Conteúdos:
# - Dicionários
# - Dicionário de dicionários
# - Associação chave-valor
# - Listas
# - Tuplas
# - Lista de tuplas
# - Constantes
# - Funções
# - Parâmetros
# - Retorno de valores
# - Estrutura de repetição while
# - Estrutura de repetição for
# - Estruturas condicionais if, elif e else
# - Operadores in e not in
# - Método items()
# - Método append()
# - Função len()
# - Acumulador
# - Atualização de estoque
# - Menu de opções
# - Controle de fluxo com return e break
# - Estrutura __name__ == "__main__"
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# CONSTANTES
# =============================================================================

DESCRICAO = "DESCRIÇÃO"
ESTOQUE = "ESTOQUE"
PRECO = "PREÇO"


# =============================================================================
# FUNÇÃO - CADASTRAR OU ATUALIZAR PRODUTO
# =============================================================================

def cad_produto(dic_produtos):
    """
    Cadastra um novo produto ou atualiza estoque e preço
    de um produto já existente.

    Parâmetro:
        dic_produtos (dict):
            Dicionário principal contendo todos os produtos.

    Estrutura de cada produto:
        codigo -> {
            DESCRICAO: descrição,
            ESTOQUE: estoque,
            PRECO: preço
        }
    """

    print("\n" + "=" * 60)
    print("CADASTRAR / ATUALIZAR PRODUTO")
    print("=" * 60)

    codigo = int(
        input("\nCódigo do produto: ")
    )


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DO PRODUTO
    # -------------------------------------------------------------------------

    if codigo in dic_produtos:

        produto = dic_produtos[codigo]

        print("\nProduto existente:")
        print(produto)

    else:

        print("\nProduto não encontrado.")

        descricao = input(
            "Informe a descrição: "
        )

        produto = {
            DESCRICAO: descricao
        }

        dic_produtos[codigo] = produto


    # -------------------------------------------------------------------------
    # ATUALIZAÇÃO DO ESTOQUE
    # -------------------------------------------------------------------------

    produto[ESTOQUE] = float(
        input("Estoque: ")
    )


    # -------------------------------------------------------------------------
    # ATUALIZAÇÃO DO PREÇO
    # -------------------------------------------------------------------------

    produto[PRECO] = float(
        input("Preço: R$ ")
    )


    # -------------------------------------------------------------------------
    # CONFIRMAÇÃO
    # -------------------------------------------------------------------------

    print("\nProduto cadastrado/atualizado com sucesso.")


# =============================================================================
# FUNÇÃO - LISTAR PRODUTOS
# =============================================================================

def listar_produtos(dic_produtos):
    """
    Exibe todos os produtos cadastrados no sistema.

    Parâmetro:
        dic_produtos (dict):
            Dicionário contendo os produtos.
    """

    print("\n" + "=" * 60)
    print("LISTA DE PRODUTOS")
    print("=" * 60)


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DE DICIONÁRIO VAZIO
    # -------------------------------------------------------------------------

    if len(dic_produtos) == 0:

        print("\nNenhum produto encontrado!")

        input(
            "\nPressione ENTER para voltar."
        )

        return


    # -------------------------------------------------------------------------
    # PERCURSO DOS PRODUTOS
    # -------------------------------------------------------------------------

    for codigo, produto in dic_produtos.items():

        print("\n" + "-" * 60)

        print(
            f"Código: {codigo}"
        )

        print(
            f"Descrição: "
            f"{produto[DESCRICAO]}"
        )

        print(
            f"Estoque: "
            f"{produto[ESTOQUE]}"
        )

        print(
            f"Preço: "
            f"R$ {produto[PRECO]:.2f}"
        )


    print("\n" + "-" * 60)

    input(
        "\nPressione ENTER para voltar."
    )


# =============================================================================
# FUNÇÃO - REALIZAR VENDA
# =============================================================================

def venda(dic_produtos, lista_vendas):
    """
    Realiza a venda de um produto.

    A função:
    - solicita o código;
    - verifica se o produto existe;
    - solicita a quantidade;
    - verifica o estoque;
    - calcula o total;
    - reduz o estoque;
    - registra a venda.

    Parâmetros:
        dic_produtos (dict):
            Dicionário contendo os produtos.

        lista_vendas (list):
            Lista contendo as vendas realizadas.
    """

    print("\n" + "=" * 60)
    print("VENDA DE PRODUTO")
    print("=" * 60)

    codigo = int(
        input("\nCódigo do produto: ")
    )


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DO CÓDIGO
    # -------------------------------------------------------------------------

    if codigo not in dic_produtos:

        print(
            "\nProduto não encontrado!"
        )

        return


    # -------------------------------------------------------------------------
    # RECUPERAÇÃO DO PRODUTO
    # -------------------------------------------------------------------------

    produto = dic_produtos[codigo]

    print("\nProduto:")

    print(
        f"Descrição: {produto[DESCRICAO]}"
    )

    print(
        f"Estoque disponível: "
        f"{produto[ESTOQUE]}"
    )

    print(
        f"Preço unitário: "
        f"R$ {produto[PRECO]:.2f}"
    )


    # -------------------------------------------------------------------------
    # QUANTIDADE VENDIDA
    # -------------------------------------------------------------------------

    quantidade = float(
        input("\nQuantidade vendida: ")
    )


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DO ESTOQUE
    # -------------------------------------------------------------------------

    if quantidade > produto[ESTOQUE]:

        print(
            "\nEstoque insuficiente!"
        )

        return


    # -------------------------------------------------------------------------
    # CÁLCULO DO TOTAL DA VENDA
    # -------------------------------------------------------------------------

    total = (
        produto[PRECO]
        * quantidade
    )

    print(
        f"\nTotal da venda: "
        f"R$ {total:.2f}"
    )


    # -------------------------------------------------------------------------
    # CRIAÇÃO DA TUPLA DA VENDA
    # -------------------------------------------------------------------------

    registro_venda = (
        codigo,
        quantidade,
        produto[PRECO]
    )


    # -------------------------------------------------------------------------
    # ATUALIZAÇÃO DO ESTOQUE
    # -------------------------------------------------------------------------

    produto[ESTOQUE] -= quantidade


    # -------------------------------------------------------------------------
    # REGISTRO DA VENDA
    # -------------------------------------------------------------------------

    lista_vendas.append(
        registro_venda
    )

    print(
        "\nVenda realizada com sucesso."
    )


# =============================================================================
# FUNÇÃO - RELATÓRIO DE VENDAS
# =============================================================================

def relatorio_vendas(dic_produtos, lista_vendas):
    """
    Exibe todas as vendas realizadas e calcula o total geral.

    Parâmetros:
        dic_produtos (dict):
            Dicionário contendo os produtos.

        lista_vendas (list):
            Lista contendo as tuplas das vendas.
    """

    print("\n" + "=" * 60)
    print("RELATÓRIO DE VENDAS")
    print("=" * 60)


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DE VENDAS
    # -------------------------------------------------------------------------

    if len(lista_vendas) == 0:

        print(
            "\nNenhuma venda encontrada!"
        )

        input(
            "\nPressione ENTER para voltar."
        )

        return


    # -------------------------------------------------------------------------
    # INICIALIZAÇÃO DO TOTAL GERAL
    # -------------------------------------------------------------------------

    total_geral = 0


    # -------------------------------------------------------------------------
    # PERCURSO DAS VENDAS
    # -------------------------------------------------------------------------

    for codigo, quantidade, preco in lista_vendas:

        produto = dic_produtos[codigo]

        total = (
            quantidade
            * preco
        )

        print("\n" + "-" * 60)

        print(
            f"Código: {codigo}"
        )

        print(
            f"Produto: "
            f"{produto[DESCRICAO]}"
        )

        print(
            f"Quantidade: "
            f"{quantidade}"
        )

        print(
            f"Preço unitário: "
            f"R$ {preco:.2f}"
        )

        print(
            f"Total da venda: "
            f"R$ {total:.2f}"
        )


        # ---------------------------------------------------------------------
        # ACUMULADOR DO TOTAL GERAL
        # ---------------------------------------------------------------------

        total_geral += total


    # -------------------------------------------------------------------------
    # TOTAL GERAL
    # -------------------------------------------------------------------------

    print("\n" + "=" * 60)

    print(
        f"TOTAL GERAL: "
        f"R$ {total_geral:.2f}"
    )

    print("=" * 60)

    input(
        "\nPressione ENTER para voltar."
    )


# =============================================================================
# FUNÇÃO - MENU
# =============================================================================

def menu():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.

    Retorno:
        str:
            Opção informada pelo usuário em letra maiúscula.
    """

    print("\n" + "=" * 60)
    print("CAIXA DE SUPERMERCADO")
    print("=" * 60)

    print("\n(C) Cadastrar / atualizar produto")
    print("(L) Listar produtos")
    print("(V) Vender produto")
    print("(R) Relatório de vendas")
    print("(S) Sair")

    print("\n" + "=" * 60)

    escolha = input(
        "Informe sua opção: "
    ).upper().strip()

    return escolha


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def principal():
    """
    Controla o fluxo principal do sistema.
    """

    # =========================================================================
    # INICIALIZAÇÃO DAS ESTRUTURAS
    # =========================================================================

    lista_vendas = []

    dic_produtos = {}


    # =========================================================================
    # LAÇO PRINCIPAL
    # =========================================================================

    while True:

        escolha = menu()


        # ---------------------------------------------------------------------
        # CADASTRAR / ATUALIZAR
        # ---------------------------------------------------------------------

        if escolha == "C":

            cad_produto(
                dic_produtos
            )


        # ---------------------------------------------------------------------
        # LISTAR
        # ---------------------------------------------------------------------

        elif escolha == "L":

            listar_produtos(
                dic_produtos
            )


        # ---------------------------------------------------------------------
        # VENDER
        # ---------------------------------------------------------------------

        elif escolha == "V":

            venda(
                dic_produtos,
                lista_vendas
            )


        # ---------------------------------------------------------------------
        # RELATÓRIO
        # ---------------------------------------------------------------------

        elif escolha == "R":

            relatorio_vendas(
                dic_produtos,
                lista_vendas
            )


        # ---------------------------------------------------------------------
        # SAIR
        # ---------------------------------------------------------------------

        elif escolha == "S":

            print(
                "\nSistema encerrado."
            )

            break


        # ---------------------------------------------------------------------
        # OPÇÃO INVÁLIDA
        # ---------------------------------------------------------------------

        else:

            print(
                "\nOpção inválida! "
                "Tente novamente."
            )


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    principal()
