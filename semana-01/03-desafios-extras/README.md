# 🚀 Desafios Extras — Semana 01

Esta pasta reúne os desafios extras desenvolvidos durante a **Semana 01** do curso **Python Básico — +IFMG**.

Os desafios complementam as práticas e os exercícios oficiais, permitindo aplicar os fundamentos iniciais da linguagem Python na resolução de problemas envolvendo cálculos, conversões, porcentagens, medidas e formatação de dados.

---

## 🎯 Objetivo

Consolidar os fundamentos iniciais da linguagem Python por meio do desenvolvimento de pequenos programas completos.

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
- tipos de dados;
- operadores aritméticos;
- adição;
- subtração;
- multiplicação;
- divisão;
- exponenciação com `**`;
- cálculo de porcentagens;
- fórmulas matemáticas;
- conversão de temperaturas;
- conversão de unidades de medida;
- estruturas condicionais;
- `if`;
- `elif`;
- `else`;
- módulo `math`;
- função `math.sqrt()`;
- métodos de strings;
- método `strip()`;
- método `title()`;
- f-strings;
- formatação com `.2f`;
- entrada, processamento e saída de dados.

---

## 📊 Desafios concluídos

| Nº | Desafio | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Média de duas notas | [`desafio01_media_duas_notas.py`](desafio01_media_duas_notas.py) | Média aritmética | ✅ |
| 02 | Conversor de temperatura | [`desafio02_conversor_temperatura.py`](desafio02_conversor_temperatura.py) | Celsius para Fahrenheit | ✅ |
| 02.01 | Conversor de temperatura ampliado | [`desafio02_01_conversor_temperatura.py`](desafio02_01_conversor_temperatura.py) | Conversão bidirecional | ✅ |
| 03 | Calculadora de IMC | [`desafio03_calculadora_imc.py`](desafio03_calculadora_imc.py) | Divisão e exponenciação | ✅ |
| 04 | Salário por horas trabalhadas | [`desafio04_salario_horas_trabalhadas.py`](desafio04_salario_horas_trabalhadas.py) | Multiplicação e salário bruto | ✅ |
| 05 | Consumo de combustível | [`desafio05_consumo_combustivel.py`](desafio05_consumo_combustivel.py) | Cálculo de consumo médio | ✅ |
| 06 | Conversor de metros | [`desafio06_conversor_metros.py`](desafio06_conversor_metros.py) | Conversão de medidas | ✅ |
| 07 | Preço com desconto | [`desafio07_preco_com_desconto.py`](desafio07_preco_com_desconto.py) | Porcentagem e desconto | ✅ |
| 08 | Reajuste salarial | [`desafio08_reajuste_salarial.py`](desafio08_reajuste_salarial.py) | Porcentagem e reajuste | ✅ |
| 09 | Circunferência | [`desafio09_circunferencia.py`](desafio09_circunferencia.py) | Comprimento e área | ✅ |
| 10 | Hipotenusa | [`desafio10_hipotenusa.py`](desafio10_hipotenusa.py) | Teorema de Pitágoras | ✅ |
| 11 | Formatação de dados do usuário | [`desafio11_formatacao_dados_usuario.py`](desafio11_formatacao_dados_usuario.py) | Manipulação de strings | ✅ |

---

## 🔎 Descrição dos desafios

### 01 — Média de duas notas

O programa solicita duas notas, calcula a média aritmética e apresenta o resultado com duas casas decimais.

```text
Média = (nota 1 + nota 2) / 2
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- adição;
- divisão;
- média aritmética;
- f-string;
- formatação decimal.

Arquivo: [`desafio01_media_duas_notas.py`](desafio01_media_duas_notas.py)

---

### 02 — Conversor de temperatura

O programa solicita uma temperatura em graus Celsius e realiza sua conversão para graus Fahrenheit.

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- operadores aritméticos;
- conversão de temperatura;
- f-string.

Arquivo: [`desafio02_conversor_temperatura.py`](desafio02_conversor_temperatura.py)

---

### 02.01 — Conversor de temperatura ampliado

Versão ampliada do desafio 02 que permite selecionar uma das duas conversões:

1. Celsius para Fahrenheit;
2. Fahrenheit para Celsius.

Fórmulas utilizadas:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
Celsius = (Fahrenheit - 32) / 1,8
```

Principais conceitos:

- entrada de opções;
- conversão para `int`;
- conversão para `float`;
- estrutura condicional;
- `if`;
- `elif`;
- `else`;
- conversão bidirecional;
- formatação decimal.

Arquivo: [`desafio02_01_conversor_temperatura.py`](desafio02_01_conversor_temperatura.py)

---

### 03 — Calculadora de IMC

O programa solicita o peso e a altura de uma pessoa e calcula o seu Índice de Massa Corporal.

```text
IMC = peso / altura²
```

Em Python:

```python
imc = peso / (altura ** 2)
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- divisão;
- exponenciação;
- formatação decimal.

Arquivo: [`desafio03_calculadora_imc.py`](desafio03_calculadora_imc.py)

---

### 04 — Salário por horas trabalhadas

O programa solicita a quantidade de horas trabalhadas e o valor recebido por hora para calcular o salário bruto.

```text
Salário bruto = horas trabalhadas × valor da hora
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- multiplicação;
- cálculo salarial;
- formatação monetária.

Arquivo: [`desafio04_salario_horas_trabalhadas.py`](desafio04_salario_horas_trabalhadas.py)

---

### 05 — Consumo de combustível

O programa solicita a distância percorrida e a quantidade de combustível utilizada para calcular o consumo médio do veículo.

```text
Consumo médio = distância percorrida / combustível utilizado
```

O resultado é apresentado em quilômetros por litro:

```text
km/l
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- divisão;
- cálculo de consumo médio;
- formatação decimal.

Arquivo: [`desafio05_consumo_combustivel.py`](desafio05_consumo_combustivel.py)

---

### 06 — Conversor de metros

O programa solicita uma medida em metros e apresenta os valores correspondentes em quilômetros, centímetros e milímetros.

```text
Quilômetros = metros / 1000
Centímetros = metros × 100
Milímetros = metros × 1000
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- multiplicação;
- divisão;
- conversão de unidades;
- formatação decimal.

Arquivo: [`desafio06_conversor_metros.py`](desafio06_conversor_metros.py)

---

### 07 — Preço com desconto

O programa solicita o preço original de um produto e o percentual de desconto.

Em seguida, calcula o valor do desconto e o preço final do produto.

```text
Valor do desconto = preço × (percentual / 100)
Preço final = preço - valor do desconto
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- cálculo de porcentagem;
- multiplicação;
- subtração;
- formatação monetária.

Arquivo: [`desafio07_preco_com_desconto.py`](desafio07_preco_com_desconto.py)

---

### 08 — Reajuste salarial

O programa solicita o salário atual e o percentual de reajuste para calcular o novo salário.

```text
Valor do reajuste = salário × (percentual / 100)
Novo salário = salário + valor do reajuste
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- porcentagem;
- multiplicação;
- adição;
- cálculo salarial;
- formatação monetária.

Arquivo: [`desafio08_reajuste_salarial.py`](desafio08_reajuste_salarial.py)

---

### 09 — Circunferência

O programa solicita o raio de uma circunferência e calcula seu comprimento e a área do círculo.

```text
Comprimento = 2 × π × raio
Área = π × raio²
```

Em Python, a área pode ser calculada com:

```python
area = pi * (raio ** 2)
```

Neste desafio também foi compreendida a diferença entre os operadores:

```python
raio ^ 2   # XOR — não representa potência
raio ** 2  # exponenciação — representa potência
```

Principais conceitos:

- entrada de dados;
- conversão para `float`;
- constante π;
- multiplicação;
- exponenciação;
- comprimento da circunferência;
- área do círculo.

Arquivo: [`desafio09_circunferencia.py`](desafio09_circunferencia.py)

---

### 10 — Hipotenusa

O programa solicita os valores dos dois catetos de um triângulo retângulo e calcula a hipotenusa por meio do Teorema de Pitágoras.

```text
Hipotenusa = √(cateto 1² + cateto 2²)
```

Em Python:

```python
hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))
```

Principais conceitos:

- importação do módulo `math`;
- função `math.sqrt()`;
- entrada de dados;
- conversão para `float`;
- exponenciação;
- adição;
- raiz quadrada;
- Teorema de Pitágoras.

Arquivo: [`desafio10_hipotenusa.py`](desafio10_hipotenusa.py)

---

### 11 — Formatação de dados do usuário

O programa solicita dados pessoais básicos e apresenta as informações de maneira organizada e formatada.

Dados solicitados:

- nome completo;
- idade;
- cidade;
- profissão.

Métodos utilizados:

```python
strip()
title()
```

O método `strip()` remove espaços desnecessários no início e no final do texto.

O método `title()` transforma a primeira letra de cada palavra em maiúscula.

Principais conceitos:

- entrada de textos;
- entrada de números inteiros;
- strings;
- métodos de strings;
- padronização de dados;
- f-strings;
- apresentação organizada de informações.

Arquivo: [`desafio11_formatacao_dados_usuario.py`](desafio11_formatacao_dados_usuario.py)

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
# Semana: 01
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
├── desafio01_media_duas_notas.py
├── desafio02_conversor_temperatura.py
├── desafio02_01_conversor_temperatura.py
├── desafio03_calculadora_imc.py
├── desafio04_salario_horas_trabalhadas.py
├── desafio05_consumo_combustivel.py
├── desafio06_conversor_metros.py
├── desafio07_preco_com_desconto.py
├── desafio08_reajuste_salarial.py
├── desafio09_circunferencia.py
├── desafio10_hipotenusa.py
└── desafio11_formatacao_dados_usuario.py
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
python semana-01\03-desafios-extras\desafio01_media_duas_notas.py
```

Exemplo para executar o desafio da hipotenusa:

```bat
python semana-01\03-desafios-extras\desafio10_hipotenusa.py
```

Exemplo para executar o desafio de formatação de dados:

```bat
python semana-01\03-desafios-extras\desafio11_formatacao_dados_usuario.py
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
| Versões ampliadas concluídas | 1 |
| Total de arquivos Python | 12 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

## ✅ Status da etapa

> **Etapa concluída:** todos os desafios extras planejados para a Semana 01 foram desenvolvidos, testados, documentados, versionados e publicados no GitHub.

---

## 🔗 Navegação

- [⬅️ Voltar para a Semana 01](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🧩 Acessar os exercícios oficiais](../02-exercicios/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.