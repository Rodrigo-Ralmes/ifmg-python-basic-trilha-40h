# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 09 - Sequência de Fibonacci
# Arquivo: desafio09_fibonacci.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Gerar uma quantidade determinada de termos da sequência de Fibonacci.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - variáveis auxiliares
# - atualização de valores
# - sequência numérica
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

quantidade = int(input("Informe a quantidade de termos da sequência: "))


# =============================================================================
# VALIDAÇÃO
# =============================================================================

if quantidade <= 0:

    print("A quantidade deve ser maior que zero.")

else:

    # =========================================================================
    # INICIALIZAÇÃO
    # =========================================================================

    primeiro = 0
    segundo = 1


    # =========================================================================
    # PROCESSAMENTO E SAÍDA DE DADOS
    # =========================================================================

    print("Sequência de Fibonacci:")

    for contador in range(quantidade):

        print(primeiro, end=" ")

        proximo = primeiro + segundo
        primeiro = segundo
        segundo = proximo

    print()