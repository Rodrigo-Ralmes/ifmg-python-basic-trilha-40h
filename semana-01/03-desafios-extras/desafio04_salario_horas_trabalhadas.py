# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 04 - Salário por horas trabalhadas
# Arquivo: desafio04_salario_horas_trabalhadas.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Calcular o salário bruto com base na quantidade de horas
# trabalhadas e no valor recebido por hora.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - multiplicação
# - formatação monetária
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora: R$ "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

salario_bruto = horas_trabalhadas * valor_hora


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CÁLCULO DO SALÁRIO ===")
print(f"Horas trabalhadas: {horas_trabalhadas:.2f}")
print(f"Valor por hora: R$ {valor_hora:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")