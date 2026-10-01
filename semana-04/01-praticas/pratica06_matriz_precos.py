# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 06 - Matriz de preços
# Arquivo: pratica06_matriz_precos.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Construir uma matriz de preços utilizando listas de listas para armazenar
# os valores de 5 produtos cotados em 3 fornecedores, calcular o preço médio
# de cada produto e calcular também o preço médio praticado por cada
# fornecedor.
#
# Conteúdos:
# - Listas
# - Listas de listas
# - Matrizes bidimensionais
# - Linhas e colunas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Laços de repetição aninhados
# - Função range()
# - Função enumerate()
# - Índices
# - Acesso a matriz por [linha][coluna]
# - Acumulador
# - Cálculo de média
# - Constantes
# - Percurso por linhas
# - Percurso por colunas
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# CONSTANTES
# =============================================================================

NUM_PRODUTOS = 5
NUM_FORNECEDORES = 3


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

matriz_precos = []


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("=" * 60)
print("COTAÇÃO DE PREÇOS - PRODUTOS E FORNECEDORES")
print("=" * 60)

for produto in range(NUM_PRODUTOS):

    print(f"\nProduto {produto + 1}")

    linha = []

    for fornecedor in range(NUM_FORNECEDORES):

        preco = float(
            input(
                f"Fornecedor {fornecedor + 1}: R$ "
            )
        )

        linha.append(preco)

    matriz_precos.append(linha)


# =============================================================================
# PROCESSAMENTO E SAÍDA - MÉDIA POR PRODUTO
# =============================================================================

print("\n" + "=" * 60)
print("PREÇO MÉDIO POR PRODUTO")
print("=" * 60)

for produto, linha in enumerate(matriz_precos, start=1):

    soma = 0

    for preco in linha:
        soma += preco

    media = soma / NUM_FORNECEDORES

    print(
        f"Produto {produto}: "
        f"R$ {media:.2f}"
    )


# =============================================================================
# PROCESSAMENTO E SAÍDA - MÉDIA POR FORNECEDOR
# =============================================================================

print("\n" + "=" * 60)
print("PREÇO MÉDIO POR FORNECEDOR")
print("=" * 60)

for fornecedor in range(NUM_FORNECEDORES):

    soma = 0

    for produto in range(NUM_PRODUTOS):

        soma += matriz_precos[produto][fornecedor]

    media = soma / NUM_PRODUTOS

    print(
        f"Fornecedor {fornecedor + 1}: "
        f"R$ {media:.2f}"
    )
