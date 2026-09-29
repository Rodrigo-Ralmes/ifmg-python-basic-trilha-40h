# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 03 - Lista por índices
# Arquivo: pratica03_lista_por_indices.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de 10 produtos em uma lista, calcular o preço médio
# e identificar quais produtos possuem preço acima da média utilizando
# os índices da lista.
#
# Conteúdos:
# - Listas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Função len()
# - Índices de listas
# - Acesso a elementos por posição
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

for i in range(len(precos)):
    if precos[i] > media:
        print(f"Produto {i + 1}: R$ {precos[i]:.2f}")
        



