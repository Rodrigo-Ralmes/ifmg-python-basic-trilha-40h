# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 12 - Decisão e repetição
# Arquivo: pratica12_decisao_repeticao.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Combinar estruturas de decisão e repetição na resolução de um problema.
#
# Conteúdos praticados:
# - for
# - if/else
# - contador
# - entrada de dados
#
# Status: A executar
# =============================================================================


# ============================================================
# INICIALIZAÇÃO
# ============================================================

aprovados = 0
reprovados = 0


# ============================================================
# ENTRADA E PROCESSAMENTO
# ============================================================

for aluno in range(1, 6):
    nota = float(input(f"Informe a nota do {aluno}º aluno: "))

    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1


# ============================================================
# SAÍDA DE DADOS
# ============================================================

print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")