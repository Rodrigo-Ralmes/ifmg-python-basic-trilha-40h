# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 03 - Estrutura if/elif/else
# Arquivo: pratica03_if_elif_else.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Trabalhar com múltiplas alternativas utilizando if, elif e else.
#
# Conteúdos praticados:
# - if
# - elif
# - else
# - classificação por faixas
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

nota = float(input("Informe a nota do aluno (0 a 100): "))


# ============================================================
# PROCESSAMENTO
# ============================================================

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
elif nota >= 60:
    conceito = "D"
else:
    conceito = "E"


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(f"Conceito obtido: {conceito}")
