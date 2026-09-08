# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 10 - Cálculo da hipotenusa
# Arquivo: desafio10_hipotenusa.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Calcular a hipotenusa de um triângulo retângulo utilizando
# as medidas dos dois catetos.
#
# Conteúdos praticados:
# - import
# - módulo math
# - math.sqrt()
# - input()
# - float()
# - exponenciação
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# IMPORTAÇÃO
# =============================================================================

import math


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CÁLCULO DA HIPOTENUSA ===")
print(f"Primeiro cateto: {cateto1:.2f}")
print(f"Segundo cateto: {cateto2:.2f}")
print(f"Hipotenusa: {hipotenusa:.2f}")
