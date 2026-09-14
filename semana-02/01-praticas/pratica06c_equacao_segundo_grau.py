# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 06C - Equação de segundo grau
# Arquivo: pratica06c_equacao_segundo_grau.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Resolver uma equação do segundo grau no formato Ax² + Bx + C = 0,
# analisando o valor de delta e tratando as diferentes possibilidades.
#
# Conteúdos praticados:
# - input()
# - float()
# - if/elif/else
# - operadores aritméticos
# - cálculo de delta
# - raiz quadrada
# - import math
# - tomada de decisão
#
# Status: A executar
# =============================================================================


# ============================================================
# IMPORTAÇÃO
# ============================================================

import math


# ============================================================
# ENTRADA DE DADOS
# ============================================================

print("Equação do segundo grau: Ax² + Bx + C = 0")

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

if a == 0:
    print("Não é uma equação de segundo grau.")

else:
    delta = b ** 2 - 4 * a * c

    print(f"Delta: {delta:.2f}")

    if delta < 0:
        print("A equação não possui raízes reais.")

    elif delta == 0:
        x = -b / (2 * a)

        print("A equação possui uma única raiz real.")
        print(f"x = {x:.2f}")

    else:
        raiz_delta = math.sqrt(delta)

        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)

        print("A equação possui duas raízes reais.")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")