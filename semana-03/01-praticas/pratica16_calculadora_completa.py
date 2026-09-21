#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 16 - Calculadora modular completa
# Arquivo: pratica16_calculadora_completa.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Integrar funções, tratamento de exceções, variável global,
# decomposição de problemas e controle do programa em uma aplicação.
#
# Conteúdos:
# - modularização
# - decomposição de problemas
# - funções
# - tratamento de exceções
# - eval()
# - variável global
# - __name__
# - __main__
#
# Status: Em desenvolvimento
# =============================================================================


HISTORICO = ""


# =============================================================================
# FUNÇÃO DE CÁLCULO
# =============================================================================

def calcula(expressao):

    try:
        return eval(expressao)

    except:
        print("Expressão inválida!")
        return None


# =============================================================================
# FUNÇÃO DE HISTÓRICO
# =============================================================================

def historico(expressao, resultado):

    global HISTORICO

    if resultado is not None:
        HISTORICO += "\n\n" + expressao
        HISTORICO += "\n" + str(resultado)


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def principal():

    while True:

        print("Informe a expressão matemática")
        print("(h para histórico, s para sair)")

        expressao = input()

        if expressao.lower() == "s":
            break

        if expressao.lower() == "h":

            if HISTORICO == "":
                print("\nHistórico vazio.\n")

            else:
                print(HISTORICO)
                print()

        else:
            resultado = calcula(expressao)

            historico(expressao, resultado)

            print(resultado)
            print()


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    principal()