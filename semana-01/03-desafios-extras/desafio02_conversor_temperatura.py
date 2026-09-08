# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 02 - Conversor de temperatura
# Arquivo: desafio02_conversor_temperatura.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Converter uma temperatura informada em graus Celsius para
# graus Fahrenheit.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - operadores aritméticos
# - conversão de temperatura
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

celsius = float(input("Digite a temperatura em graus Celsius: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

fahrenheit = (celsius * 9 / 5) + 32


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CONVERSOR DE TEMPERATURA ===")
print(f"Temperatura em Celsius: {celsius:.2f} °C")
print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")