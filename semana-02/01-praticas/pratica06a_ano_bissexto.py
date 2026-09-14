# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 06A - Verificação de ano bissexto
# Arquivo: pratica06a_ano_bissexto.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Verificar se um determinado ano é bissexto utilizando estruturas de decisão,
# operadores relacionais, operadores lógicos e o operador de resto da divisão.
#
# Conteúdos praticados:
# - input()
# - int()
# - if/else
# - operadores relacionais
# - operadores lógicos and/or
# - operador de resto da divisão %
# - combinação de condições
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

ano = int(input("Informe o ano: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

# Um ano é bissexto quando:
# - é divisível por 400
# OU
# - é divisível por 4 e não é divisível por 100

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "Ano bissexto"
else:
    resultado = "Ano não bissexto"


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(resultado)