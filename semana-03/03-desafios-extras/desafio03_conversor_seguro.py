# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 03 - Conversor seguro de temperatura
# Arquivo: desafio03_conversor_seguro.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar um conversor de temperatura utilizando funções e validação.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - tratamento de exceções
# - estruturas condicionais
# =============================================================================


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def principal():

    print("CONVERSOR DE TEMPERATURA")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            celsius = float(input("Temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)

            print(f"\n{celsius:.2f} °C = {resultado:.2f} °F")

        elif opcao == 2:
            fahrenheit = float(input("Temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)

            print(f"\n{fahrenheit:.2f} °F = {resultado:.2f} °C")

        else:
            print("\nOpção inválida.")

    except ValueError:
        print("\nErro: informe valores válidos.")


if __name__ == "__main__":
    principal()