# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 04.01 - Lista com enumerate() e contador progressivo
# Arquivo: pratica04_01_lista_enumerate.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Armazenar os preços de 10 produtos em uma lista, calcular o preço médio,
# identificar os produtos com preço acima da média utilizando enumerate()
# e demonstrar o funcionamento de um contador progressivo, exibindo a
# quantidade acumulada sempre que um novo produto acima da média é encontrado.
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
# - Contagem progressiva de elementos
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

        print(f"TOTAL: {qtde_acima_media}")
        print(f"Produto {indice}: R$ {preco:.2f}")