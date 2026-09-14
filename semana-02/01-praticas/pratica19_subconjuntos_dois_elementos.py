# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 19 - Subconjuntos com dois elementos
# Arquivo: pratica19_subconjuntos_dois_elementos.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Gerar todos os subconjuntos possíveis contendo dois elementos
# diferentes de um conjunto de números naturais.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - laços aninhados
# - definição dos limites do range()
# - end
# - sep
#
# Referência:
# E-book Python Básico +IFMG - Figura 39
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
# GERAÇÃO DOS SUBCONJUNTOS
# ============================================================

print("\nSubconjuntos:", end="")

for cont in range(1, n + 1):

    for cont2 in range(cont + 1, n + 1):

        print(
            "{",
            cont,
            ", ",
            cont2,
            "}",
            sep="",
            end=" "
        )