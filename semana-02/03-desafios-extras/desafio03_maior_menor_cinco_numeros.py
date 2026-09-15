# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 03 - Maior e menor de cinco números
# Arquivo: desafio03_maior_menor_cinco_numeros.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Ler cinco números informados pelo usuário e identificar o maior e o menor
# valor digitado.
#
# Conteúdos praticados:
# - input()
# - float()
# - for
# - range()
# - operadores relacionais
# - comparação de valores
# - atualização de variáveis
#
# Status: A executar
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

maior = None
menor = None


# =============================================================================
# ENTRADA E PROCESSAMENTO
# =============================================================================

for contador in range(1, 6):

    numero = float(input(f"Informe o {contador}º número: "))

    if maior is None:
        maior = numero
        menor = numero

    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"Maior número informado: {maior}")
print(f"Menor número informado: {menor}")