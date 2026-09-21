# -*- coding: utf-8 -*-

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40 horas
# Semana: 03
# Tipo: Desafio Extra
# Desafio: 01
# Arquivo: desafio01_divisao_segura.py
#
# Objetivo:
# Desenvolver um programa capaz de realizar uma divisão
# entre dois números utilizando tratamento de exceções.
#
# Conteúdos praticados:
# - Entrada de dados com input()
# - Conversão de dados com float()
# - Estrutura try/except
# - Tratamento de ValueError
# - Tratamento de ZeroDivisionError
# - Operações aritméticas
#
# Observação:
# Este desafio é complementar e autoral, criado para
# consolidação dos conteúdos estudados na Semana 03.
# ============================================================


# ============================================================
# ENTRADA, PROCESSAMENTO E TRATAMENTO DE EXCEÇÕES
# ============================================================

try:
    # Solicita o primeiro número.
    numero1 = float(input("Digite o primeiro número: "))

    # Solicita o segundo número.
    numero2 = float(input("Digite o segundo número: "))

    # Realiza a divisão.
    resultado = numero1 / numero2

    # Exibe o resultado caso nenhuma exceção tenha ocorrido.
    print("\nResultado da divisão:")
    print(f"{numero1} / {numero2} = {resultado}")


# ============================================================
# TRATAMENTO DE ENTRADA INVÁLIDA
# ============================================================

except ValueError:
    print("\nErro: digite apenas valores numéricos.")


# ============================================================
# TRATAMENTO DE DIVISÃO POR ZERO
# ============================================================

except ZeroDivisionError:
    print("\nErro: não é possível realizar divisão por zero.")


# ============================================================
# FINALIZAÇÃO
# ============================================================

print("\nPrograma finalizado.")