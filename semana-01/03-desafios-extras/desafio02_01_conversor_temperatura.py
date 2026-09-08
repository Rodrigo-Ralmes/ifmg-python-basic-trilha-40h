# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra ampliado
# Desafio: 02.01 - Conversor de temperatura bidirecional
# Arquivo: desafio02_01_conversor_temperatura.py
# Autor: Rodrigo de Almeida Silveira
# Data: 08/09/2026
#
# Objetivo:
# Permitir que o usuário escolha entre converter uma temperatura
# de Celsius para Fahrenheit ou de Fahrenheit para Celsius.
#
# Conteúdos praticados:
# - input()
# - int()
# - float()
# - variáveis
# - operadores aritméticos
# - estruturas condicionais
# - if, elif e else
# - conversão de temperatura
# - saída formatada
# - f-string
#
# Status: Concluído
# =============================================================================


# =============================================================================
# APRESENTAÇÃO DAS OPÇÕES
# =============================================================================

print("=== CONVERSOR DE TEMPERATURA ===")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
print("-------------------------------------------------------------------")


# =============================================================================
# ENTRADA DA OPÇÃO
# =============================================================================

opcao = int(input("Escolha a opção de conversão: "))

print("-------------------------------------------------------------------")


# =============================================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# =============================================================================

if opcao == 1:
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print()
    print("=== CELSIUS PARA FAHRENHEIT ===")
    print(f"Temperatura em Celsius: {celsius:.2f} °C")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")

elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

    celsius = (fahrenheit - 32) / 1.8

    print()
    print("=== FAHRENHEIT PARA CELSIUS ===")
    print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura em Celsius: {celsius:.2f} °C")

else:
    print("Opção inválida! Digite somente 1 ou 2.")

print("-------------------------------------------------------------------")