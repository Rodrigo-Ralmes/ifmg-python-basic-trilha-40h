# 🧩 Exercícios — Semana 02

Esta pasta reúne os exercícios desenvolvidos durante a **Semana 02** do curso **Python Básico — +IFMG**.

Os exercícios foram organizados conforme a sequência do material didático da Semana 02 e permitem aplicar os conhecimentos adquiridos sobre estruturas de decisão e estruturas de repetição.

---

## 🎯 Objetivo

O objetivo desta etapa é consolidar os conteúdos da Semana 02 por meio da resolução de problemas utilizando:

- estruturas condicionais;
- operadores relacionais;
- operadores lógicos;
- múltiplas alternativas;
- operadores aritméticos;
- estruturas de repetição;
- `while`;
- `for`;
- `range()`;
- `break`;
- contadores;
- acumuladores;
- processamento de quantidade indefinida de dados;
- algoritmos matemáticos;
- menus interativos.

---

## 🧠 Metodologia

Cada exercício foi desenvolvido seguindo o fluxo:

```text
Leitura do problema
        ↓
Identificação das entradas
        ↓
Definição das regras
        ↓
Planejamento do algoritmo
        ↓
Implementação em Python
        ↓
Execução no Spyder
        ↓
Testes com diferentes valores
        ↓
Validação dos resultados
        ↓
Correção de possíveis erros
        ↓
Documentação
        ↓
Versionamento com Git
        ↓
Publicação no GitHub
```

Os programas foram estruturados, sempre que aplicável, em:

```python
# ============================================================
# ENTRADA DE DADOS
# ============================================================


# ============================================================
# PROCESSAMENTO
# ============================================================


# ============================================================
# SAÍDA DE DADOS
# ============================================================
```

---

## 📚 Conteúdos praticados

Durante os exercícios foram utilizados:

- `input()`;
- `int()`;
- `float()`;
- `print()`;
- variáveis;
- operadores aritméticos;
- operadores relacionais;
- operadores lógicos;
- `if`;
- `elif`;
- `else`;
- comparações;
- resto de divisão;
- divisão inteira;
- cálculo de imposto;
- maior valor;
- menor valor;
- `while`;
- `while True`;
- `for`;
- `range()`;
- `break`;
- acumulador;
- fatorial;
- menu de opções;
- calculadora;
- tratamento de divisão por zero;
- formatação das saídas.

---

# 📊 Exercícios concluídos

| Nº | Exercício | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Maior entre três números | [`ex01_maior_de_tres.py`](ex01_maior_de_tres.py) | Estruturas de decisão | ✅ |
| 02 | Par ou ímpar sem operador `%` | [`ex02_par_impar_sem_modulo.py`](ex02_par_impar_sem_modulo.py) | Divisão inteira e decisão | ✅ |
| 03 | Cálculo do imposto de renda | [`ex03_imposto_renda.py`](ex03_imposto_renda.py) | `if/elif/else` | ✅ |
| 04 | Maior e menor de uma sequência | [`ex04_maior_menor_sequencia.py`](ex04_maior_menor_sequencia.py) | `while`, maior e menor | ✅ |
| 05 | Fatorial | [`ex05_fatorial.py`](ex05_fatorial.py) | `for` e acumulador | ✅ |
| 06 | Calculadora simples | [`ex06_calculadora.py`](ex06_calculadora.py) | Menu, repetição e decisão | ✅ |

---

# 🔎 Descrição dos exercícios

## 01 — Maior entre três números

O programa recebe três números e identifica qual deles possui o maior valor.

### Entradas

São solicitados três valores:

```python
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
```

### Processamento

São realizadas comparações entre os três números.

Exemplo:

```python
if a > b and a > c:
    maior = a
elif b > c:
    maior = b
else:
    maior = c
```

### Exemplo de execução

```text
Informe três números.

A: 10
B: 25
C: 8

O maior número é: 25
```

### Principais conceitos

- entrada de dados;
- `int()`;
- comparação;
- operador `>`;
- operador `and`;
- `if`;
- `elif`;
- `else`;
- seleção do maior valor.

Arquivo: [`ex01_maior_de_tres.py`](ex01_maior_de_tres.py)

---

## 02 — Número par ou ímpar sem utilizar `%`

O exercício verifica se um número é par ou ímpar sem utilizar diretamente o operador de resto `%`.

A ideia é utilizar divisão inteira e reconstruir o número.

### Estratégia

Para um número inteiro `n`:

```python
metade = n // 2
reconstruido = metade * 2
```

Se:

```python
reconstruido == n
```

o número é par.

Caso contrário, é ímpar.

### Exemplo

Para:

```text
n = 8
```

temos:

```text
8 // 2 = 4
4 × 2 = 8
```

Logo, o número é par.

Para:

```text
n = 7
```

temos:

```text
7 // 2 = 3
3 × 2 = 6
```

Como `6 != 7`, o número é ímpar.

### Principais conceitos

- entrada de dados;
- `int()`;
- divisão inteira `//`;
- multiplicação;
- comparação;
- `if/else`;
- paridade sem `%`.

Arquivo: [`ex02_par_impar_sem_modulo.py`](ex02_par_impar_sem_modulo.py)

---

## 03 — Cálculo do imposto de renda

O programa recebe um salário e calcula o imposto conforme as faixas apresentadas no material didático.

### Faixas utilizadas

```text
Até R$ 1.903,98
→ isento

De R$ 1.903,99 até R$ 2.826,65
→ 7,5%

De R$ 2.826,66 até R$ 3.751,05
→ 15%

De R$ 3.751,06 até R$ 4.664,68
→ 22,5%

Acima de R$ 4.664,68
→ 27,5%
```

### Estrutura de decisão

```python
if salario <= 1903.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 7.5 / 100
elif salario <= 3751.05:
    imposto = salario * 15 / 100
elif salario <= 4664.68:
    imposto = salario * 22.5 / 100
else:
    imposto = salario * 27.5 / 100
```

### Exemplo conceitual

Para:

```text
Salário = R$ 3.000,00
```

a alíquota utilizada é:

```text
15%
```

e o imposto calculado é:

```text
3000 × 15 / 100 = 450
```

### Principais conceitos

- `float()`;
- faixas de valores;
- `if/elif/else`;
- porcentagem;
- multiplicação;
- divisão;
- formatação monetária.

Arquivo: [`ex03_imposto_renda.py`](ex03_imposto_renda.py)

---

## 04 — Maior e menor número de uma sequência

O programa recebe uma quantidade indefinida de números.

Após cada valor, o usuário informa se deseja continuar ou encerrar.

Ao final são apresentados:

- maior número informado;
- menor número informado.

### Estrutura geral

```python
while True:
    numero = float(input("Informe um número: "))
```

O programa compara cada novo número com os valores armazenados.

### Controle de continuação

Exemplo:

```python
resposta = input("Deseja continuar? (S/N): ").strip().lower()

if resposta == "n":
    break
```

### Exemplo de execução

```text
Informe um número: 10
Deseja continuar? (S/N): S

Informe um número: 5
Deseja continuar? (S/N): S

Informe um número: 22
Deseja continuar? (S/N): N

Maior número informado: 22
Menor número informado: 5
```

### Principais conceitos

- quantidade indefinida;
- `while True`;
- `break`;
- comparação;
- maior valor;
- menor valor;
- atualização de variáveis;
- `.strip()`;
- `.lower()`.

Arquivo: [`ex04_maior_menor_sequencia.py`](ex04_maior_menor_sequencia.py)

---

## 05 — Fatorial

O programa calcula o fatorial de um número.

O fatorial de `n` é representado por:

```text
n!
```

Exemplo:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Portanto:

```text
5! = 120
```

Também:

```text
0! = 1
1! = 1
```

### Implementação com `for`

Uma possibilidade é:

```python
fatorial = 1

for numero in range(1, n + 1):
    fatorial *= numero
```

### Exemplo de execução

```text
Informe um número: 5

Fatorial de 5 = 120
```

### Principais conceitos

- `int()`;
- `for`;
- `range()`;
- acumulador multiplicativo;
- operador `*=`;
- fatorial.

Arquivo: [`ex05_fatorial.py`](ex05_fatorial.py)

---

## 06 — Calculadora simples

O último exercício integra vários conceitos da Semana 02.

O programa apresenta repetidamente um menu de operações.

### Operações disponíveis

```text
+
-
*
/
s
```

onde:

```text
+ → soma
- → subtração
* → multiplicação
/ → divisão
s → sair
```

### Estrutura principal

O programa permanece em execução utilizando:

```python
while True:
```

O usuário escolhe uma operação.

Se escolher:

```python
s
```

o programa utiliza:

```python
break
```

e encerra.

### Entrada dos números

Quando uma operação matemática é escolhida:

```python
numero1 = float(input("N1: "))
numero2 = float(input("N2: "))
```

### Processamento

Exemplo:

```python
if operacao == "+":
    resultado = numero1 + numero2

elif operacao == "-":
    resultado = numero1 - numero2

elif operacao == "*":
    resultado = numero1 * numero2

elif operacao == "/":
    resultado = numero1 / numero2
```

Também deve ser verificada a tentativa de divisão por zero.

### Exemplo de execução

```text
Calculadora (+, -, *, /)
Digite s para sair.

Informe a operação desejada: +
N1: 10
N2: 5

Resultado: 15
```

Após a operação, o menu é apresentado novamente.

### Principais conceitos

- `while True`;
- menu;
- entrada de opção;
- `if/elif/else`;
- `break`;
- operações matemáticas;
- soma;
- subtração;
- multiplicação;
- divisão;
- validação;
- repetição;
- programa interativo.

Arquivo: [`ex06_calculadora.py`](ex06_calculadora.py)

---

# 🗂️ Organização dos códigos

Os exercícios seguem um padrão contendo:

- curso;
- trilha;
- semana;
- tipo da atividade;
- número e nome do exercício;
- arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status;
- entrada;
- processamento;
- saída.

Exemplo:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Exercício
# Atividade: Exercício XX - Nome
# Arquivo: nome_do_arquivo.py
# Autor: Rodrigo Ralmes
#
# Objetivo:
# Descrição do objetivo.
#
# Conteúdos praticados:
# - conteúdo
# - conteúdo
#
# Status: Concluído
# =============================================================================
```

---

# 📁 Estrutura da pasta

```text
02-exercicios/
├── README.md
├── ex01_maior_de_tres.py
├── ex02_par_impar_sem_modulo.py
├── ex03_imposto_renda.py
├── ex04_maior_menor_sequencia.py
├── ex05_fatorial.py
└── ex06_calculadora.py
```

---

# ▶️ Como executar

## Execução pelo Spyder

1. Abra o Spyder.
2. Acesse `semana-02/02-exercicios`.
3. Abra o exercício.
4. Execute o programa.
5. Informe os dados solicitados.
6. Analise o resultado apresentado.
7. Faça novos testes com valores diferentes.

## Execução pelo terminal

Acesse:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

### Exercício 01

```bat
python semana-02\02-exercicios\ex01_maior_de_tres.py
```

### Exercício 02

```bat
python semana-02\02-exercicios\ex02_par_impar_sem_modulo.py
```

### Exercício 03

```bat
python semana-02\02-exercicios\ex03_imposto_renda.py
```

### Exercício 04

```bat
python semana-02\02-exercicios\ex04_maior_menor_sequencia.py
```

### Exercício 05

```bat
python semana-02\02-exercicios\ex05_fatorial.py
```

### Exercício 06

```bat
python semana-02\02-exercicios\ex06_calculadora.py
```

---

# 💡 Aprendizados consolidados

A realização dos exercícios permitiu consolidar:

- interpretação de problemas;
- identificação de entradas;
- definição das regras;
- construção de algoritmos;
- comparações entre valores;
- identificação do maior valor;
- utilização de operadores relacionais;
- utilização de operadores lógicos;
- uso de `if`;
- uso de `elif`;
- uso de `else`;
- classificação por faixas;
- cálculo de porcentagem;
- utilização de divisão inteira;
- implementação de algoritmos sem determinadas operações;
- repetição com quantidade indefinida;
- uso de `while`;
- uso de `while True`;
- interrupção de laços;
- uso de `break`;
- identificação de maior e menor valor;
- utilização de `for`;
- utilização de `range()`;
- construção de acumuladores;
- cálculo de fatorial;
- criação de menus;
- implementação de uma calculadora;
- combinação de estruturas de decisão e repetição;
- teste de diferentes cenários;
- identificação e correção de erros;
- documentação dos programas;
- versionamento separado;
- publicação no GitHub.

---

# 📈 Progresso

| Indicador | Resultado |
|---|---:|
| Exercícios planejados | 6 |
| Exercícios concluídos | 6 |
| Total de arquivos Python | 6 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

# ✅ Status da etapa

> **Etapa concluída:** todos os exercícios da Semana 02 foram desenvolvidos, testados, documentados, versionados e publicados no GitHub.

---

# 🔗 Navegação

- [⬅️ Voltar para a Semana 02](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🚀 Acessar os desafios extras](../03-desafios-extras/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

# 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.