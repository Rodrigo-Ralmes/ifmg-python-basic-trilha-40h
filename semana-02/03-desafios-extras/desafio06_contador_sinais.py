# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 06 - Contador de sinais
# Arquivo: desafio06_contador_sinais.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Ler dez valores e contabilizar quantos são positivos, negativos e iguais
# a zero.
#
# Conteúdos praticados:
# - input()
# - float()
# - for
# - range()
# - if/elif/else
# - contadores
# - operadores relacionais
#
# Status: A executar
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

positivos = 0
negativos = 0
zeros = 0


# =============================================================================
# ENTRADA E PROCESSAMENTO
# =============================================================================

for contador in range(1, 11):

    numero = float(input(f"Informe o {contador}º número: "))

    if numero > 0:
        positivos += 1

    elif numero < 0:
        negativos += 1

    else:
        zeros += 1


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print("\nResultado:")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números iguais a zero: {zeros}")