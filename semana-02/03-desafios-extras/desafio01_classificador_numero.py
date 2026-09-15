# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 01 - Classificador de número
# Arquivo: desafio01_classificador_numero.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Classificar um número inteiro como positivo, negativo ou zero e,
# quando diferente de zero, identificar também se o número é par ou ímpar.
#
# Conteúdos praticados:
# - input()
# - int()
# - if/elif/else
# - estrutura condicional aninhada
# - operadores relacionais
# - operador de resto %
# - comparação de valores
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

numero = int(input("Informe um número inteiro: "))


# =============================================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# =============================================================================

if numero > 0:
    print("O número é positivo.")

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

elif numero < 0:
    print("O número é negativo.")

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

else:
    print("O número é zero.")