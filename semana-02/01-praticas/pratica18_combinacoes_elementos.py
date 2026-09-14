# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 18 - Combinações de elementos
# Arquivo: pratica18_combinacoes_elementos.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Gerar combinações de dois elementos de um conjunto de números naturais
# utilizando dois laços for aninhados.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - laços aninhados
# - end
# - sep
#
# Referência:
# E-book Python Básico +IFMG - Figura 38
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

n = int(input("Informe o número de elementos do conjunto: "))


# ============================================================
# EXIBIÇÃO DOS ELEMENTOS
# ============================================================

print("Elementos:", end=" ")

for cont in range(1, n + 1):
    print(cont, end=" ")


# ============================================================
# COMBINAÇÕES
# ============================================================

print("\nCombinações:", end="")

for cont in range(1, n + 1):

    for cont2 in range(1, n + 1):

        print(
            "(",
            cont,
            ", ",
            cont2,
            ")",
            sep="",
            end=" "
        )