# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 15 - Função principal da calculadora
# Arquivo: pratica15_funcao_principal_calculadora.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar a função responsável por controlar o fluxo principal
# de uma calculadora de expressões.
#
# Conteúdos:
# - decomposição de problemas
# - função principal
# - while
# - comandos
# - funções auxiliares
#
# Status: Em desenvolvimento
# =============================================================================


HISTORICO = ""


def calcula(expressao):

    try:
        return eval(expressao)

    except:
        print("Expressão inválida!")
        return None


def historico(expressao, resultado):

    global HISTORICO

    if resultado is not None:
        HISTORICO += "\n\n" + expressao
        HISTORICO += "\n" + str(resultado)


def principal():

    while True:

        print("Informe a expressão matemática")
        print("(h para histórico, s para sair)")

        expressao = input()

        if expressao.lower() == "s":
            break

        if expressao.lower() == "h":
            print(HISTORICO)
            print()

        else:
            resultado = calcula(expressao)

            historico(expressao, resultado)

            print(resultado)
            print()


principal()