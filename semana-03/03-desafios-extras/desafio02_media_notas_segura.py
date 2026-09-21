# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 02 - Média de notas segura
# Arquivo: desafio02_media_notas_segura.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Calcular a média de duas notas utilizando funções e tratamento de erros.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - try
# - except
# - validação
# =============================================================================


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def situacao_aluno(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


def principal():

    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
            print("\nErro: as notas devem estar entre 0 e 10.")
            return

        media = calcular_media(nota1, nota2)

        print(f"\nMédia: {media:.2f}")
        print(f"Situação: {situacao_aluno(media)}")

    except ValueError:
        print("\nErro: informe apenas valores numéricos.")


if __name__ == "__main__":
    principal()