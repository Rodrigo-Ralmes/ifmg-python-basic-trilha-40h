# -*- coding: utf-8 -*-

# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 04
# Tipo: Prática
# Atividade: 12 - Operações com conjuntos
# Arquivo: pratica12_operacoes_conjuntos.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Demonstrar a utilização de conjuntos em Python e aplicar operações de
# interseção, união, diferença, subconjunto, superconjunto, verificação
# de pertencimento, adição e remoção de elementos.
#
# Conteúdos:
# - Conjuntos
# - Tipo set
# - Elementos não repetidos
# - Coleções não ordenadas
# - Interseção
# - União
# - Diferença
# - Subconjunto
# - Superconjunto
# - Operador in
# - Método add()
# - Método remove()
# - Operadores &, |, -, <= e >=
# - Métodos intersection()
# - Método union()
# - Método difference()
# - Método issubset()
# - Método issuperset()
#
# Status: Em desenvolvimento
# =============================================================================


# =============================================================================
# INICIALIZAÇÃO DOS CONJUNTOS
# =============================================================================

s1 = {1, 2, 3, 4}

s2 = {4, 5, 6}

s3 = {4, 5}


# =============================================================================
# SAÍDA - CONJUNTOS ORIGINAIS
# =============================================================================

print("=" * 60)
print("OPERAÇÕES COM CONJUNTOS")
print("=" * 60)

print("\nConjuntos utilizados:")

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")


# =============================================================================
# INTERSEÇÃO
# =============================================================================

print("\n" + "=" * 60)
print("INTERSEÇÃO")
print("=" * 60)

intersecao_operador = s1 & s2

intersecao_metodo = s1.intersection(s2)

print(f"\ns1 & s2 = {intersecao_operador}")

print(
    f"s1.intersection(s2) = "
    f"{intersecao_metodo}"
)


# =============================================================================
# UNIÃO
# =============================================================================

print("\n" + "=" * 60)
print("UNIÃO")
print("=" * 60)

uniao_operador = s1 | s2

uniao_metodo = s1.union(s2)

print(f"\ns1 | s2 = {uniao_operador}")

print(
    f"s1.union(s2) = "
    f"{uniao_metodo}"
)


# =============================================================================
# DIFERENÇA
# =============================================================================

print("\n" + "=" * 60)
print("DIFERENÇA")
print("=" * 60)

diferenca_operador = s1 - s2

diferenca_metodo = s1.difference(s2)

print(f"\ns1 - s2 = {diferenca_operador}")

print(
    f"s1.difference(s2) = "
    f"{diferenca_metodo}"
)


# =============================================================================
# SUBCONJUNTO
# =============================================================================

print("\n" + "=" * 60)
print("SUBCONJUNTO")
print("=" * 60)

subconjunto_operador = s3 <= s2

subconjunto_metodo = s3.issubset(s2)

print(f"\ns3 <= s2 = {subconjunto_operador}")

print(
    f"s3.issubset(s2) = "
    f"{subconjunto_metodo}"
)


# =============================================================================
# SUPERCONJUNTO
# =============================================================================

print("\n" + "=" * 60)
print("SUPERCONJUNTO")
print("=" * 60)

superconjunto_operador = s1 >= s3

superconjunto_metodo = s1.issuperset(s3)

print(f"\ns1 >= s3 = {superconjunto_operador}")

print(
    f"s1.issuperset(s3) = "
    f"{superconjunto_metodo}"
)


# =============================================================================
# VERIFICAÇÃO DE PERTENCIMENTO
# =============================================================================

print("\n" + "=" * 60)
print("PERTENCIMENTO")
print("=" * 60)

valor = 4

print(
    f"\nO valor {valor} pertence a s1? "
    f"{valor in s1}"
)

print(
    f"O valor {valor} pertence a s2? "
    f"{valor in s2}"
)

print(
    f"O valor {valor} pertence a s3? "
    f"{valor in s3}"
)


# =============================================================================
# ADIÇÃO DE ELEMENTO
# =============================================================================

print("\n" + "=" * 60)
print("ADIÇÃO DE ELEMENTO")
print("=" * 60)

print(f"\ns1 antes do add(): {s1}")

s1.add(5)

print(f"s1 depois de add(5): {s1}")


# =============================================================================
# REMOÇÃO DE ELEMENTO
# =============================================================================

print("\n" + "=" * 60)
print("REMOÇÃO DE ELEMENTO")
print("=" * 60)

print(f"\ns1 antes do remove(): {s1}")

s1.remove(2)

print(f"s1 depois de remove(2): {s1}")
