# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 05 - Cotação de fornecedores
# Arquivo: pratica05_cotacao_fornecedores.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de um mesmo produto informados por 5 fornecedores,
# calcular o preço médio da cotação e identificar quais fornecedores
# apresentam preço abaixo da média.
#
# Conteúdos:
# - Listas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Função len()
# - Função enumerate()
# - Percurso de listas
# - Cálculo de média
# - Estrutura condicional if
# - Comparação de valores
# - Identificação de fornecedores abaixo da média
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

print("Cotação de preços")

print("\nInforme o preço do produto em 5 fornecedores:")

for i in range(1, 6):
    preco = float(input(f"Fornecedor {i}: R$ "))

    precos.append(preco)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = sum(precos) / len(precos)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"\nPreço médio da cotação: R$ {media:.2f}")

print("\nFornecedores com preço abaixo da média:")

for indice, preco in enumerate(precos, start=1):
    if preco < media:
        print(f"Fornecedor {indice}: R$ {preco:.2f}")

