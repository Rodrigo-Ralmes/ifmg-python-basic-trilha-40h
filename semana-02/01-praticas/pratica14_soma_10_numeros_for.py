# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 14 - Soma de 10 números usando for
# Arquivo: pratica14_soma_10_numeros_for.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Utilizar o laço for para receber dez números informados pelo usuário
# e acumular a soma desses valores.
#
# Conteúdos praticados:
# - input()
# - float()
# - for
# - range()
# - acumulador
# - operador +=
#
# Referência:
# E-book Python Básico +IFMG - Figura 34
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

for cont in range(10):
    n = float(input("Informe um número: "))
    soma += n


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(soma)
