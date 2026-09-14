# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 04 - Maior e menor de uma sequência
# Arquivo: ex04_maior_menor_sequencia.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Ler uma quantidade indeterminada de números e identificar
# o maior e o menor valor informado.
#
# Conteúdos praticados:
# - float("-inf")
# - float("inf")
# - while True
# - input()
# - float()
# - if
# - break
# - lower()
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.3.5 - Exercícios
# Exercício A - Maior e menor número de uma sequência.
#
# Status: A executar
# =============================================================================


# ============================================================
# INICIALIZAÇÃO
# ============================================================

maior = float("-inf") # -∞, qualquer número pode ser maior 
menor = float("inf")  # +∞, qualquer número pode ser menor


# ============================================================
# REPETIÇÃO
# ============================================================

while True:

    n = float(input("Informe um número: "))


# ============================================================
# VERIFICAÇÃO DO MAIOR VALOR
# ============================================================

    if n > maior:
        maior = n


# ============================================================
# VERIFICAÇÃO DO MENOR VALOR
# ============================================================

    if n < menor:
        menor = n


# ============================================================
# CONTROLE DA REPETIÇÃO
# ============================================================

    resp = input("Deseja continuar? (S/N): ")

    if resp.lower() == "n":
        break


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print("Maior número informado:", maior)
print("Menor número informado:", menor)
