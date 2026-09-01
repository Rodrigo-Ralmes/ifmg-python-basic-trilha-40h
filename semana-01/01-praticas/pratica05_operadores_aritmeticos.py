# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 08:08:08 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 05 - Operadores aritméticos
# Arquivo: pratica05_operadores_aritmeticos.py
# Autor: Rodrigo de Almeida Silveira
# Data: 01/09/2026 08:08:08
#
# Objetivo:
# Praticar os principais operadores aritméticos disponíveis
# na linguagem Python.
#
# Conteúdos praticados:
# - soma +
# - subtração -
# - multiplicação *
# - divisão /
# - divisão inteira //
# - resto da divisão %
# - potenciação **
#
# Status: Prática
# ============================================================


# ============================================================
# ENTRADA
# ============================================================

numero1 = float(input("Informe o primeiro número: "))

numero2 = float(input("Informe o segundo número: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

soma = numero1 + numero2

subtracao = numero1 - numero2

multiplicacao = numero1 * numero2

divisao = numero1 / numero2

divisao_inteira = numero1 // numero2

resto = numero1 % numero2

potencia = numero1 ** numero2


# ============================================================
# SAÍDA
# ============================================================

print()

print("=== RESULTADOS ===")

print("Soma:", soma)

print("Subtração:", subtracao)

print("Multiplicação:", multiplicacao)

print("Divisão:", divisao)

print("Divisão inteira:", divisao_inteira)

print("Resto da divisão:", resto)

print("Potenciação:", potencia)