# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:29:38 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 04 - Entrada e saída de dados
# Arquivo: pratica04_input_output.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 17:29:38
#
# Objetivo:
# Praticar a entrada de dados com input(), conversões
# de tipos e saída de informações com print().
#
# Conteúdos praticados:
# - input()
# - print()
# - str
# - int()
# - float()
# - conversão de dados
#
# Status: Prática
# ============================================================


print("=== CADASTRO SIMPLES ===")


# ============================================================
# ENTRADA DE DADOS
# ============================================================

nome = input("Informe seu nome: ")

idade = int(input("Informe sua idade: "))

altura = float(input("Informe sua altura: "))


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print()

print("=== DADOS INFORMADOS ===")

print("Nome:", nome)

print("Idade:", idade)

print("Altura:", altura)


# ============================================================
# VERIFICAÇÃO DOS TIPOS
# ============================================================

print()

print("Tipo da variável nome:", type(nome))

print("Tipo da variável idade:", type(idade))

print("Tipo da variável altura:", type(altura))