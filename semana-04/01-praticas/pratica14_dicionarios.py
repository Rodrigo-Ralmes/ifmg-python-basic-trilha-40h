# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 14 - Dicionários
# Arquivo: pratica14_dicionarios.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar a criação e manipulação de dicionários em Python, utilizando
# associações entre chaves e valores, consulta, inclusão, atualização,
# percurso e alguns dos principais métodos disponíveis para esse tipo
# de coleção.
#
# Conteúdos:
# - Dicionários
# - Associação chave-valor
# - Criação de dicionário vazio
# - Criação de dicionário preenchido
# - Consulta por chave
# - Inclusão de elementos
# - Alteração de valores
# - Estrutura de repetição for
# - Método clear()
# - Método copy()
# - Método items()
# - Método keys()
# - Método popitem()
# - Método update()
# - Método values()
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# CRIAÇÃO DOS DICIONÁRIOS
# =============================================================================

dic_vazio = {}

dic_letras = {
    1: "A",
    2: "B",
    3: "C"
}


# =============================================================================
# SAÍDA - DICIONÁRIOS INICIAIS
# =============================================================================

print("=" * 60)
print("DICIONÁRIOS")
print("=" * 60)

print("\nDicionário vazio:")
print(dic_vazio)

print("\nDicionário de letras:")
print(dic_letras)


# =============================================================================
# INCLUSÃO DE NOVA CHAVE E VALOR
# =============================================================================

print("\n" + "=" * 60)
print("INCLUSÃO DE ELEMENTO")
print("=" * 60)

dic_letras[4] = "E"

print("\nApós adicionar a chave 4 com o valor 'E':")
print(dic_letras)


# =============================================================================
# ALTERAÇÃO DE VALOR
# =============================================================================

print("\n" + "=" * 60)
print("ALTERAÇÃO DE VALOR")
print("=" * 60)

dic_letras[4] = "D"

print("\nApós alterar o valor da chave 4 para 'D':")
print(dic_letras)


# =============================================================================
# CONSULTA DIRETA POR CHAVE
# =============================================================================

print("\n" + "=" * 60)
print("CONSULTA POR CHAVE")
print("=" * 60)

print(f"\nValor associado à chave 1: {dic_letras[1]}")
print(f"Valor associado à chave 2: {dic_letras[2]}")
print(f"Valor associado à chave 3: {dic_letras[3]}")
print(f"Valor associado à chave 4: {dic_letras[4]}")


# =============================================================================
# PERCORRENDO O DICIONÁRIO
# =============================================================================

print("\n" + "=" * 60)
print("PERCORRENDO O DICIONÁRIO")
print("=" * 60)

for contador in range(1, 5):
    print(
        f"{contador}: "
        f"{dic_letras[contador]}"
    )


# =============================================================================
# MÉTODO keys()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO keys()")
print("=" * 60)

chaves = dic_letras.keys()

print("\nChaves do dicionário:")
print(chaves)


# =============================================================================
# MÉTODO values()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO values()")
print("=" * 60)

valores = dic_letras.values()

print("\nValores do dicionário:")
print(valores)


# =============================================================================
# MÉTODO items()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO items()")
print("=" * 60)

itens = dic_letras.items()

print("\nPares chave-valor:")
print(itens)


# =============================================================================
# PERCURSO COM items()
# =============================================================================

print("\n" + "=" * 60)
print("PERCURSO COM items()")
print("=" * 60)

for chave, valor in dic_letras.items():

    print(
        f"Chave: {chave} | "
        f"Valor: {valor}"
    )


# =============================================================================
# MÉTODO copy()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO copy()")
print("=" * 60)

copia_letras = dic_letras.copy()

print("\nDicionário original:")
print(dic_letras)

print("\nCópia do dicionário:")
print(copia_letras)


# =============================================================================
# MÉTODO update()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO update()")
print("=" * 60)

novas_letras = {
    5: "E",
    6: "F"
}

copia_letras.update(
    novas_letras
)

print("\nDicionário utilizado na atualização:")
print(novas_letras)

print("\nCópia após update():")
print(copia_letras)


# =============================================================================
# MÉTODO popitem()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO popitem()")
print("=" * 60)

item_removido = copia_letras.popitem()

print("\nItem removido:")
print(item_removido)

print("\nDicionário após popitem():")
print(copia_letras)


# =============================================================================
# MÉTODO clear()
# =============================================================================

print("\n" + "=" * 60)
print("MÉTODO clear()")
print("=" * 60)

copia_para_limpar = dic_letras.copy()

print("\nAntes do clear():")
print(copia_para_limpar)

copia_para_limpar.clear()

print("\nDepois do clear():")
print(copia_para_limpar)


# =============================================================================
# SAÍDA FINAL
# =============================================================================

print("\n" + "=" * 60)
print("DICIONÁRIO ORIGINAL PRESERVADO")
print("=" * 60)

print("\ndic_letras:")
print(dic_letras)