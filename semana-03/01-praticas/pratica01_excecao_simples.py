# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 01 - Tratamento simples de exceção
# Arquivo: pratica01_excecao_simples.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar o tratamento básico de erros utilizando as estruturas
# try e except.
#
# Conteúdos:
# - try
# - except
# - conversão para float
# - divisão
# - tratamento de exceções
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA E PROCESSAMENTO
# =============================================================================

try:
    print("Informe dois números.")

    n1 = float(input("n1: "))
    n2 = float(input("n2: "))

    resultado = n1 / n2

    print(f"{n1} / {n2} = {resultado}")

except:
    print("Ocorreu um erro.")