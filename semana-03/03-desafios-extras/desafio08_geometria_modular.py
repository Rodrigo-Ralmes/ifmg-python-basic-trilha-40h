# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Desafio Extra
# Atividade: 08 - Geometria modular
# Arquivo: desafio08_geometria_modular.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar funções independentes para cálculo de áreas geométricas.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
# - modularização
# - tratamento de exceções
# =============================================================================


import math


def area_quadrado(lado):
    return lado ** 2


def area_retangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_circulo(raio):
    return math.pi * raio ** 2


def principal():

    print("CÁLCULO DE ÁREAS")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Círculo")

    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            lado = float(input("Lado: "))
            resultado = area_quadrado(lado)

        elif opcao == 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            resultado = area_retangulo(base, altura)

        elif opcao == 3:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            resultado = area_triangulo(base, altura)

        elif opcao == 4:
            raio = float(input("Raio: "))
            resultado = area_circulo(raio)

        else:
            print("\nOpção inválida.")
            return

        print(f"\nÁrea calculada: {resultado:.2f}")

    except ValueError:
        print("\nErro: informe apenas números válidos.")


if __name__ == "__main__":
    principal()