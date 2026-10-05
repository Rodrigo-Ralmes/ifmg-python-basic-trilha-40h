# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 11 - Tuplas aplicadas a produtos
# Arquivo: pratica11_tuplas_produtos.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar o nome e o preço de 10 produtos utilizando tuplas, inserir essas
# tuplas em uma lista, calcular o preço médio dos produtos e identificar
# aqueles que possuem preço acima da média por meio do desempacotamento.
#
# Conteúdos:
# - Tuplas
# - Listas
# - Lista de tuplas
# - Criação de tuplas
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Acumulador
# - Cálculo de média
# - Desempacotamento de tuplas
# - Estrutura condicional if
# - Formatação de valores monetários
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

soma = 0

lista_produtos = []


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("=" * 60)
print("CADASTRO DE PRODUTOS")
print("=" * 60)

print("\nInforme os dados de 10 produtos:")

for contador in range(1, 11):

    print(f"\nProduto {contador}")

    nome = input("Nome: ")

    preco = float(input("Preço: R$ "))


    # -------------------------------------------------------------------------
    # CRIAÇÃO DA TUPLA
    # -------------------------------------------------------------------------

    produto = (nome, preco)


    # -------------------------------------------------------------------------
    # ACUMULADOR
    # -------------------------------------------------------------------------

    soma += preco


    # -------------------------------------------------------------------------
    # INSERÇÃO DA TUPLA NA LISTA
    # -------------------------------------------------------------------------

    lista_produtos.append(produto)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = soma / len(lista_produtos)


# =============================================================================
# SAÍDA DE DADOS - PREÇO MÉDIO
# =============================================================================

print("\n" + "=" * 60)
print("RESULTADO")
print("=" * 60)

print(f"\nPreço médio dos produtos: R$ {media:.2f}")


# =============================================================================
# SAÍDA DE DADOS - PRODUTOS ACIMA DA MÉDIA
# =============================================================================

print("\nProdutos com preço acima da média:")

for produto in lista_produtos:

    # -------------------------------------------------------------------------
    # DESEMPACOTAMENTO DA TUPLA
    # -------------------------------------------------------------------------

    nome, preco = produto


    # -------------------------------------------------------------------------
    # VERIFICAÇÃO DO PREÇO
    # -------------------------------------------------------------------------

    if preco > media:

        print(
            f"\nProduto: {nome}"
        )

        print(
            f"Preço: R$ {preco:.2f}"
        )