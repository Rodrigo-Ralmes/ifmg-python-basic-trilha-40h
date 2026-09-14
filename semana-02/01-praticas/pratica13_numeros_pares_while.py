# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 13 - Listagem de números pares com while
# Arquivo: pratica13_numeros_pares_while.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Utilizar o laço de repetição while para listar números pares
# menores que um limite informado pelo usuário.
#
# Conteúdos praticados:
# - input()
# - int()
# - while
# - contador
# - incremento
# - condição de parada
#
# Referência:
# E-book Python Básico +IFMG - Figura 33
#
# Status: A executar
# =============================================================================


# ============================================================
# INICIALIZAÇÃO
# ============================================================

atual = 0


# ============================================================
# ENTRADA DE DADOS
# ============================================================

n = int(input("Informe um número: "))


# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

while atual < n:
    print(atual)
    atual += 2