# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 09 - Recursão e cálculo do fatorial
# Arquivo: pratica09_recursao_fatorial.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar recursão por meio de uma função que calcula o fatorial
# de um número inteiro.
#
# Conteúdos:
# - recursão
# - condição de parada
# - funções
# - return
#
# Status: Em desenvolvimento
# =============================================================================


def fatorial(numero):

    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


numero = int(input("Informe um número: "))

print(f"O fatorial de {numero} é {fatorial(numero)}")