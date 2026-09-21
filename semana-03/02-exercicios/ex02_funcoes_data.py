# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Exercício
# Atividade: 02 - Funções para data
# Arquivo: ex02_funcoes_data.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Modularizar a verificação de ano bissexto e o cálculo da quantidade
# de dias de determinado mês.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - modularização
# - estruturas condicionais
#
# Status: Em desenvolvimento
# =============================================================================


def ano_bissexto(ano):

    if ano % 400 == 0:
        return True

    elif ano % 4 == 0 and ano % 100 != 0:
        return True

    else:
        return False


def dias_mes(ano, mes):

    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31

    elif mes in (4, 6, 9, 11):
        return 30

    elif mes == 2:

        if ano_bissexto(ano):
            return 29

        return 28

    return -1


def principal():

    print("Informe a data")

    ano = int(input("Ano: "))
    mes = int(input("Mês: "))

    print(f"Ano bissexto: {ano_bissexto(ano)}")

    quantidade_dias = dias_mes(ano, mes)

    if quantidade_dias == -1:
        print("Mês inválido.")

    else:
        print(f"Dias do mês: {quantidade_dias}")


if __name__ == "__main__":
    principal()
