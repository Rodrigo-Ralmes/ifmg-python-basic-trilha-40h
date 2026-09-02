# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:03:24 2026

@author: Rodrigo
"""

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Exercício oficial
# Exercício: 02A - Conversão de segundos para horas, minutos e segundos
# Arquivo: ex02a_segundos_para_hms.py
# Autor: Rodrigo de Almeida Silveira
# Data: 02/09/2026 12:03:24
#
# Objetivo:
# Solicitar uma quantidade total de segundos e convertê-la em
# horas, minutos e segundos.
#
# Conteúdos praticados:
# - input()
# - int()
# - variáveis
# - divisão inteira
# - operador de resto
# - conversão de tempo
# - saída de dados
# - f-string
#
# Status: Concluído
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

total_segundos = int(input("Digite a quantidade total de segundos: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

horas = total_segundos // 3600
restante = total_segundos % 3600

minutos = restante // 60
segundos = restante % 60

# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("------------------------------------------------------------------------")
print("=== CONVERSÃO DE SEGUNDOS ===")
print(f"Total informado: {total_segundos} segundos")
print(f"Resultado: {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
print("------------------------------------------------------------------------")