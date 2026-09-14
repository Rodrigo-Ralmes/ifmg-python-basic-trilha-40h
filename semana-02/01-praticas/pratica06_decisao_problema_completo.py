# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 06 - Problema completo com decisão
# Arquivo: pratica06_decisao_problema_completo.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Integrar entrada, cálculo de média e classificação da situação de um aluno.
#
# Conteúdos praticados:
# - input
# - float
# - média aritmética
# - if/elif/else
# - f-string
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))


# ============================================================
# PROCESSAMENTO
# ============================================================

media = (nota1 + nota2) / 2

if media >= 60:
    situacao = "Aprovado"
elif media >= 40:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")