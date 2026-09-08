# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 03 - Calculadora de IMC
# Arquivo: desafio03_calculadora_imc.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Solicitar o peso e a altura de uma pessoa, calcular o Índice
# de Massa Corporal e apresentar o resultado.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - exponenciação
# - divisão
# - saída formatada
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

peso = float(input("Digite o peso em quilogramas: "))
altura = float(input("Digite a altura em metros: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

imc = peso / (altura ** 2)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CALCULADORA DE IMC ===")
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")