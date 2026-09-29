# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 04 - Percorrendo lista com enumerate()
# Arquivo: pratica04_lista_enumerate.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de 10 produtos em uma lista, calcular o preço médio
# e identificar os produtos com preço acima da média utilizando a função
# enumerate() para obter simultaneamente o índice e o valor de cada elemento.
#
# Conteúdos:
# - Listas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Função len()
# - Função enumerate()
# - Índices de listas
# - Percurso de listas
# - Acumulador
# - Cálculo de média
# - Estrutura condicional if
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

precos = []


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("Informe o preço de 10 produtos:")

for i in range(1, 11):
    preco = float(input(f"Produto {i}: R$ "))

    precos.append(preco)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = sum(precos) / len(precos)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"\nPreço médio: R$ {media:.2f}")

print("\nProdutos com preço acima da média:")

for indice, preco in enumerate(precos, start=1):
    if preco > media:
        print(f"Produto {indice}: R$ {preco:.2f}")