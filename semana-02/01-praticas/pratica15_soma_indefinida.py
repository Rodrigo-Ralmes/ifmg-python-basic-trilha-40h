# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 15 - Soma indefinida de números
# Arquivo: pratica15_soma_indefinida.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Somar uma quantidade indeterminada de números até que o usuário
# informe zero, utilizando while True e break.
#
# Conteúdos praticados:
# - while True
# - input()
# - float()
# - if
# - break
# - acumulador
#
# Referência:
# E-book Python Básico +IFMG - Figura 35
#
# Status: A executar
# =============================================================================


# ============================================================
# INICIALIZAÇÃO
# ============================================================

soma = 0


# ============================================================
# PROCESSAMENTO
# ============================================================

while True:
    n = float(input("Informe um número: "))

    if n == 0:
        break

    soma = soma + n


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print("Soma dos números:", soma)