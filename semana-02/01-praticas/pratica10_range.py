# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 10 - Função range()
# Arquivo: pratica10_range.py
# Autor: Rodrigo Ralmes
# Data: 08/09/2026
#
# Objetivo:
# Explorar diferentes formas de utilização da função range() em laços for.
#
# Conteúdos praticados:
# - for
# - range(início, fim, passo)
# - sequências numéricas
#
# Status: A executar
# =============================================================================


# ============================================================
# RANGE COM UM ARGUMENTO
# ============================================================

print("range(5):")

for numero in range(5):
    print(numero)


# ============================================================
# RANGE COM INÍCIO E FIM
# ============================================================

print("\nrange(1, 6):")

for numero in range(1, 6):
    print(numero)


# ============================================================
# RANGE COM INÍCIO, FIM E PASSO
# ============================================================

print("\nrange(0, 11, 2):")

for numero in range(0, 11, 2):
    print(numero)