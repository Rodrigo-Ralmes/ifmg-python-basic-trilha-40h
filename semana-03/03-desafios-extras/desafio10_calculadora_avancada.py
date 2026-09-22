# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 10 - Calculadora avançada
# Arquivo: desafio10_calculadora_avancada.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Integrar modularização, funções, tratamento de exceções, menu,
# repetição, parâmetros e retorno em um único programa.
#
# Conteúdos:
# - funções
# - modularização
# - decomposição de problemas
# - try / except
# - while
# - parâmetros
# - return
# - histórico
# =============================================================================


HISTORICO = []


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def potencia(base, expoente):
    return base ** expoente


def registrar_historico(descricao):
    HISTORICO.append(descricao)


def exibir_historico():

    print("\nHISTÓRICO")

    if len(HISTORICO) == 0:
        print("Nenhuma operação realizada.")
        return

    for item in HISTORICO:
        print(item)


def exibir_menu():

    print("\nCALCULADORA AVANÇADA")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Histórico")
    print("0 - Sair")


def ler_numero(mensagem):

    while True:

        try:
            return float(input(mensagem))

        except ValueError:
            print("Valor inválido. Tente novamente.")


def principal():

    while True:

        exibir_menu()

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("\nCalculadora encerrada.")
            break

        if opcao == "6":
            exibir_historico()
            continue

        if opcao not in ("1", "2", "3", "4", "5"):
            print("\nOpção inválida.")
            continue

        numero1 = ler_numero("Primeiro número: ")
        numero2 = ler_numero("Segundo número: ")

        try:

            if opcao == "1":
                resultado = somar(numero1, numero2)
                operador = "+"

            elif opcao == "2":
                resultado = subtrair(numero1, numero2)
                operador = "-"

            elif opcao == "3":
                resultado = multiplicar(numero1, numero2)
                operador = "*"

            elif opcao == "4":
                resultado = dividir(numero1, numero2)
                operador = "/"

            else:
                resultado = potencia(numero1, numero2)
                operador = "**"

            descricao = (
                f"{numero1} {operador} {numero2} = {resultado}"
            )

            registrar_historico(descricao)

            print(f"\nResultado: {resultado}")

        except ZeroDivisionError:
            print("\nErro: não é possível dividir por zero.")


if __name__ == "__main__":
    principal()