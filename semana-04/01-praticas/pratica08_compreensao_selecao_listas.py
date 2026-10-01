# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 08 - Compreensão e seleção de listas
# Arquivo: pratica08_compreensao_selecao_listas.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar diferentes formas de criação, conversão, seleção e consulta
# de elementos em listas, utilizando compreensão de listas, split(),
# fatiamento, len() e os operadores in e not in.
#
# Conteúdos:
# - Listas
# - Compreensão de listas
# - List comprehension
# - Função range()
# - Função input()
# - Método split()
# - Conversão para int
# - Função len()
# - Índices
# - Fatiamento de listas
# - Operador :
# - Operador in
# - Operador not in
# - Seleção de elementos
# - Consulta de elementos
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# CRIAÇÃO DE LISTA COM COMPREENSÃO
# =============================================================================

quadrados = [numero ** 2 for numero in range(1, 11)]


# =============================================================================
# SAÍDA - LIST COMPREHENSION
# =============================================================================

print("=" * 60)
print("COMPREENSÃO DE LISTAS")
print("=" * 60)

print("\nNúmeros ao quadrado de 1 a 10:")
print(quadrados)


# =============================================================================
# ENTRADA DE DADOS COM split()
# =============================================================================

print("\n" + "=" * 60)
print("CONVERSÃO DE TEXTO PARA LISTA DE NÚMEROS")
print("=" * 60)

entrada = input(
    "\nInforme números inteiros separados por espaço: "
)


# =============================================================================
# CONVERSÃO DOS DADOS
# =============================================================================

numeros = [
    int(valor)
    for valor in entrada.split()
]


# =============================================================================
# SAÍDA - LISTA CONVERTIDA
# =============================================================================

print("\nLista criada:")
print(numeros)

print(
    f"\nQuantidade de elementos: "
    f"{len(numeros)}"
)


# =============================================================================
# FATIAMENTO DE LISTAS
# =============================================================================

print("\n" + "=" * 60)
print("FATIAMENTO DE LISTAS")
print("=" * 60)

print("\nLista completa:")
print(numeros[:])

print("\nLista a partir do segundo elemento:")
print(numeros[1:])

print("\nLista sem o último elemento:")
print(numeros[:-1])

print("\nElementos dos índices 3 até 6:")
print(numeros[3:7])


# =============================================================================
# CONSULTA DE ELEMENTOS COM in E not in
# =============================================================================

print("\n" + "=" * 60)
print("CONSULTA DE ELEMENTOS")
print("=" * 60)

valor_consulta = int(
    input("\nInforme um número para pesquisar na lista: ")
)

if valor_consulta in numeros:
    print(
        f"\nO número {valor_consulta} "
        f"PERTENCE à lista."
    )
else:
    print(
        f"\nO número {valor_consulta} "
        f"NÃO pertence à lista."
    )


# =============================================================================
# DEMONSTRAÇÃO DO OPERADOR not in
# =============================================================================

if valor_consulta not in numeros:
    print(
        f"O operador 'not in' confirmou que "
        f"{valor_consulta} não está presente."
    )
else:
    print(
        f"O operador 'not in' confirmou que "
        f"{valor_consulta} está presente."
    )

