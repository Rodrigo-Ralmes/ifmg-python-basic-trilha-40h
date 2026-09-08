# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Desafio extra
# Desafio: 11 - Formatação de dados do usuário
# Arquivo: desafio11_formatacao_dados_usuario.py
# Autor: Rodrigo de Almeida Silveira
# Data: 03/09/2026
#
# Objetivo:
# Solicitar dados pessoais básicos e apresentá-los de maneira
# organizada utilizando strings formatadas.
#
# Conteúdos praticados:
# - input()
# - int()
# - variáveis
# - strings
# - métodos de string
# - f-string
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# ENTRADA DE DADOS
# =============================================================================

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
profissao = input("Digite sua profissão: ")


# =============================================================================
# PROCESSAMENTO
# =============================================================================

nome_formatado = nome.strip().title()
cidade_formatada = cidade.strip().title()
profissao_formatada = profissao.strip().title()


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

print()
print("=== DADOS DO USUÁRIO ===")
print(f"Nome: {nome_formatado}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade_formatada}")
print(f"Profissão: {profissao_formatada}")
