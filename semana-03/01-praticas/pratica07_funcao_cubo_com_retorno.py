# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 07 - Função cubo com retorno
# Arquivo: pratica07_funcao_cubo_com_retorno.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Utilizar return para devolver o resultado produzido por uma função.
#
# Conteúdos:
# - def
# - parâmetros
# - return
# - composição de funções
#
# Status: Em desenvolvimento
# =============================================================================


def cubo(numero):
    return numero * numero * numero


numero = float(input("Informe um número: "))

print(f"{numero} ao cubo é {cubo(numero)}")
print(f"{numero} elevado à nona é {cubo(cubo(numero))}")