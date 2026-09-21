# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 04 - Calculadora com funções
# Arquivo: desafio04_calculadora_funcoes.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar uma calculadora modular utilizando funções independentes.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - tratamento de exceções
# =============================================================================


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def principal():

    print("CALCULADORA")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    try:
        opcao = int(input("\nEscolha uma operação: "))

        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))

        if opcao == 1:
            resultado = somar(numero1, numero2)

        elif opcao == 2:
            resultado = subtrair(numero1, numero2)

        elif opcao == 3:
            resultado = multiplicar(numero1, numero2)

        elif opcao == 4:
            resultado = dividir(numero1, numero2)

        else:
            print("\nOpção inválida.")
            return

        print(f"\nResultado: {resultado}")

    except ValueError:
        print("\nErro: informe valores numéricos válidos.")

    except ZeroDivisionError:
        print("\nErro: divisão por zero não permitida.")


if __name__ == "__main__":
    principal()