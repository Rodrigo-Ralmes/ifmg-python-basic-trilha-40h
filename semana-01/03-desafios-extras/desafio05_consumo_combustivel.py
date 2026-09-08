# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 05 - Consumo de combustível
# Arquivo: desafio05_consumo_combustivel.py
# Autor: Rodrigo de Almeida Silveira
# Data: 08/09/2026
#
# Objetivo:
# Calcular o consumo médio de combustível de um veículo em
# quilômetros por litro.
#
# Conteúdos praticados:
# - input()
# - float()
# - variáveis
# - divisão
# - cálculo de consumo médio
# - saída formatada
# - f-string
#
# Status: Concluído
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

distancia = float(
    input("Digite a distância percorrida em quilômetros: ")
)

combustivel = float(
    input("Digite a quantidade de combustível utilizada: ")
)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

consumo_medio = distancia / combustivel


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== CONSUMO DE COMBUSTÍVEL ===")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível utilizado: {combustivel:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")