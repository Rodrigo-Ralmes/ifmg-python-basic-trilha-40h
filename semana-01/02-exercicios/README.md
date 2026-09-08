# 🧩 Exercícios Oficiais — Semana 01

Esta pasta reúne os exercícios oficiais desenvolvidos durante a **Semana 01** do curso **Python Básico — +IFMG**.

Os exercícios foram utilizados para aplicar, de maneira estruturada, os fundamentos iniciais da linguagem Python por meio da interpretação de problemas, definição das entradas, processamento das informações e apresentação dos resultados.

---

## 🎯 Objetivo

O objetivo desta etapa é consolidar os conhecimentos fundamentais da Semana 01 por meio da resolução de exercícios envolvendo:

- leitura e interpretação de problemas;
- entrada de dados;
- conversão de tipos;
- armazenamento de valores em variáveis;
- utilização de operadores aritméticos;
- aplicação de fórmulas matemáticas;
- divisão inteira;
- operador de resto;
- conversão de unidades de tempo;
- cálculo de porcentagem;
- formatação das informações;
- apresentação organizada dos resultados.

---

## 🧠 Metodologia

Cada exercício foi desenvolvido seguindo um processo sequencial e lógico:

```text
Leitura do problema
        ↓
Identificação das entradas
        ↓
Definição das variáveis
        ↓
Planejamento do processamento
        ↓
Implementação em Python
        ↓
Execução no Spyder
        ↓
Verificação dos resultados
        ↓
Correção de possíveis erros
        ↓
Versionamento com Git
        ↓
Publicação no GitHub
```

Os programas foram organizados internamente em três partes principais:

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

Essa separação permite compreender com clareza:

- quais informações entram no programa;
- quais cálculos e transformações são realizados;
- quais resultados são apresentados ao usuário.

---

## 📚 Conteúdos praticados

Durante o desenvolvimento dos exercícios, foram utilizados os seguintes conteúdos:

- `input()`;
- `int()`;
- `float()`;
- `print()`;
- variáveis;
- tipos numéricos;
- operadores aritméticos;
- adição;
- subtração;
- multiplicação;
- divisão;
- divisão inteira com `//`;
- operador de resto com `%`;
- cálculo de área;
- conversão de segundos;
- cálculo de juros simples;
- cálculo de porcentagem;
- f-strings;
- formatação com `.2f`;
- entrada, processamento e saída de dados.

---

## 📊 Exercícios concluídos

| Nº | Exercício | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Área de um triângulo | [`ex01_area_triangulo.py`](ex01_area_triangulo.py) | Multiplicação, divisão e cálculo de área | ✅ |
| 02A | Conversão de segundos para HMS | [`ex02a_segundos_para_hms.py`](ex02a_segundos_para_hms.py) | Divisão inteira, resto e conversão de tempo | ✅ |
| 03 | Cálculo de juros simples | [`ex03_juros_simples.py`](ex03_juros_simples.py) | Porcentagem, juros e montante | ✅ |

---

## 🔎 Descrição dos exercícios

### 01 — Área de um triângulo

O programa solicita a base e a altura de um triângulo, calcula sua área e apresenta o resultado.

A fórmula utilizada é:

```text
Área = (base × altura) / 2
```

Em Python:

```python
area = (base * altura) / 2
```

### Entradas

O programa recebe:

- base do triângulo;
- altura do triângulo.

As entradas são convertidas para `float`, permitindo a utilização de valores inteiros ou decimais.

Exemplo:

```python
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
```

### Processamento

```python
area = (base * altura) / 2
```

### Exemplo de execução

```text
Digite a base do triângulo: 5
Digite a altura do triângulo: 10

=== ÁREA DO TRIÂNGULO ===
Base: 5.00
Altura: 10.00
Área do triângulo: 25.00
```

### Principais conceitos

- entrada de dados;
- conversão para `float`;
- variáveis;
- multiplicação;
- divisão;
- cálculo de área;
- f-string;
- formatação decimal.

Arquivo: [`ex01_area_triangulo.py`](ex01_area_triangulo.py)

---

### 02A — Conversão de segundos para horas, minutos e segundos

O programa solicita uma quantidade total de segundos e converte o valor informado em:

- horas;
- minutos;
- segundos restantes.

Para realizar a conversão, são utilizados:

- divisão inteira com `//`;
- operador de resto com `%`.

### Fórmulas utilizadas

```text
Horas = total de segundos // 3600
Restante = total de segundos % 3600
Minutos = restante // 60
Segundos = restante % 60
```

Em Python:

```python
horas = total_segundos // 3600
restante = total_segundos % 3600

minutos = restante // 60
segundos = restante % 60
```

### Entendendo a divisão inteira

O operador `//` retorna somente a parte inteira da divisão.

Exemplo:

```python
7120 // 3600
```

Resultado:

```text
1
```

Isso significa que existem uma hora completa em `7120` segundos.

### Entendendo o operador de resto

O operador `%` retorna o restante de uma divisão.

Exemplo:

```python
7120 % 3600
```

Resultado:

```text
3520
```

Após retirar uma hora completa, restam `3520` segundos.

### Exemplo de execução

```text
Digite a quantidade total de segundos: 7120

=== CONVERSÃO DE SEGUNDOS ===
Total informado: 7120 segundos
Resultado: 1 hora(s), 58 minuto(s) e 40 segundo(s)
```

### Verificação do resultado

```text
1 hora = 3600 segundos
58 minutos = 3480 segundos
40 segundos = 40 segundos
```

Somando os valores:

```text
3600 + 3480 + 40 = 7120 segundos
```

Portanto, o resultado está correto.

### Principais conceitos

- entrada de dados;
- conversão para `int`;
- variáveis;
- divisão inteira;
- operador de resto;
- conversão de unidades de tempo;
- saída formatada;
- f-string.

Arquivo: [`ex02a_segundos_para_hms.py`](ex02a_segundos_para_hms.py)

---

### 03 — Cálculo de juros simples

O programa solicita:

- capital inicial;
- taxa de juros;
- quantidade de períodos.

Em seguida, calcula o valor dos juros simples e o montante final.

### Fórmula dos juros simples

```text
Juros = Capital × Taxa × Tempo
```

Como a taxa é informada em porcentagem, primeiro ela precisa ser convertida para sua forma decimal:

```text
Taxa decimal = Taxa percentual / 100
```

Depois, são calculados os juros:

```text
Juros = Capital × Taxa decimal × Tempo
```

Por fim, calcula-se o montante:

```text
Montante = Capital + Juros
```

### Implementação em Python

```python
taxa_decimal = taxa_percentual / 100
juros = capital * taxa_decimal * tempo
montante = capital + juros
```

### Exemplo de cálculo

Considerando:

```text
Capital inicial = R$ 1.000,00
Taxa de juros = 10% ao período
Quantidade de períodos = 12
```

Conversão da taxa:

```text
10 / 100 = 0,10
```

Cálculo dos juros:

```text
Juros = 1000 × 0,10 × 12
Juros = 1200
```

Cálculo do montante:

```text
Montante = 1000 + 1200
Montante = 2200
```

### Exemplo de execução

```text
Digite o capital inicial: R$ 1000
Digite a taxa de juros (% ao período): 10
Digite a quantidade de períodos: 12

=== CÁLCULO DE JUROS SIMPLES ===
Capital inicial: R$ 1000.00
Taxa de juros: 10.00% ao período
Quantidade de períodos: 12
Juros: R$ 1200.00
Montante final: R$ 2200.00
```

### Principais conceitos

- entrada de dados;
- conversão para `float`;
- conversão para `int`;
- variáveis;
- operadores aritméticos;
- divisão;
- multiplicação;
- porcentagem;
- juros simples;
- montante;
- f-string;
- formatação monetária.

Arquivo: [`ex03_juros_simples.py`](ex03_juros_simples.py)

---

## 🔢 Operadores utilizados

### Multiplicação

O operador `*` realiza uma multiplicação:

```python
resultado = valor1 * valor2
```

Foi utilizado no cálculo da área e dos juros simples.

---

### Divisão

O operador `/` realiza uma divisão e pode produzir um resultado decimal:

```python
resultado = valor1 / valor2
```

Foi utilizado no cálculo da área e na conversão da taxa percentual.

---

### Divisão inteira

O operador `//` realiza uma divisão e retorna apenas a parte inteira:

```python
resultado = valor1 // valor2
```

Foi utilizado para descobrir a quantidade completa de horas e minutos.

---

### Operador de resto

O operador `%` retorna o restante de uma divisão:

```python
restante = valor1 % valor2
```

Foi utilizado para determinar os segundos restantes após a conversão das horas e dos minutos.

---

## 🗂️ Organização dos códigos

Os arquivos seguem um padrão de documentação contendo:

- curso;
- trilha;
- semana;
- tipo da atividade;
- número e nome do exercício;
- nome do arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status;
- entrada de dados;
- processamento;
- saída de dados.

Exemplo do cabeçalho utilizado:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Exercício oficial
# Exercício: número e nome do exercício
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
02-exercicios/
├── README.md
├── ex01_area_triangulo.py
├── ex02a_segundos_para_hms.py
└── ex03_juros_simples.py
```

---

## ▶️ Como executar

### Execução pelo Spyder

1. Abra o Spyder.
2. Acesse a pasta `semana-01/02-exercicios`.
3. Abra o arquivo desejado.
4. Execute o programa.
5. Informe os valores solicitados no console.
6. Verifique os resultados apresentados.

### Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

Para executar o exercício 01:

```bat
python semana-01\02-exercicios\ex01_area_triangulo.py
```

Para executar o exercício 02A:

```bat
python semana-01\02-exercicios\ex02a_segundos_para_hms.py
```

Para executar o exercício 03:

```bat
python semana-01\02-exercicios\ex03_juros_simples.py
```

---

## 💡 Aprendizados consolidados

A conclusão dos exercícios permitiu consolidar os seguintes aprendizados:

- interpretar enunciados;
- identificar os dados necessários;
- definir entradas, processamento e saídas;
- escolher tipos de dados adequados;
- converter entradas para `int` e `float`;
- armazenar valores em variáveis;
- aplicar operadores aritméticos;
- utilizar corretamente a divisão comum;
- utilizar divisão inteira;
- utilizar o operador de resto;
- aplicar fórmulas geométricas;
- converter unidades de tempo;
- calcular porcentagens;
- calcular juros simples;
- calcular o montante final;
- formatar valores numéricos;
- apresentar informações de maneira organizada;
- testar os programas com valores diferentes;
- analisar e corrigir erros;
- documentar os códigos;
- versionar individualmente os exercícios;
- publicar os resultados no GitHub.

---

## 📈 Progresso

| Indicador | Resultado |
|---|---:|
| Exercícios oficiais planejados | 3 |
| Exercícios oficiais concluídos | 3 |
| Total de arquivos Python | 3 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

## ✅ Status da etapa

> **Etapa concluída:** todos os exercícios oficiais planejados para a Semana 01 foram desenvolvidos, testados, documentados, versionados e publicados no GitHub.

---

## 🔗 Navegação

- [⬅️ Voltar para a Semana 01](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🚀 Acessar os desafios extras](../03-desafios-extras/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.