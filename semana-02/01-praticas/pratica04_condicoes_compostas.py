# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 04 - Condições compostas
# Arquivo: pratica04_condicoes_compostas.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Combinar condições com operadores lógicos em estruturas de decisão.
#
# Conteúdos praticados:
# - and
# - or
# - not
# - if/else
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

idade = int(input("Informe sua idade: "))
possui_cnh = input("Possui CNH? (S/N): ").strip().lower()


# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

if idade >= 18 and possui_cnh == "s":
    print("Você atende aos dois requisitos para dirigir.")
else:
    print("Você não atende aos dois requisitos para dirigir.")