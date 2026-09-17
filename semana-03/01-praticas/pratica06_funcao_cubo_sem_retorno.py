# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 06 - Função cubo sem retorno
# Arquivo: pratica06_funcao_cubo_sem_retorno.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar a passagem de parâmetros para uma função que apresenta
# diretamente o resultado na tela.
#
# Conteúdos:
# - funções
# - parâmetros
# - variáveis locais
# - chamada de função
#
# Status: Em desenvolvimento
# =============================================================================


def calcula_cubo(numero):
    cubo = numero * numero * numero
    print(f"{numero} ao cubo é {cubo}")


numero = float(input("Informe um número: "))

calcula_cubo(numero)