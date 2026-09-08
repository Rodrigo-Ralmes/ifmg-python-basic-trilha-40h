# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 06 - Conversor de metros
# Arquivo: desafio06_conversor_metros.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Converter uma medida informada em metros para quilômetros,
# centímetros e milímetros.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - multiplicação
# - divisão
# - conversão de medidas
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

metros = float(input("Digite uma medida em metros: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

quilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CONVERSOR DE METROS ===")
print(f"Metros: {metros:.2f} m")
print(f"Quilômetros: {quilometros:.3f} km")
print(f"Centímetros: {centimetros:.2f} cm")
print(f"Milímetros: {milimetros:.2f} mm")

