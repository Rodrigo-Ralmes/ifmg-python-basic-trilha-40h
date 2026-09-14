# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 02 - Estrutura if/else
# Arquivo: pratica02_if_else.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Utilizar if e else para criar dois caminhos possíveis de execução.
#
# Conteúdos praticados:
# - if
# - else
# - operadores relacionais
# - f-string
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

nota = float(input("Informe a nota final do aluno: "))


# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

if nota >= 60:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Situação do aluno: {situacao}")
