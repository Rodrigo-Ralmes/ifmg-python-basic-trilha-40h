# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:12:50 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 08 - Funções básicas
# Arquivo: pratica08_funcoes.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 15:12:50
#
# Objetivo:
# Experimentar algumas funções disponíveis no Python e
# observar os resultados produzidos.
#
# Conteúdos praticados:
# - abs()
# - round()
# - type()
# - chr()
# - ord()
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# FUNÇÃO ABS
# ============================================================

numero = -25

print("Valor original:", numero)

print("Valor absoluto:", abs(numero))


# ============================================================
# FUNÇÃO ROUND
# ============================================================

numero_decimal = 3.14159265

print()

print("Número original:", numero_decimal)

print("Arredondado:", round(numero_decimal))

print("Arredondado para 2 casas:", round(numero_decimal, 2))


# ============================================================
# FUNÇÃO TYPE
# ============================================================

idade = 47

altura = 1.75

nome = "Python"

print()

print("Tipo da idade:", type(idade))

print("Tipo da altura:", type(altura))

print("Tipo do nome:", type(nome))


# ============================================================
# CHR E ORD
# ============================================================

print()

print("Código 65 convertido em caractere:", chr(65))

print("Caractere A convertido em código:", ord("A"))