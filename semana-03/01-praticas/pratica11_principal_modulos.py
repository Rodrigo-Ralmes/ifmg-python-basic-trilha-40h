# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Prática
# Atividade: 11 - Utilização de módulo próprio
# Arquivo: pratica11_principal_modulos.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Importar e utilizar funções existentes em outro módulo Python.
#
# Conteúdos:
# - módulos
# - import
# - from ... import
# - reutilização de código
#
# Status: Em desenvolvimento
# =============================================================================


from pratica10_modulo_mat import cubo, fatorial


numero = int(input("Informe um número: "))

print(f"{numero} ao cubo é {cubo(numero)}")
print(f"O fatorial de {numero} é {fatorial(numero)}")