# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:10:27 2026

@author: Rodrigo
"""

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Exercício oficial
# Exercício: 03 - Cálculo de juros simples
# Arquivo: ex03_juros_simples.py
# Autor: Rodrigo de Almeida Silveira
# Data: 02/09/2026 18:10:27
#
# Objetivo:
# Solicitar o capital inicial, a taxa de juros e o tempo,
# calcular os juros simples e apresentar o montante final.
#
# Conteúdos praticados:
# - input()
# - float()
# - int()
# - variáveis
# - operadores aritméticos
# - cálculo de porcentagem
# - juros simples
# - saída formatada
# - f-string
#
# Status: Concluído
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

capital = float(input("Digite o capital inicial: R$ "))
taxa_percentual = float(input("Digite a taxa de juros (% ao período): "))
tempo = int(input("Digite a quantidade de períodos: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

taxa_decimal = taxa_percentual / 100
juros = capital * taxa_decimal * tempo
montante = capital + juros


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CÁLCULO DE JUROS SIMPLES ===")
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa de juros: {taxa_percentual:.2f}% ao período")
print(f"Quantidade de períodos: {tempo}")
print(f"Juros: R$ {juros:.2f}")
print(f"Montante final: R$ {montante:.2f}")
print()