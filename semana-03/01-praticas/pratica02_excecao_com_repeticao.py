# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 02 - Tratamento de exceção com repetição
# Arquivo: pratica02_excecao_com_repeticao.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Combinar tratamento de exceções com um laço de repetição para permitir
# novas tentativas quando ocorrer um erro.
#
# Conteúdos:
# - while
# - try
# - except
# - break
# - tratamento de exceções
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# REPETIÇÃO E TRATAMENTO DE EXCEÇÃO
# =============================================================================

while True:

    try:
        print("Informe dois números.")

        n1 = float(input("n1: "))
        n2 = float(input("n2: "))

        resultado = n1 / n2

        break

    except:
        print("Ocorreu um erro! Tente novamente.")


# =============================================================================
# RESULTADO
# =============================================================================

print(f"{n1} / {n2} = {resultado}")
