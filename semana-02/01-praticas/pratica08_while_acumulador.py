# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 08 - While com contador e acumulador
# Arquivo: pratica08_while_acumulador.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Utilizar contador e acumulador dentro de um laço while.
#
# Conteúdos praticados:
# - while
# - contador
# - acumulador
# - soma
#
# Status: A executar
# =============================================================================


# ============================================================
# INICIALIZAÇÃO
# ============================================================

contador = 1
soma = 0


# ============================================================
# PROCESSAMENTO
# ============================================================

while contador <= 5:
    numero = float(input(f"Informe o {contador}º número: "))
    soma += numero
    contador += 1

media = soma / 5


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(f"Soma dos valores: {soma:.2f}")
print(f"Média dos valores: {media:.2f}")