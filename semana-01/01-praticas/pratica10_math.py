# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:30:42 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Trilha: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 10 - Biblioteca math
# Arquivo: pratica10_math.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026
#
# Objetivo:
# Conhecer a importação da biblioteca math e experimentar
# algumas funções matemáticas disponíveis nela.
#
# Conteúdos praticados:
# - import
# - biblioteca math
# - math.pi
# - math.sqrt()
# - math.ceil()
# - math.floor()
# - math.pow()
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# IMPORTAÇÃO DA BIBLIOTECA
# ============================================================

import math


# ============================================================
# CONSTANTE PI
# ============================================================

print("Valor de pi:", math.pi)


# ============================================================
# RAIZ QUADRADA
# ============================================================

numero = 25

raiz = math.sqrt(numero)

print()

print("Número:", numero)

print("Raiz quadrada:", raiz)


# ============================================================
# ARREDONDAMENTO PARA CIMA
# ============================================================

valor = 5.2

print()

print("Valor:", valor)

print("Arredondamento para cima:", math.ceil(valor))


# ============================================================
# ARREDONDAMENTO PARA BAIXO
# ============================================================

print("Arredondamento para baixo:", math.floor(valor))


# ============================================================
# POTÊNCIA
# ============================================================

base = 2

expoente = 3

potencia = math.pow(base, expoente)

print()

print("Base:", base)

print("Expoente:", expoente)

print("Potência:", potencia)


# ============================================================
# EXEMPLO COM CIRCUNFERÊNCIA
# ============================================================

raio = 5

area = math.pi * raio ** 2

comprimento = 2 * math.pi * raio

print()

print("=== CIRCUNFERÊNCIA ===")

print("Raio:", raio)

print("Área:", area)

print("Comprimento:", comprimento)