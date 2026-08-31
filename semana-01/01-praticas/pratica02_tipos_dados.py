# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:37:59 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 02 - Tipos básicos de dados
# Arquivo: pratica02_tipos_dados.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 15:37:59
#
# Objetivo:
# Conhecer e experimentar os quatro tipos básicos de dados
# apresentados na Semana 1: int, float, bool e str.
#
# Conteúdos praticados:
# - int
# - float
# - bool
# - str
# - type()
# - variáveis
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# CRIAÇÃO DOS DADOS
# ============================================================

numero_inteiro = 10

numero_decimal = 3.14

valor_logico = True

texto = "Python Básico"


# ============================================================
# EXIBIÇÃO DOS VALORES
# ============================================================

print("Número inteiro:", numero_inteiro)

print("Número decimal:", numero_decimal)

print("Valor lógico:", valor_logico)

print("Texto:", texto)


# ============================================================
# DESCOBRINDO OS TIPOS
# ============================================================

print("Tipo de numero_inteiro:", type(numero_inteiro))

print("Tipo de numero_decimal:", type(numero_decimal))

print("Tipo de valor_logico:", type(valor_logico))

print("Tipo de texto:", type(texto))