# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:58:50 2026

@author: Rodrigo
"""

# ============================================================
# Curso: Python Básico - +IFMG
# Carga horária: 40h
# Trilha integrada: Python + Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: 09 - Manipulação de strings
# Arquivo: pratica09_strings.py
# Autor: Rodrigo de Almeida Silveira
# Data: 31/08/2026 15:58:50
#
# Objetivo:
# Praticar operações básicas de manipulação e formatação
# de informações textuais.
#
# Conteúdos praticados:
# - str
# - find()
# - format()
# - len()
# - concatenação
# - print()
#
# Status: Prática
# ============================================================


# ============================================================
# CRIAÇÃO DA STRING
# ============================================================

nome = input("Informe seu nome: ")

cidade = input("Informe sua cidade: ")


# ============================================================
# CONCATENAÇÃO
# ============================================================

mensagem = "Olá, " + nome + "!"

print()

print(mensagem)


# ============================================================
# TAMANHO DO TEXTO
# ============================================================

print("Quantidade de caracteres do nome:", len(nome))


# ============================================================
# LOCALIZANDO TEXTO
# ============================================================

posicao = nome.find("a")

print("Posição da primeira letra 'a':", posicao)


# ============================================================
# FORMAT
# ============================================================

mensagem_formatada = "Meu nome é {} e moro em {}.".format(nome, cidade)

print(mensagem_formatada)


# ============================================================
# FORMATAÇÃO DE NÚMEROS
# ============================================================

valor = 1234.56789

print("Valor original:", valor)

print("Valor com duas casas decimais: {:.2f}".format(valor))