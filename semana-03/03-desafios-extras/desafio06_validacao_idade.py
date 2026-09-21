# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 06 - Validação de idade
# Arquivo: desafio06_validacao_idade.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Validar a entrada de idade utilizando uma função específica.
#
# Conteúdos:
# - funções
# - validação
# - tratamento de exceções
# - return
# =============================================================================


def ler_idade():

    while True:

        try:
            idade = int(input("Digite sua idade: "))

            if idade < 0 or idade > 120:
                print("Idade inválida. Tente novamente.")
                continue

            return idade

        except ValueError:
            print("Erro: informe um número inteiro.")


def classificar_idade(idade):

    if idade < 12:
        return "Criança"

    elif idade < 18:
        return "Adolescente"

    elif idade < 60:
        return "Adulto"

    else:
        return "Idoso"


def principal():

    idade = ler_idade()

    classificacao = classificar_idade(idade)

    print(f"\nIdade: {idade}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    principal()