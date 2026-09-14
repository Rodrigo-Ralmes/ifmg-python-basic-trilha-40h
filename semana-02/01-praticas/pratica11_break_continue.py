# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 11 - break e continue
# Arquivo: pratica11_break_continue.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Compreender a interrupção e a continuação de laços de repetição.
#
# Conteúdos praticados:
# - for
# - break
# - continue
#
# Status: A executar
# =============================================================================


# ============================================================
# EXEMPLO COM CONTINUE
# ============================================================

print("Números de 1 a 10, exceto o número 5:")

for numero in range(1, 11):
    if numero == 5:
        continue

    print(numero)


# ============================================================
# EXEMPLO COM BREAK
# ============================================================

print("\nContagem interrompida ao chegar em 6:")

for numero in range(1, 11):
    if numero == 6:
        break

    print(numero)