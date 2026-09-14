# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 06 - Calculadora simples
# Arquivo: ex06_calculadora.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Desenvolver uma calculadora simples capaz de realizar operações
# de soma, subtração, multiplicação e divisão repetidamente até que
# o usuário escolha encerrar o programa.
#
# Conteúdos praticados:
# - while True
# - input()
# - float()
# - if
# - elif
# - else
# - break
# - continue
# - operadores aritméticos
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.3.5 - Exercícios
# Exercício C - Calculadora simples.
#
# Status: A executar
# =============================================================================


# ============================================================
# LAÇO PRINCIPAL
# ============================================================

while True:


# ============================================================
# MENU
# ============================================================

    print("Calculadora (+, -, *, /)")
    print("s: sair")


# ============================================================
# ENTRADA DA OPERAÇÃO
# ============================================================

    resp = input("Informe a operação desejada (s para sair): ")


# ============================================================
# VERIFICAÇÃO DE SAÍDA
# ============================================================

    if resp == "s":
        print("Você saiu da calculadora")
        break
        

# ============================================================
# ENTRADA DOS NÚMEROS
# ============================================================

    print("Informe dois números:")

    n1 = float(input("N1: "))
    n2 = float(input("N2: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

    if resp == "+":
        r = n1 + n2

    elif resp == "-":
        r = n1 - n2

    elif resp == "*":
        r = n1 * n2

    elif resp == "/":
        r = n1 / n2

    else:
        print("Operação inválida!")
        continue


# ============================================================
# SAÍDA DE DADOS
# ============================================================

    print("Resultado calculado: " , n1, resp, n2, "=", r)

