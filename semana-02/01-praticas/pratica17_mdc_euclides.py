# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 17 - Cálculo do MDC pelo algoritmo de Euclides
# Arquivo: pratica17_mdc_euclides.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Calcular o Máximo Divisor Comum entre dois números utilizando
# o algoritmo de Euclides e um laço de repetição.
#
# Conteúdos praticados:
# - input()
# - int()
# - if/else
# - while True
# - operador %
# - break
# - algoritmo de Euclides
#
# Referência:
# E-book Python Básico +IFMG - Figura 37
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

print("Informe dois números")

n1 = int(input("N1: "))
n2 = int(input("N2: "))


# ============================================================
# VALIDAÇÃO E PROCESSAMENTO
# ============================================================

if n1 < 1 or n2 < 1:
    print("Números inválidos para MDC")

else:

    while True:
        resto = n1 % n2

        print(n1, "/", n2, "-> resto:", resto)

        if resto == 0:
            break

        n1 = n2
        n2 = resto


# ============================================================
# SAÍDA DE DADOS
# ============================================================

    print("O MDC é", n2)