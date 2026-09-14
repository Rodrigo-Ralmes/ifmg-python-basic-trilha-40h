# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 06B - Classificação de triângulos
# Arquivo: pratica06b_classificacao_triangulos.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Verificar se três lados podem formar um triângulo e, em caso positivo,
# classificá-lo como equilátero, isósceles ou escaleno.
#
# Conteúdos praticados:
# - input()
# - float()
# - if/elif/else
# - operadores relacionais
# - operadores lógicos and/or
# - validação de condições
# - classificação por regras
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

print("Informe os três lados do triângulo.")

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

# Regra de existência de um triângulo:
# cada lado deve ser menor que a soma dos outros dois.

if (
    lado1 >= lado2 + lado3
    or lado2 >= lado1 + lado3
    or lado3 >= lado1 + lado2
):
    classificacao = "Triângulo inválido"

else:
    if lado1 == lado2 and lado2 == lado3:
        classificacao = "Triângulo equilátero"

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        classificacao = "Triângulo isósceles"

    else:
        classificacao = "Triângulo escaleno"


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(classificacao)