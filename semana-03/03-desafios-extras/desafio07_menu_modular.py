# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 07 - Menu modular
# Arquivo: desafio07_menu_modular.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Decompor um programa em pequenas funções responsáveis por cada tarefa.
#
# Conteúdos:
# - modularização
# - decomposição de problemas
# - funções
# - menu
# - while
# =============================================================================


def exibir_menu():

    print("\nMENU")
    print("1 - Exibir mensagem")
    print("2 - Dobrar número")
    print("3 - Verificar par ou ímpar")
    print("0 - Sair")


def exibir_mensagem():
    print("\nPython Básico - Semana 03")


def dobrar_numero():

    try:
        numero = float(input("Digite um número: "))

        print(f"Dobro: {numero * 2}")

    except ValueError:
        print("Valor inválido.")


def verificar_par_impar():

    try:
        numero = int(input("Digite um número inteiro: "))

        if numero % 2 == 0:
            print("O número é par.")

        else:
            print("O número é ímpar.")

    except ValueError:
        print("Valor inválido.")


def principal():

    while True:

        exibir_menu()

        opcao = input("Escolha: ")

        if opcao == "1":
            exibir_mensagem()

        elif opcao == "2":
            dobrar_numero()

        elif opcao == "3":
            verificar_par_impar()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    principal()
