# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Exercício
# Atividade: 01 - Função input_int()
# Arquivo: ex01_input_int.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar uma função de entrada que somente aceite números inteiros válidos.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - try
# - except
# - validação de entrada
#
# Status: Em desenvolvimento
# =============================================================================


def input_int(mensagem):

    while True:

        try:
            return int(input(mensagem))

        except ValueError:
            print("Número inválido! Tente novamente.")


numero = input_int("Informe um número inteiro: ")

print(f"Número informado: {numero}")