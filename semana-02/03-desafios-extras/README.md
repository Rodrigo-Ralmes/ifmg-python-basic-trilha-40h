# 🚀 Desafios Extras — Semana 02

Esta pasta reúne os desafios extras desenvolvidos durante a **Semana 02** do curso **Python Básico — +IFMG**.

Os desafios complementam as práticas e os exercícios oficiais, permitindo aplicar os estruturas de decisão e estruturas de repetição na resolução de problemas envolvendo condições, repetições, contadores, acumuladores, sequências numéricas e controle de fluxo.

---

## 🎯 Objetivo

Consolidar os estruturas de decisão e estruturas de repetição por meio do desenvolvimento de pequenos programas completos.

Os desafios foram elaborados para exercitar:

- interpretação de problemas;
- identificação das entradas;
- definição das variáveis;
- processamento dos dados;
- aplicação de fórmulas matemáticas;
- formatação das saídas;
- execução e teste dos programas;
- identificação e correção de erros;
- versionamento dos arquivos com Git;
- publicação dos códigos no GitHub.

---

## 🧠 Metodologia

Cada desafio foi desenvolvido seguindo um fluxo sequencial e lógico:

```text
Problema
    ↓
Análise
    ↓
Definição das entradas
    ↓
Processamento
    ↓
Implementação em Python
    ↓
Teste no Spyder
    ↓
Correção
    ↓
Versionamento com Git
    ↓
Publicação no GitHub
```

Internamente, os códigos foram organizados em três seções principais:

```python
# =============================================================================
# ENTRADA DE DADOS
# =============================================================================


# =============================================================================
# PROCESSAMENTO
# =============================================================================


# =============================================================================
# SAÍDA DE DADOS
# =============================================================================
```

Essa estrutura torna os arquivos mais organizados, legíveis e fáceis de compreender.

---

## 📚 Conteúdos praticados

Durante o desenvolvimento dos desafios, foram utilizados os seguintes conceitos:

- `input()`;
- `int()`;
- `float()`;
- variáveis;
- operadores aritméticos;
- operadores relacionais;
- operadores lógicos;
- operador de resto `%`;
- estruturas condicionais;
- `if`;
- `elif`;
- `else`;
- estruturas condicionais aninhadas;
- `while`;
- `while True`;
- `for`;
- `range()`;
- `break`;
- `continue`;
- contadores;
- acumuladores;
- comparação de valores;
- maior e menor valor;
- média aritmética;
- divisibilidade;
- sequências numéricas;
- métodos de strings;
- método `strip()`;
- método `lower()`;
- f-strings;
- formatação com `.2f`;
- entrada, processamento e saída de dados.

---

## 📊 Desafios concluídos

| Nº | Desafio | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Classificador de número | [`desafio01_classificador_numero.py`](desafio01_classificador_numero.py) | `if/elif/else` e paridade | ✅ |
| 02 | Situação do aluno | [`desafio02_situacao_aluno.py`](desafio02_situacao_aluno.py) | Média e decisão múltipla | ✅ |
| 03 | Maior e menor de cinco números | [`desafio03_maior_menor_cinco_numeros.py`](desafio03_maior_menor_cinco_numeros.py) | `for` e comparação | ✅ |
| 04 | Tabuada | [`desafio04_tabuada.py`](desafio04_tabuada.py) | `for`, `range()` e multiplicação | ✅ |
| 05 | Soma dos pares de um intervalo | [`desafio05_soma_pares_intervalo.py`](desafio05_soma_pares_intervalo.py) | Acumulador e `%` | ✅ |
| 06 | Contador de sinais | [`desafio06_contador_sinais.py`](desafio06_contador_sinais.py) | Contadores | ✅ |
| 07 | Senha com três tentativas | [`desafio07_senha_tres_tentativas.py`](desafio07_senha_tres_tentativas.py) | `while` e `break` | ✅ |
| 08 | Calculadora com menu | [`desafio08_calculadora_menu.py`](desafio08_calculadora_menu.py) | `while True`, `break` e `continue` | ✅ |
| 09 | Sequência de Fibonacci | [`desafio09_fibonacci.py`](desafio09_fibonacci.py) | Sequência e repetição | ✅ |
| 10 | Número primo | [`desafio10_numero_primo.py`](desafio10_numero_primo.py) | Divisibilidade e `break` | ✅ |
| 11 | Estatísticas da turma | [`desafio11_estatisticas_turma.py`](desafio11_estatisticas_turma.py) | Contadores, acumuladores e média | ✅ |

---

## 🔎 Descrição dos desafios

### 01 — Classificador de número

O programa solicita um número inteiro e identifica se o valor é positivo, negativo ou zero. Quando o número é diferente de zero, também verifica se ele é par ou ímpar.

```python
numero % 2 == 0
```

Principais conceitos:

- entrada de dados;
- conversão para `int`;
- `if`;
- `elif`;
- `else`;
- estruturas aninhadas;
- operador `%`.

Arquivo: [`desafio01_classificador_numero.py`](desafio01_classificador_numero.py)

---

### 02 — Situação do aluno

O programa solicita duas notas, calcula a média aritmética e classifica o aluno como aprovado, em recuperação ou reprovado.

```text
Média = (nota 1 + nota 2) / 2
```

Critérios utilizados:

```text
Média >= 60 → Aprovado
Média >= 40 → Recuperação
Média < 40  → Reprovado
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- média aritmética;
- `if`;
- `elif`;
- `else`;
- formatação decimal.

Arquivo: [`desafio02_situacao_aluno.py`](desafio02_situacao_aluno.py)

---

### 03 — Maior e menor de cinco números

O programa solicita cinco números e identifica o maior e o menor valor informado por meio de comparações sucessivas.

Principais conceitos:

- `for`;
- `range()`;
- operadores relacionais;
- atualização de variáveis;
- maior valor;
- menor valor.

Arquivo: [`desafio03_maior_menor_cinco_numeros.py`](desafio03_maior_menor_cinco_numeros.py)

---

### 04 — Tabuada

O programa solicita um número inteiro e apresenta sua tabuada de multiplicação de 1 a 10.

```python
for multiplicador in range(1, 11):
```

Principais conceitos:

- `for`;
- `range()`;
- multiplicação;
- repetição definida;
- f-string.

Arquivo: [`desafio04_tabuada.py`](desafio04_tabuada.py)

---

### 05 — Soma dos pares de um intervalo

O programa percorre um intervalo numérico, identifica os números pares e acumula sua soma.

```python
numero % 2 == 0
soma += numero
```

Principais conceitos:

- `for`;
- `range()`;
- `if`;
- operador `%`;
- acumulador;
- intervalos numéricos.

Arquivo: [`desafio05_soma_pares_intervalo.py`](desafio05_soma_pares_intervalo.py)

---

### 06 — Contador de sinais

O programa solicita dez valores e contabiliza quantos são positivos, negativos ou iguais a zero.

```python
positivos += 1
negativos += 1
zeros += 1
```

Principais conceitos:

- contadores;
- `for`;
- `range()`;
- `if`;
- `elif`;
- `else`.

Arquivo: [`desafio06_contador_sinais.py`](desafio06_contador_sinais.py)

---

### 07 — Senha com três tentativas

O programa simula um controle simples de autenticação, permitindo no máximo três tentativas.

```python
while tentativas < 3:
```

Quando a senha correta é informada, `break` encerra imediatamente o laço.

Principais conceitos:

- strings;
- `while`;
- contador;
- condição de parada;
- `break`;
- comparação.

Arquivo: [`desafio07_senha_tres_tentativas.py`](desafio07_senha_tres_tentativas.py)

---

### 08 — Calculadora com menu

O programa implementa uma calculadora interativa que permanece ativa até que o usuário escolha sair.

```python
while True:
```

São utilizados `break` para encerrar o programa e `continue` para retornar ao início do menu em situações específicas.

Principais conceitos:

- menu;
- `while True`;
- `if/elif/else`;
- `break`;
- `continue`;
- operadores aritméticos;
- validação.

Arquivo: [`desafio08_calculadora_menu.py`](desafio08_calculadora_menu.py)

---

### 09 — Sequência de Fibonacci

O programa gera uma quantidade definida de termos da sequência de Fibonacci.

```text
0 1 1 2 3 5 8 13 21 34 ...
```

Cada novo termo é obtido pela soma dos dois anteriores.

```python
proximo = primeiro + segundo
```

Principais conceitos:

- `for`;
- `range()`;
- variáveis auxiliares;
- atualização de valores;
- sequência numérica.

Arquivo: [`desafio09_fibonacci.py`](desafio09_fibonacci.py)

---

### 10 — Número primo

O programa verifica se um número inteiro é primo.

A divisibilidade é testada utilizando o operador `%`, e a busca pode ser encerrada com `break` quando um divisor é encontrado.

Principais conceitos:

- divisibilidade;
- operador `%`;
- `for`;
- `range()`;
- `if`;
- `break`;
- variável booleana.

Arquivo: [`desafio10_numero_primo.py`](desafio10_numero_primo.py)

---

### 11 — Estatísticas da turma

O programa solicita a quantidade de alunos e suas notas. Ao final, calcula a média da turma, a maior nota, a menor nota e as quantidades de aprovados e reprovados.

```python
soma_notas += nota
aprovados += 1
```

Principais conceitos:

- `for`;
- `range()`;
- contador;
- acumulador;
- média;
- maior valor;
- menor valor;
- `if/else`.

Arquivo: [`desafio11_estatisticas_turma.py`](desafio11_estatisticas_turma.py)

---

## 🗂️ Organização dos códigos

Os arquivos seguem um padrão de documentação contendo:

- identificação do curso;
- identificação da trilha;
- número da semana;
- tipo da atividade;
- número e nome do desafio;
- nome do arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status da atividade;
- entrada de dados;
- processamento;
- saída de dados.

Exemplo da estrutura utilizada:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 02 - Controle de Fluxo
# Tipo: Desafio extra
# Desafio: número e nome do desafio
# Arquivo: nome_do_arquivo.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Descrição do objetivo do programa.
#
# Conteúdos praticados:
# - conteúdo
# - conteúdo
#
# Status: Concluído
# =============================================================================
```

---

## 📁 Estrutura da pasta

```text
03-desafios-extras/
├── README.md
├── desafio01_classificador_numero.py
├── desafio02_situacao_aluno.py
├── desafio03_maior_menor_cinco_numeros.py
├── desafio04_tabuada.py
├── desafio05_soma_pares_intervalo.py
├── desafio06_contador_sinais.py
├── desafio07_senha_tres_tentativas.py
├── desafio08_calculadora_menu.py
├── desafio09_fibonacci.py
├── desafio10_numero_primo.py
└── desafio11_estatisticas_turma.py
```

---

## ▶️ Como executar

### Execução pelo Spyder

1. Abra o Spyder.
2. Selecione o arquivo desejado.
3. Execute o programa.
4. Informe os valores solicitados no console.
5. Verifique o resultado apresentado.

### Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

Execute o desafio desejado:

```bat
python semana-02\03-desafios-extras\desafio01_classificador_numero.py
```

Exemplo para executar o desafio da hipotenusa:

```bat
python semana-02\03-desafios-extras\desafio10_numero_primo.py
```

Exemplo para executar o desafio de formatação de dados:

```bat
python semana-02\03-desafios-extras\desafio11_estatisticas_turma.py
```

---

## 💡 Aprendizados consolidados

A conclusão desta etapa permitiu desenvolver e consolidar as seguintes competências:

- transformar um problema escrito em uma sequência lógica;
- identificar entradas, processamento e saídas;
- selecionar os tipos de dados adequados;
- utilizar variáveis com nomes descritivos;
- converter valores digitados pelo usuário;
- aplicar operadores aritméticos;
- implementar fórmulas matemáticas;
- trabalhar com porcentagens;
- converter temperaturas;
- converter unidades de medida;
- calcular áreas e comprimentos;
- utilizar exponenciação corretamente;
- importar e utilizar o módulo `math`;
- aplicar estruturas condicionais;
- formatar valores numéricos;
- organizar mensagens no console;
- manipular e padronizar strings;
- testar os programas com valores diferentes;
- interpretar mensagens de erro;
- corrigir problemas de sintaxe e lógica;
- documentar os códigos;
- versionar cada desafio separadamente;
- publicar a evolução dos estudos no GitHub.

---

## 📈 Progresso

| Indicador | Resultado |
|---|---:|
| Desafios principais planejados | 11 |
| Desafios principais concluídos | 11 |
| Total de arquivos Python | 11 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

## ✅ Status da etapa

> **Etapa concluída:** todos os desafios extras planejados para a Semana 02 foram desenvolvidos, testados, documentados, versionados e publicados no GitHub.

---

## 🔗 Navegação

- [⬅️ Voltar para a Semana 02](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🧩 Acessar os exercícios oficiais](../02-exercicios/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.