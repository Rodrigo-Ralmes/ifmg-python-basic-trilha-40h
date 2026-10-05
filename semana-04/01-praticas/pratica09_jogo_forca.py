# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 09 - Jogo da Forca com listas
# Arquivo: pratica09_jogo_forca.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Implementar um jogo da forca para dois jogadores utilizando listas,
# funções, estruturas de repetição, validações e operadores de associação.
# Um jogador informa a palavra secreta e o outro tenta descobri-la,
# digitando uma letra por vez.
#
# Conteúdos:
# - Listas
# - Inicialização de listas
# - Funções
# - Parâmetros
# - Retorno de valores
# - Estrutura de repetição while
# - Estrutura de repetição for
# - Função enumerate()
# - Estrutura condicional if
# - Operadores in e not in
# - Função len()
# - Método upper()
# - Método strip()
# - Método join()
# - Validação de dados
# - Manipulação de strings
# - Contador de erros
# - Controle de fluxo
# - continue
# - break
# - Estrutura __name__ == "__main__"
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# FUNÇÃO - VALIDAR PALAVRA
# =============================================================================

def valida_palavra(palavra):
    """
    Verifica se todos os caracteres da palavra estão entre A e Z.

    Parâmetro:
        palavra (str): palavra que será validada.

    Retorno:
        bool: True se a palavra for válida.
              False se possuir algum caractere inválido.
    """

    for letra in palavra:
        if letra < "A" or letra > "Z":
            return False

    return True


# =============================================================================
# FUNÇÃO - INICIAR NOVO JOGO
# =============================================================================

def novo_jogo():
    """
    Solicita ao primeiro jogador a palavra secreta.

    A função permanece em repetição até que seja informada
    uma palavra válida.

    Retorno:
        str: palavra secreta validada e convertida para maiúsculas.
    """

    while True:

        print("Informe a palavra para seu adversário.")
        print("Não use espaços ou caracteres especiais.")

        palavra = input("Palavra: ").upper().strip()

        if valida_palavra(palavra):
            return palavra

        else:
            print("\nPalavra inválida! Tente novamente.\n")


# =============================================================================
# FUNÇÃO - VERIFICAR SE A PALAVRA POSSUI A LETRA
# =============================================================================

def tem_letra(palavra, letra, letras_tela):
    """
    Verifica se a letra informada existe na palavra secreta.

    Quando a letra é encontrada, sua posição correspondente
    é atualizada na lista letras_tela.

    Parâmetros:
        palavra (str):
            Palavra secreta.

        letra (str):
            Letra informada pelo jogador.

        letras_tela (list):
            Lista utilizada para representar as letras já descobertas.

    Retorno:
        bool: True se a letra existir na palavra.
              False caso contrário.
    """

    encontrada = False

    for indice, caractere in enumerate(palavra):

        if caractere == letra:

            encontrada = True

            letras_tela[indice] = letra

    return encontrada


# =============================================================================
# FUNÇÃO - MOSTRAR ESTADO ATUAL DO JOGO
# =============================================================================

def mostra_jogo(letras_tela, digitadas, erros):
    """
    Exibe as informações atuais do jogo.

    Parâmetros:
        letras_tela (list):
            Letras descobertas e posições ainda ocultas.

        digitadas (str):
            Letras já informadas pelo jogador.

        erros (int):
            Quantidade atual de erros.
    """

    # Limpa visualmente a tela para esconder a palavra secreta
    # informada pelo primeiro jogador.
    print("\n" * 100)

    print("=" * 60)
    print("JOGO DA FORCA")
    print("=" * 60)

    print("\nPalavra:")
    print("".join(letras_tela))

    print("\nLetras digitadas:", digitadas)

    print("Erros:", erros)


# =============================================================================
# FUNÇÃO - VALIDAR LETRA
# =============================================================================

def valida_letra(letra, digitadas):
    """
    Verifica se a entrada possui exatamente uma letra válida
    e se essa letra ainda não foi utilizada.

    Parâmetros:
        letra (str):
            Letra informada pelo jogador.

        digitadas (str):
            Letras já utilizadas anteriormente.

    Retorno:
        bool: True se a letra for válida e ainda não tiver sido digitada.
              False caso contrário.
    """

    if len(letra) != 1:
        return False

    if letra < "A" or letra > "Z" or letra in digitadas:
        return False

    return True


# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def principal():
    """
    Controla todo o fluxo do jogo da forca.
    """

    # =========================================================================
    # INICIALIZAÇÃO DO JOGO
    # =========================================================================

    palavra = novo_jogo()

    # Cria uma lista contendo um "_" para cada caractere da palavra.
    #
    # Exemplo:
    #
    # palavra = "PYTHON"
    #
    # letras_tela =
    # ["_", "_", "_", "_", "_", "_"]
    #
    letras_tela = ["_"] * len(palavra)

    # Contador de erros.
    erros = 0

    # String utilizada para armazenar as letras já informadas.
    digitadas = ""


    # =========================================================================
    # LAÇO PRINCIPAL DO JOGO
    # =========================================================================

    while True:

        # ---------------------------------------------------------------------
        # EXIBIÇÃO DO ESTADO ATUAL
        # ---------------------------------------------------------------------

        mostra_jogo(
            letras_tela,
            digitadas,
            erros
        )


        # ---------------------------------------------------------------------
        # ENTRADA DA LETRA
        # ---------------------------------------------------------------------

        letra = input(
            "\nInforme uma letra: "
        ).upper().strip()


        # ---------------------------------------------------------------------
        # VALIDAÇÃO DA LETRA
        # ---------------------------------------------------------------------

        if not valida_letra(letra, digitadas):

            print(
                "\nLetra inválida ou já digitada."
            )

            continue


        # ---------------------------------------------------------------------
        # REGISTRO DA LETRA DIGITADA
        # ---------------------------------------------------------------------

        digitadas += letra


        # ---------------------------------------------------------------------
        # VERIFICAÇÃO DA LETRA NA PALAVRA
        # ---------------------------------------------------------------------

        if not tem_letra(
            palavra,
            letra,
            letras_tela
        ):

            erros += 1


        # ---------------------------------------------------------------------
        # VERIFICAÇÃO DE DERROTA
        # ---------------------------------------------------------------------

        if erros == 5:

            mostra_jogo(
                letras_tela,
                digitadas,
                erros
            )

            print("\nVocê perdeu!")

            break


        # ---------------------------------------------------------------------
        # VERIFICAÇÃO DE VITÓRIA
        # ---------------------------------------------------------------------

        if "_" not in letras_tela:

            mostra_jogo(
                letras_tela,
                digitadas,
                erros
            )

            print("\nVocê acertou!")

            break


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    principal()