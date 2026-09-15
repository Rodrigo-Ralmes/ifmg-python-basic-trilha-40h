# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 10 - Número primo
# Arquivo: desafio10_numero_primo.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Verificar se um número inteiro informado pelo usuário é primo.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - if/else
# - operador %
# - variável booleana
# - break
# - divisibilidade
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

numero = int(input("Informe um número inteiro: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

if numero < 2:

    primo = False

else:

    primo = True

    for divisor in range(2, numero):

        if numero % divisor == 0:
            primo = False
            break


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

if primo:
    print(f"{numero} é um número primo.")

else:
    print(f"{numero} não é um número primo.")