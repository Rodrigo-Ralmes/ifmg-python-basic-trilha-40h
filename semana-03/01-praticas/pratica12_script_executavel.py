#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 12 - Script executável
# Arquivo: pratica12_script_executavel.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar a estrutura básica de um arquivo Python que também pode
# ser executado como script.
#
# Conteúdos:
# - script Python
# - funções
# - shebang
# - execução de programa
#
# Status: Em desenvolvimento
# =============================================================================


def cubo(numero):
    return numero * numero * numero


numero = int(input("Informe um número: "))

print(f"{numero} ao cubo é {cubo(numero)}")