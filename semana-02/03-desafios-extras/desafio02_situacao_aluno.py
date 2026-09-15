# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 02 - Situação do aluno
# Arquivo: desafio02_situacao_aluno.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Solicitar duas notas, calcular a média aritmética do aluno e classificá-lo
# como aprovado, em recuperação ou reprovado.
#
# Conteúdos praticados:
# - input()
# - float()
# - média aritmética
# - if/elif/else
# - operadores relacionais
# - f-string
# - formatação decimal
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))


# =============================================================================
# PROCESSAMENTO
# =============================================================================

media = (nota1 + nota2) / 2

if media >= 60:
    situacao = "Aprovado"

elif media >= 40:
    situacao = "Recuperação"

else:
    situacao = "Reprovado"


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")