# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 03 - Cálculo do imposto de renda
# Arquivo: ex03_imposto_renda.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Calcular o imposto de renda de um salário com base nas faixas
# e alíquotas definidas no exercício do material didático.
#
# Conteúdos praticados:
# - input()
# - float()
# - if
# - elif
# - else
# - operadores relacionais
# - cálculo de porcentagem
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.2.5 - Exercícios
# Exercício C - Calcular o imposto de renda de um salário.
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

salario = float(input("Informe o salário: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

if salario <= 1903.98:
    imposto = 0

elif salario <= 2826.65:
    imposto = salario * 7.5 / 100

elif salario <= 3751.05:
    imposto = salario * 15 / 100

elif salario <= 4664.68:
    imposto = salario * 22.5 / 100

else:
    imposto = salario * 27.5 / 100


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print("O imposto de renda é", imposto)