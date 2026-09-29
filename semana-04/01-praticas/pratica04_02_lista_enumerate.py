# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 04.02 - Lista com enumerate() e total final
# Arquivo: pratica04_02_lista_enumerate.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de 10 produtos em uma lista, calcular o preço médio,
# identificar os produtos com preço acima da média utilizando enumerate()
# e apresentar, ao final do percurso, a quantidade total de produtos que
# possuem preço acima da média.
#
# Conteúdos:
# - Listas
# - Criação de lista vazia
# - Método append()
# - Estrutura de repetição for
# - Função range()
# - Função len()
# - Função enumerate()
# - Índices de listas
# - Percurso de listas
# - Cálculo de média
# - Contador
# - Incremento com +=
# - Estrutura condicional if
# - Contagem de elementos
# - Exibição do total após o laço
#
# Status: Concluído
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

precos = []


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("Informe o preço de 10 produtos:")

for i in range(1, 11):
    preco = float(input(f"Produto {i}: R$ "))

    precos.append(preco)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = sum(precos) / len(precos)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"\nPreço médio: R$ {media:.2f}")

print("\nProdutos com preço acima da média:")

qtde_acima_media = 0

for indice, preco in enumerate(precos, start=1):
    if preco > media:
        qtde_acima_media += 1

        print(f"Produto {indice}: R$ {preco:.2f}")


print(f"\nTOTAL DE PRODUTOS ACIMA DA MÉDIA: {qtde_acima_media}")