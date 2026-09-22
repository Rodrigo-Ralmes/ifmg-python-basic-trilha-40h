# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 09 - Estatísticas de números
# Arquivo: desafio09_estatisticas_numeros.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar funções reutilizáveis para calcular estatísticas simples.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - decomposição de problemas
# =============================================================================


def calcular_media(a, b, c):
    return (a + b + c) / 3


def maior_numero(a, b, c):
    return max(a, b, c)


def menor_numero(a, b, c):
    return min(a, b, c)


def calcular_soma(a, b, c):
    return a + b + c


def principal():

    try:
        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))
        numero3 = float(input("Terceiro número: "))

        print("\nESTATÍSTICAS")

        print(
            f"Soma: "
            f"{calcular_soma(numero1, numero2, numero3):.2f}"
        )

        print(
            f"Média: "
            f"{calcular_media(numero1, numero2, numero3):.2f}"
        )

        print(
            f"Maior número: "
            f"{maior_numero(numero1, numero2, numero3):.2f}"
        )

        print(
            f"Menor número: "
            f"{menor_numero(numero1, numero2, numero3):.2f}"
        )

    except ValueError:
        print("\nErro: informe apenas números válidos.")


if __name__ == "__main__":
    principal()
