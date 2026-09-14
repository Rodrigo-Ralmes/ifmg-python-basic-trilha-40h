# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício 01 - Maior entre três números
# Arquivo: ex01_maior_de_tres.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Receber três números inteiros e informar qual deles possui o maior valor.
#
# Conteúdos praticados:
# - input()
# - int()
# - if
# - elif
# - else
# - operadores relacionais
# - operador lógico and
#
# Referência:
# E-book Python Básico +IFMG
# Seção 2.2.5 - Exercícios
# Exercício A - Receber três números e informar o maior deles.
#
# Status: A executar
# =============================================================================


# ============================================================
# APRESENTAÇÃO
# ============================================================

print("Informe três números")


# ============================================================
# ENTRADA DE DADOS
# ============================================================

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))


# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

if (a > b) and (a > c):
    print("O maior número é", a)

elif b > c:
    print("O maior número é", b)

else:
    print("O maior número é", c)