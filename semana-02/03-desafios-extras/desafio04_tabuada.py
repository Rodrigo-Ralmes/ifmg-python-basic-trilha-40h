# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 04 - Tabuada
# Arquivo: desafio04_tabuada.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Solicitar um número inteiro e apresentar sua tabuada de multiplicação
# do número 1 até o número 10.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - multiplicação
# - repetição definida
# - f-string
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

numero = int(input("Informe um número para gerar a tabuada: "))


# =============================================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# =============================================================================

print(f"\nTabuada do {numero}:")

for multiplicador in range(1, 11):

    resultado = numero * multiplicador

    print(f"{numero} x {multiplicador} = {resultado}")