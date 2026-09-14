# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 02 - Par ou ímpar sem operador %
# Arquivo: ex02_par_impar_sem_modulo.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Verificar se um número inteiro é par ou ímpar sem utilizar
# o operador de resto da divisão (%).
#
# Conteúdos praticados:
# - input()
# - int()
# - divisão inteira //
# - multiplicação
# - subtração
# - if
# - else
# - operadores relacionais
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.2.5 - Exercícios
# Exercício B - Testar se um número é ímpar ou par, sem usar o operador %.
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

n = int(input("Informe um número: "))


# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

if n // 2 * 2 - n == 0:
    print("O número é par!")

else:
    print("O número é ímpar")