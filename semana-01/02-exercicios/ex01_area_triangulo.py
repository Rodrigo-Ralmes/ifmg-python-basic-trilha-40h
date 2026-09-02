# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 08:32:52 2026

@author: Rodrigo
"""
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Exercício oficial
# Exercício: 01 - Área de um triângulo
# Arquivo: ex01_area_triangulo.py
# Autor: Rodrigo de Almeida Silveira
# Data: 02/09/2026 08:32:52
#
# Objetivo:
# Solicitar a base e a altura de um triângulo, calcular sua área
# e apresentar o resultado.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - operadores aritméticos
# - cálculo de área
# - saída de dados
# - f-string
#
# Status: Concluído
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

area = (base * altura) / 2


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== ÁREA DO TRIÂNGULO ===")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área do triângulo: {area:.2f}")