# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Prática
# Atividade: Prática 05 - Estruturas de decisão aninhadas
# Arquivo: pratica05_if_aninhado.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Compreender estruturas if dentro de outras estruturas if.
#
# Conteúdos praticados:
# - if aninhado
# - else
# - entrada de dados
# - strip() -> remove espaços em branco no início e no fim da string
# - lower() -> converte a string para letras minúsculas
#
# Status: A executar
# =============================================================================


# ============================================================
# ENTRADA DE DADOS
# ============================================================

idade = int(input("Informe sua idade: "))

# ============================================================
# PROCESSAMENTO E SAÍDA DE DADOS
# ============================================================

if idade >= 18:
    possui_cnh = input("Possui CNH? (S/N): ").strip().lower()

    if possui_cnh == "s":
        print("Maior de idade e habilitado para dirigir.")
    else:
        print("Maior de idade, mas não possui CNH.")
else:
    print("Menor de idade.")

