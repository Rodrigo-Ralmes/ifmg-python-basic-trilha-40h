# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:03:33 2026

@author: Rodrigo
"""
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 01 - Média de duas notas
# Arquivo: desafio01_media_duas_notas.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026 11:03:33
#
# Objetivo:
# Solicitar duas notas, calcular a média aritmética e apresentar
# o resultado com duas casas decimais.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - operadores aritméticos
# - saída formatada
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = (nota1 + nota2) / 2


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== MÉDIA DAS NOTAS ===")
print(f"Primeira nota: {nota1:.2f}")
print(f"Segunda nota: {nota2:.2f}")
print(f"Média: {media:.2f}")
print()
