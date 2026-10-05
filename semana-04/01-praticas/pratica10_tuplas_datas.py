# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 10 - Tuplas representando datas
# Arquivo: pratica10_tuplas_datas.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Utilizar tuplas para representar datas, armazenando ano, mês e dia em
# uma estrutura fixa, comparar duas datas diretamente e identificar qual
# delas é a mais recente.
#
# Conteúdos:
# - Tuplas
# - Criação de tuplas
# - Índices
# - Imutabilidade
# - Comparação de tuplas
# - Entrada de dados
# - Conversão para int
# - Estrutura condicional if
# - Desempacotamento de tuplas
# - Formatação de datas
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# FUNÇÃO - LER DATA
# =============================================================================

def ler_data(numero):
    """
    Solicita dia, mês e ano e retorna uma tupla no formato:

        (ano, mes, dia)

    A ordem ano, mês e dia permite comparar diretamente
    duas tuplas representando datas.

    Parâmetro:
        numero (int):
            Número utilizado para identificar a data na tela.

    Retorno:
        tuple:
            Tupla contendo ano, mês e dia.
    """

    print(f"\nData {numero}")

    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))

    data = (ano, mes, dia)

    return data


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

print("=" * 60)
print("COMPARAÇÃO DE DATAS UTILIZANDO TUPLAS")
print("=" * 60)

print("\nInforme as datas:")

data1 = ler_data(1)

data2 = ler_data(2)


# =============================================================================
# PROCESSAMENTO
# =============================================================================

data_mais_recente = data1

if data2 > data1:
    data_mais_recente = data2


# =============================================================================
# DESEMPACOTAMENTO DA TUPLA
# =============================================================================

ano, mes, dia = data_mais_recente


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print("\n" + "=" * 60)
print("RESULTADO")
print("=" * 60)

print(f"\nPrimeira data: {data1[2]:02d}/{data1[1]:02d}/{data1[0]}")

print(f"Segunda data: {data2[2]:02d}/{data2[1]:02d}/{data2[0]}")

print(
    f"\nData mais recente: "
    f"{dia:02d}/{mes:02d}/{ano}"
)