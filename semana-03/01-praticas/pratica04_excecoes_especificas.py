# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 04 - Tratamento de exceções específicas
# Arquivo: pratica04_excecoes_especificas.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Tratar individualmente diferentes tipos de exceções.
#
# Conteúdos:
# - ValueError
# - ZeroDivisionError
# - try
# - except
# - tratamento específico de erros
#
# Status: Em desenvolvimento
# =============================================================================


while True:

    try:
        print("Informe dois números.")

        n1 = float(input("n1: "))
        n2 = float(input("n2: "))

        resultado = n1 / n2

        break

    except ValueError as erro:
        print(erro)
        print("Número inválido! Tente novamente.")

    except ZeroDivisionError as erro:
        print(erro)
        print("Divisão por zero! Tente novamente.")


print(f"{n1} / {n2} = {resultado}")

