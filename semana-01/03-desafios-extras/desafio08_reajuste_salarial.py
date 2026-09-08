# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 08 - Reajuste salarial
# Arquivo: desafio08_reajuste_salarial.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Calcular o valor do reajuste e o novo salário de um trabalhador.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - porcentagem
# - operadores aritméticos
# - formatação monetária
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

salario_atual = float(input("Digite o salário atual: R$ "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

valor_reajuste = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + valor_reajuste


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== REAJUSTE SALARIAL ===")
print(f"Salário atual: R$ {salario_atual:.2f}")
print(f"Percentual de reajuste: {percentual_reajuste:.2f}%")
print(f"Valor do reajuste: R$ {valor_reajuste:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")