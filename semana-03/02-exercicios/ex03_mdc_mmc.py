# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Exercício
# Atividade: 03 - MDC e MMC
# Arquivo: ex03_mdc_mmc.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar funções independentes para cálculo do máximo divisor comum
# e mínimo múltiplo comum.
#
# Conteúdos:
# - funções
# - modularização
# - algoritmo de Euclides
# - return
# - MDC
# - MMC
#
# Status: Em desenvolvimento
# =============================================================================


def mdc(n1, n2):

    while True:

        resto = n1 % n2

        if resto == 0:
            return n2

        n1 = n2
        n2 = resto


def mmc(n1, n2):
    return n1 * n2 // mdc(n1, n2)


def principal():

    print("Informe dois números inteiros:")

    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))

    print(f"MDC: {mdc(n1, n2)}")
    print(f"MMC: {mmc(n1, n2)}")


if __name__ == "__main__":
    principal()