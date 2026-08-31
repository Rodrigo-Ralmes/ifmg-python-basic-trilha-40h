# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:10:48 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 03 - Variáveis
# Arquivo: pratica03_variaveis.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 17:10:48
#
# Objetivo:
# Praticar a criação, atribuição e utilização de variáveis,
# além de observar que Python diferencia letras maiúsculas
# e minúsculas.
#
# Conteúdos praticados:
# - variáveis
# - atribuição com =
# - nomes de variáveis
# - case sensitive
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# CRIAÇÃO DE VARIÁVEIS
# ============================================================

nome = "Rodrigo"

idade = 47

altura = 1.75

estudando_python = True


# ============================================================
# EXIBINDO AS VARIÁVEIS
# ============================================================

print("Nome:", nome)

print("Idade:", idade)

print("Altura:", altura)

print("Está estudando Python:", estudando_python)


# ============================================================
# ALTERAÇÃO DO VALOR DE UMA VARIÁVEL
# ============================================================

idade = 48

print("Nova idade armazenada:", idade)


# ============================================================
# CASE SENSITIVE
# ============================================================

nome = "Rodrigo"

Nome = "Python"

print("Variável nome:", nome)

print("Variável Nome:", Nome)