# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 05 - Cálculo do fatorial
# Arquivo: ex05_fatorial.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Calcular o fatorial de um número inteiro utilizando um laço for.
#
# Conceito:
# n! = n × (n - 1) × (n - 2) × ... × 2 × 1
#
# Exemplos:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 1! = 1
# 0! = 1
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - passo negativo
# - acumulador
# - multiplicação
# - operador *=
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.3.5 - Exercícios
# Exercício B - Cálculo do fatorial.
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

n = int(input("Informe um número: "))


# ============================================================
# INICIALIZAÇÃO DO ACUMULADOR
# ============================================================

fat = 1


# ============================================================
# PROCESSAMENTO
# ============================================================

for cont in range(n, 1, -1):
    fat *= cont


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print("O fatorial de", n, "é", fat)

