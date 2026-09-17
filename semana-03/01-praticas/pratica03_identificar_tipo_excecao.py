# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 03 - Identificação do tipo de exceção
# Arquivo: pratica03_identificar_tipo_excecao.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Identificar a classe da exceção gerada durante a execução utilizando
# Exception e type().
#
# Conteúdos:
# - Exception
# - type()
# - try
# - except
# - classes de exceção
#
# Status: Em desenvolvimento
# =============================================================================


while True:

    try:
        print("Informe dois números.")

        n1 = float(input("n1: "))
        n2 = float(input("n2: "))

        resultado = n1 / n2

        break

    except Exception as erro:
        print("Ocorreu o seguinte tipo de erro:")
        print(type(erro))


print(f"{n1} / {n2} = {resultado}")