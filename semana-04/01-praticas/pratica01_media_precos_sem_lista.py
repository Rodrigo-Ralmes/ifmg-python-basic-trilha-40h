# -*- coding: utf-8 -*-

"""
SEMANA 04 - PRÁTICA 01
Tema: necessidade de coleções de dados

Objetivo:
Ler o preço de 10 produtos, calcular a média e perceber que,
sem armazenar os preços, não conseguimos revisitar os valores
de forma eficiente.
"""

soma = 0

print("Informe o preço de 10 produtos:")

for i in range(1, 11):
    preco = float(input(f"Produto {i}: R$ "))
    soma += preco

media = soma / 10

print(f"\nPreço médio: R$ {media:.2f}")