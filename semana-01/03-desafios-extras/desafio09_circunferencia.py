# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 09 - Comprimento e área da circunferência
# Arquivo: desafio09_circunferencia.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Calcular o comprimento e a área de uma circunferência a partir
# do valor de seu raio.
#
# Conteúdos praticados:
# - import
# - módulo math
# - math.pi
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

raio = float(input("Digite o raio da circunferência: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

comprimento = 2 * math.pi * raio
area = math.pi * (raio ** 2)


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CIRCUNFERÊNCIA ===")
print(f"Raio: {raio:.2f}")
print(f"Comprimento: {comprimento:.2f}")
print(f"Área: {area:.2f}")

