# -*- coding: utf-8 -*-
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Atividade: Desafio 07 - Senha com três tentativas
# Arquivo: desafio07_senha_tres_tentativas.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Simular um processo simples de autenticação permitindo no máximo três
# tentativas para informar a senha correta.
#
# Conteúdos praticados:
# - input()
# - strings
# - while
# - contador
# - if/else
# - break
# - comparação de valores
#
# Status: A executar
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

senha_correta = "python123"
tentativas = 0
acesso_liberado = False


# =============================================================================
# PROCESSAMENTO
# =============================================================================

while tentativas < 3:

    senha = input("Informe a senha: ").strip()

    tentativas += 1

    if senha == senha_correta:
        acesso_liberado = True
        break

    else:
        restantes = 3 - tentativas

        if restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {restantes}")


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================

if acesso_liberado:
    print("Acesso liberado.")

else:
    print("Acesso bloqueado. Número máximo de tentativas atingido.")