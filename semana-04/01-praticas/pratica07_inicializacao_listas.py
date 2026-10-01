# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 07 - Inicialização de listas
# Arquivo: pratica07_inicializacao_listas.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar diferentes formas de inicializar listas em Python, utilizando
# a função range(), a função list() e o operador de repetição (*), permitindo
# criar listas previamente preenchidas para diferentes necessidades.
#
# Conteúdos:
# - Listas
# - Inicialização de listas
# - Função list()
# - Função range()
# - Operador de repetição *
# - Índices
# - Função len()
# - Estrutura de repetição for
# - Percurso de listas
# - Alteração de elementos
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO DE LISTA COM range()
# =============================================================================

lista_numeros = list(range(10))


# =============================================================================
# INICIALIZAÇÃO DE LISTA COM REPETIÇÃO
# =============================================================================

lista_zeros = [0] * 10


# =============================================================================
# SAÍDA DE DADOS - LISTAS INICIAIS
# =============================================================================

print("=" * 60)
print("INICIALIZAÇÃO DE LISTAS")
print("=" * 60)

print("\nLista criada com list(range(10)):")
print(lista_numeros)

print("\nLista criada com [0] * 10:")
print(lista_zeros)


# =============================================================================
# PERCORRENDO A LISTA POR ÍNDICES
# =============================================================================

print("\n" + "=" * 60)
print("ÍNDICES E VALORES DA LISTA")
print("=" * 60)

for indice in range(len(lista_numeros)):
    print(
        f"Índice {indice}: "
        f"{lista_numeros[indice]}"
    )


# =============================================================================
# ALTERAÇÃO DOS ELEMENTOS DA LISTA
# =============================================================================

for indice in range(len(lista_zeros)):
    lista_zeros[indice] = indice + 1


# =============================================================================
# SAÍDA DE DADOS - LISTA ALTERADA
# =============================================================================

print("\n" + "=" * 60)
print("LISTA APÓS ALTERAÇÃO DOS ELEMENTOS")
print("=" * 60)

print(lista_zeros)