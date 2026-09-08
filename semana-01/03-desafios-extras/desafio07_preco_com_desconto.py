# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 07 - Preço com desconto
# Arquivo: desafio07_preco_com_desconto.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Calcular o valor do desconto e o preço final de um produto.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - porcentagem
# - operadores aritméticos
# - formatação monetária
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

preco = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

valor_desconto = preco * (percentual_desconto / 100)
preco_final = preco - valor_desconto


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== PREÇO COM DESCONTO ===")
print(f"Preço original: R$ {preco:.2f}")
print(f"Percentual de desconto: {percentual_desconto:.2f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
