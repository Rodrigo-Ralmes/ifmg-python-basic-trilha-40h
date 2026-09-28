# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 02 - Preços acima da média com lista
# Arquivo: pratica02_precos_acima_media_lista.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de 10 produtos em uma lista, calcular o preço médio
# e exibir os preços que estão acima da média.
#
# Conteúdos:
# - Listas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Função len()
# - Acumulador
# - Cálculo de média
# - Percurso de lista
# - Estrutura condicional if
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

precos = []
soma = 0


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("Informe o preço de 10 produtos:")

for i in range(1, 11):
    preco = float(input(f"Produto {i}: R$ "))

    precos.append(preco)

    soma += preco


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = soma / len(precos)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"\nPreço médio: R$ {media:.2f}")

print("\nPreços acima da média:")

for preco in precos:
    if preco > media:
        print(f"R$ {preco:.2f}")
