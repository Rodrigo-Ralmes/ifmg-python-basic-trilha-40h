# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 05 - Soma dos pares de um intervalo
# Arquivo: desafio05_soma_pares_intervalo.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Percorrer um intervalo informado pelo usuário, identificar os números pares
# e calcular a soma desses valores.
#
# Conteúdos praticados:
# - input()
# - int()
# - for
# - range()
# - if
# - operador %
# - acumulador
# - soma
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

inicio = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o fim do intervalo: "))


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

soma = 0


# =============================================================================
# PROCESSAMENTO
# =============================================================================

for numero in range(inicio, fim + 1):

    if numero % 2 == 0:
        soma += numero


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"Soma dos números pares entre {inicio} e {fim}: {soma}")

