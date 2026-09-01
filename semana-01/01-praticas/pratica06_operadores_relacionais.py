# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:56:40 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 06 - Operadores relacionais
# Arquivo: pratica06_operadores_relacionais.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 10:56:40
#
# Objetivo:
# Praticar comparações entre valores utilizando operadores
# relacionais e observar os resultados booleanos.
#
# Conteúdos praticados:
# - ==
# - !=
# - >
# - <
# - >=
# - <=
# - bool
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# ENTRADA
# ============================================================

numero1 = float(input("Informe o primeiro número: "))

numero2 = float(input("Informe o segundo número: "))


# ============================================================
# COMPARAÇÕES
# ============================================================

igual = numero1 == numero2

diferente = numero1 != numero2

maior = numero1 > numero2

menor = numero1 < numero2

maior_ou_igual = numero1 >= numero2

menor_ou_igual = numero1 <= numero2


# ============================================================
# SAÍDA
# ============================================================

print()

print("=== COMPARAÇÕES ===")

print(numero1, "==", numero2, ":", igual)

print(numero1, "!=", numero2, ":", diferente)

print(numero1, ">", numero2, ":", maior)

print(numero1, "<", numero2, ":", menor)

print(numero1, ">=", numero2, ":", maior_ou_igual)

print(numero1, "<=", numero2, ":", menor_ou_igual)

print()

print("-------------- FIM PROGRAMA ---------------")