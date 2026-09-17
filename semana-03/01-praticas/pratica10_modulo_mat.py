# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 10 - Criação de módulo matemático
# Arquivo: pratica10_modulo_mat.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Criar um módulo contendo funções matemáticas reutilizáveis.
#
# Conteúdos:
# - módulos
# - funções
# - return
# - recursão
#
# Status: Em desenvolvimento
# =============================================================================


def cubo(numero):
    return numero * numero * numero


def fatorial(numero):

    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)
