# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 16 - Soma indefinida exceto números negativos
# Arquivo: pratica16_soma_indefinida_sem_negativos.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Somar uma quantidade indeterminada de números, ignorando valores
# negativos e encerrando o processamento quando for informado zero.
#
# Conteúdos praticados:
# - while True
# - if
# - continue
# - break
# - acumulador
# - entrada de dados
#
# Referência:
# E-book Python Básico +IFMG - Figura 36
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

    if n < 0:
        continue

    if n == 0:
        break

    soma = soma + n


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print("Soma dos números:", soma)