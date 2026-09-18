# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 14 - Função de histórico
# Arquivo: pratica14_funcao_historico.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar a utilização de variável global para armazenar
# resultados válidos.
#
# Conteúdos:
# - função
# - variável global
# - global
# - None
# - concatenação de strings
#
# Status: Em desenvolvimento
# =============================================================================


HISTORICO = ""


def historico(expressao, resultado):

    global HISTORICO

    if resultado is not None:
        HISTORICO += "\n\n" + expressao
        HISTORICO += "\n" + str(resultado)


historico("10 + 5", 15)

print(HISTORICO)