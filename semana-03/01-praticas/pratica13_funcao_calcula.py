# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 13 - Função de cálculo de expressão
# Arquivo: pratica13_funcao_calcula.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar uma função responsável por calcular uma expressão e tratar
# possíveis erros.
#
# Conteúdos:
# - decomposição de problemas
# - funções
# - eval()
# - try
# - except
# - None
#
# Status: Em desenvolvimento
# =============================================================================


def calcula(expressao):

    try:
        return eval(expressao)

    except:
        print("Expressão inválida!")
        return None


expressao = input("Informe uma expressão matemática: ")

resultado = calcula(expressao)

print(f"Resultado: {resultado}")