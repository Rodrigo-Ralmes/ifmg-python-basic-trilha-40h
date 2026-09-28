#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 01 - Média de preços sem lista
# Arquivo: pratica01_media_precos_sem_lista.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Calcular o preço médio de dez produtos sem utilizar uma coleção de dados,
# demonstrando a necessidade de armazenar valores quando eles precisam ser
# consultados novamente durante o processamento.
#
# Conteúdos:
# - variáveis
# - entrada de dados
# - conversão para float
# - estrutura de repetição for
# - acumulador
# - cálculo de média
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA E PROCESSAMENTO
# =============================================================================

soma = 0

print("Informe o preço dos produtos.")

for i in range(1, 11):
    preco = float(input(f"Produto {i}: R$ "))
    soma += preco


# =============================================================================
# CÁLCULO DA MÉDIA
# =============================================================================

media = soma / 10


# =============================================================================
# SAÍDA
# =============================================================================

print(f"\nPreço médio: R$ {media:.2f}")