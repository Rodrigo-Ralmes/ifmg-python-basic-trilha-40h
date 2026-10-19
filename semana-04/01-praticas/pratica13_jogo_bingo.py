# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 13 - Jogo de Bingo com conjuntos
# Arquivo: pratica13_jogo_bingo.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Implementar um jogo de bingo para vários jogadores utilizando listas,
# tuplas e conjuntos. O programa gera cartelas aleatórias, realiza sorteios,
# remove os números sorteados das cartelas e identifica automaticamente
# o jogador ou os jogadores vencedores.
#
# Conteúdos:
# - Listas
# - Tuplas
# - Conjuntos
# - Lista de tuplas
# - Funções
# - Parâmetros
# - Retorno de valores
# - Constantes
# - Biblioteca random
# - Função shuffle()
# - Função range()
# - Função len()
# - Método pop()
# - Método add()
# - Método remove()
# - Operador in
# - Conversão com set()
# - Fatiamento de listas
# - Desempacotamento de tuplas
# - Variável anônima _
# - Estrutura de repetição for
# - Estrutura de repetição while
# - Estrutura condicional if
# - Controle de fluxo com break
# - Estrutura __name__ == "__main__"
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# IMPORTAÇÕES
# =============================================================================

from random import shuffle


# =============================================================================
# CONSTANTES
# =============================================================================

TOTAL_NUM = 80

PERCENTUAL_CARTELA = 0.30


# =============================================================================
# FUNÇÃO - GERAR NÚMEROS
# =============================================================================

def gera_numeros():
    """
    Gera uma lista contendo todos os números possíveis do bingo,
    embaralha essa lista e retorna o resultado.

    Retorno:
        list:
            Lista com números de 1 até TOTAL_NUM em ordem aleatória.
    """

    lista_num = list(range(1, TOTAL_NUM + 1))

    shuffle(lista_num)

    return lista_num


# =============================================================================
# FUNÇÃO - GERAR CARTELA
# =============================================================================

def gera_cartela():
    """
    Gera uma cartela aleatória para um jogador.

    A cartela contém 30% dos números disponíveis no jogo.
    Os números são armazenados em um conjunto porque sua ordem
    não é importante e não pode haver elementos repetidos.

    Retorno:
        set:
            Conjunto contendo os números da cartela.
    """

    lista_num = gera_numeros()

    cartela_num = int(TOTAL_NUM * PERCENTUAL_CARTELA)

    cartela_set = set(
        lista_num[:cartela_num]
    )

    return cartela_set


# =============================================================================
# FUNÇÃO - GERAR JOGADORES
# =============================================================================

def gera_jogadores(num_jogadores):
    """
    Cadastra os jogadores e gera uma cartela para cada um.

    Cada jogador é representado por uma tupla:

        (nome, cartela)

    As tuplas são armazenadas em uma lista.

    Parâmetro:
        num_jogadores (int):
            Quantidade de jogadores participantes.

    Retorno:
        list:
            Lista contendo as tuplas dos jogadores.
    """

    lista_jogadores = []

    for contador in range(num_jogadores):

        print("\n" + "=" * 60)
        print(f"JOGADOR {contador + 1}")
        print("=" * 60)

        nome = input(
            "\nNome do jogador: "
        ).strip()

        cartela = gera_cartela()

        jogador = (
            nome,
            cartela
        )

        lista_jogadores.append(
            jogador
        )

    return lista_jogadores


# =============================================================================
# FUNÇÃO - REMOVER NÚMERO DAS CARTELAS
# =============================================================================

def remove_numero(lista_jogadores, numero):
    """
    Remove o número sorteado das cartelas que possuírem
    esse número.

    Parâmetros:
        lista_jogadores (list):
            Lista contendo as tuplas dos jogadores.

        numero (int):
            Número sorteado.
    """

    for _, cartela in lista_jogadores:

        if numero in cartela:

            cartela.remove(numero)


# =============================================================================
# FUNÇÃO - MOSTRAR ESTADO ATUAL DO JOGO
# =============================================================================

def mostra_jogo(sorteados, lista_jogadores):
    """
    Exibe os números sorteados e os números restantes
    nas cartelas dos jogadores.

    Parâmetros:
        sorteados (set):
            Conjunto contendo os números já sorteados.

        lista_jogadores (list):
            Lista contendo os jogadores e suas cartelas.
    """

    print("\n" + "=" * 60)
    print("BINGO")
    print("=" * 60)

    print(
        "\nNúmeros sorteados:"
    )

    print(
        sorted(sorteados)
    )

    print("\nCartelas:")

    for jogador in lista_jogadores:

        nome, cartela = jogador

        print(
            f"\n{nome}: "
            f"{sorted(cartela)}"
        )


# =============================================================================
# FUNÇÃO - BUSCAR VENCEDORES
# =============================================================================

def busca_vencedores(lista_jogadores):
    """
    Verifica quais jogadores não possuem mais números
    em suas cartelas.

    Um jogador vence quando sua cartela fica vazia.

    Parâmetro:
        lista_jogadores (list):
            Lista contendo os jogadores e suas cartelas.

    Retorno:
        set:
            Conjunto contendo os nomes dos vencedores.
    """

    vencedores = set()

    for nome, cartela in lista_jogadores:

        if len(cartela) == 0:

            vencedores.add(
                nome
            )

    return vencedores


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def principal():
    """
    Controla todo o fluxo de execução do jogo de bingo.
    """

    # =========================================================================
    # INÍCIO DO JOGO
    # =========================================================================

    print("=" * 60)
    print("INICIANDO O BINGO")
    print("=" * 60)

    num_jogadores = int(
        input(
            "\nInforme o número de jogadores: "
        )
    )


    # =========================================================================
    # GERAÇÃO DOS JOGADORES
    # =========================================================================

    lista_jogadores = gera_jogadores(
        num_jogadores
    )


    # =========================================================================
    # GERAÇÃO DOS NÚMEROS DO SORTEIO
    # =========================================================================

    lista_numeros = gera_numeros()


    # =========================================================================
    # CONJUNTO DE NÚMEROS SORTEADOS
    # =========================================================================

    sorteados = set()


    # =========================================================================
    # LAÇO PRINCIPAL DO JOGO
    # =========================================================================

    while True:

        # ---------------------------------------------------------------------
        # MOSTRAR ESTADO ATUAL
        # ---------------------------------------------------------------------

        mostra_jogo(
            sorteados,
            lista_jogadores
        )


        # ---------------------------------------------------------------------
        # AGUARDAR O PRÓXIMO SORTEIO
        # ---------------------------------------------------------------------

        print(
            "\nPressione ENTER para sortear um número."
        )

        input()


        # ---------------------------------------------------------------------
        # SORTEAR NÚMERO
        # ---------------------------------------------------------------------

        numero = lista_numeros.pop()


        # ---------------------------------------------------------------------
        # REGISTRAR NÚMERO SORTEADO
        # ---------------------------------------------------------------------

        sorteados.add(
            numero
        )

        print("\n" + "=" * 60)

        print(
            f"NÚMERO SORTEADO: {numero}"
        )

        print("=" * 60)


        # ---------------------------------------------------------------------
        # REMOVER NÚMERO DAS CARTELAS
        # ---------------------------------------------------------------------

        remove_numero(
            lista_jogadores,
            numero
        )


        # ---------------------------------------------------------------------
        # VERIFICAR VENCEDORES
        # ---------------------------------------------------------------------

        vencedores = busca_vencedores(
            lista_jogadores
        )


        # ---------------------------------------------------------------------
        # ENCERRAMENTO DO JOGO
        # ---------------------------------------------------------------------

        if len(vencedores) > 0:

            mostra_jogo(
                sorteados,
                lista_jogadores
            )

            print("\n" + "=" * 60)
            print("BINGO!")
            print("=" * 60)

            print(
                "\nVencedor(es):",
                vencedores
            )

            break


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    principal()