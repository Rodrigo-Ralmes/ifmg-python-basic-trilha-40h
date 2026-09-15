# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 08 - Calculadora com menu
# Arquivo: desafio08_calculadora_menu.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Desenvolver uma calculadora simples utilizando um menu de operações
# executado repetidamente até que o usuário escolha a opção de sair.
#
# Conteúdos praticados:
# - while True
# - input()
# - float()
# - if/elif/else
# - break
# - continue
# - operadores aritméticos
# - validação de opção
#
# Status: A executar
# =============================================================================


# =============================================================================
# PROCESSAMENTO
# =============================================================================

while True:

    print("\nCALCULADORA")
    print("+  Adição")
    print("-  Subtração")
    print("*  Multiplicação")
    print("/  Divisão")
    print("S  Sair")

    operacao = input("\nInforme a operação desejada: ").strip().lower()

    if operacao == "s":
        print("Calculadora encerrada.")
        break

    if operacao not in ["+", "-", "*", "/"]:
        print("Operação inválida.")
        continue

    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "*":
        resultado = numero1 * numero2

    else:

        if numero2 == 0:
            print("Não é possível realizar divisão por zero.")
            continue

        resultado = numero1 / numero2


    # =========================================================================
    # SAÍDA DE DADOS
    # =========================================================================

    print(f"Resultado: {resultado:.2f}")