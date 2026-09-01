# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:29:03 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 07 - Operadores lógicos
# Arquivo: pratica07_operadores_logicos.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 14:29:03
#
# Objetivo:
# Praticar operadores da lógica proposicional utilizando
# valores booleanos.
#
# Conteúdos praticados:
# - bool
# - and
# - or
# - not
# - operadores relacionais
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# VALORES BOOLEANOS
# ============================================================

valor1 = True

valor2 = False


# ============================================================
# OPERADOR NOT
# ============================================================

print("=== OPERADOR NOT ===")

print("not True =", not valor1)

print("not False =", not valor2)


# ============================================================
# OPERADOR AND
# ============================================================

print()

print("=== OPERADOR AND ===")

print("True and True =", True and True)

print("True and False =", True and False)

print("False and True =", False and True)

print("False and False =", False and False)


# ============================================================
# OPERADOR OR
# ============================================================

print()

print("=== OPERADOR OR ===")

print("True or True =", True or True)

print("True or False =", True or False)

print("False or True =", False or True)

print("False or False =", False or False)


# ============================================================
# COMBINANDO COMPARAÇÕES
# ============================================================

numero = 10

comparacao1 = numero > 5

comparacao2 = numero < 20

resultado = comparacao1 and comparacao2

print()

print("Número:", numero)

print("Número > 5:", comparacao1)

print("Número < 20:", comparacao2)

print("Número > 5 AND número < 20:", resultado)