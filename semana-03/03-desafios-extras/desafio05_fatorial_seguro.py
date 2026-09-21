# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 05 - Fatorial seguro com recursão
# Arquivo: desafio05_fatorial_seguro.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Calcular o fatorial de um número utilizando recursão.
#
# Conteúdos:
# - recursão
# - função
# - return
# - condição de parada
# - tratamento de exceções
# =============================================================================


def fatorial(numero):

    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


def principal():

    try:
        numero = int(input("Digite um número inteiro não negativo: "))

        if numero < 0:
            print("\nErro: o número deve ser maior ou igual a zero.")
            return

        resultado = fatorial(numero)

        print(f"\n{numero}! = {resultado}")

    except ValueError:
        print("\nErro: informe apenas números inteiros.")


if __name__ == "__main__":
    principal()