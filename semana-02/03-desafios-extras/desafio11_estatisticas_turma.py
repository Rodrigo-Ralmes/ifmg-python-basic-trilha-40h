# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 11 - Estatísticas da turma
# Arquivo: desafio11_estatisticas_turma.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Registrar as notas de uma quantidade determinada de alunos e apresentar
# estatísticas gerais da turma.
#
# Conteúdos praticados:
# - input()
# - int()
# - float()
# - for
# - range()
# - contador
# - acumulador
# - média
# - maior valor
# - menor valor
# - if/else
# - f-string
#
# Status: A executar
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

quantidade_alunos = int(input("Informe a quantidade de alunos: "))


# =============================================================================
# VALIDAÇÃO
# =============================================================================

if quantidade_alunos <= 0:

    print("A quantidade de alunos deve ser maior que zero.")

else:

    # =========================================================================
    # INICIALIZAÇÃO
    # =========================================================================

    soma_notas = 0
    aprovados = 0
    reprovados = 0

    maior_nota = None
    menor_nota = None


    # =========================================================================
    # ENTRADA E PROCESSAMENTO
    # =========================================================================

    for aluno in range(1, quantidade_alunos + 1):

        nota = float(input(f"Informe a nota do {aluno}º aluno: "))

        soma_notas += nota

        if maior_nota is None:
            maior_nota = nota
            menor_nota = nota

        else:

            if nota > maior_nota:
                maior_nota = nota

            if nota < menor_nota:
                menor_nota = nota

        if nota >= 6:
            aprovados += 1

        else:
            reprovados += 1


    # =========================================================================
    # CÁLCULO DA MÉDIA
    # =========================================================================

    media_turma = soma_notas / quantidade_alunos


    # =========================================================================
    # SAÍDA DE DADOS
    # =========================================================================

    print("\nESTATÍSTICAS DA TURMA")
    print(f"Quantidade de alunos: {quantidade_alunos}")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")
    print(f"Alunos aprovados: {aprovados}")
    print(f"Alunos reprovados: {reprovados}")