# 🚀 Desafios Extras — Semana 03

Esta pasta reúne os desafios extras desenvolvidos durante a **Semana 03** do curso **Python Básico — +IFMG**.

Os desafios complementam as práticas e os exercícios oficiais, permitindo aplicar os conteúdos de **tratamento de exceções, modularização, decomposição de problemas, criação de funções, reutilização de código e recursão** na resolução de problemas mais completos.

> **Importante:** os arquivos desta pasta são exercícios **autorais de consolidação**. Eles não correspondem aos exercícios oficiais do e-book do +IFMG.

---

## 🎯 Objetivo

Consolidar os conteúdos estudados na Semana 03 por meio do desenvolvimento de pequenos programas completos, organizados e reutilizáveis.

Os desafios foram elaborados para exercitar:

- interpretação de problemas;
- decomposição de problemas em partes menores;
- criação e chamada de funções;
- definição de parâmetros;
- retorno de valores;
- reutilização de código;
- tratamento de exceções;
- validação de entradas;
- tratamento de entradas inválidas;
- tratamento de divisão por zero;
- modularização;
- recursão;
- organização lógica dos programas;
- execução e teste dos programas;
- identificação e correção de erros;
- versionamento individual dos arquivos com Git;
- publicação dos códigos no GitHub.

---

## 🧠 Metodologia

Cada desafio foi desenvolvido seguindo um fluxo sequencial e lógico:

```text
Problema
    ↓
Análise
    ↓
Decomposição do problema
    ↓
Definição das funções
    ↓
Tratamento das entradas
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

Na Semana 03, os códigos passam a enfatizar a separação das responsabilidades em funções, permitindo organizar melhor os programas e reutilizar trechos de código.

Exemplo:

```python
def calcular(valor1, valor2):
    # processamento
    return resultado


try:
    # entrada e chamada das funções
    pass

except ValueError:
    # tratamento da entrada inválida
    pass
```

Essa estrutura favorece programas mais organizados, legíveis, reutilizáveis e fáceis de testar.

---

## 📚 Conteúdos praticados

Durante o desenvolvimento dos desafios, foram utilizados e consolidados conceitos como:

- `input()`;
- `int()`;
- `float()`;
- variáveis;
- operadores aritméticos;
- operadores relacionais;
- estruturas condicionais;
- `if`;
- `elif`;
- `else`;
- `try`;
- `except`;
- `ValueError`;
- `ZeroDivisionError`;
- tratamento de exceções;
- validação de dados;
- definição de funções com `def`;
- chamada de funções;
- parâmetros;
- argumentos;
- `return`;
- funções reutilizáveis;
- decomposição de problemas;
- modularização;
- funções recursivas;
- recursão;
- menus;
- cálculos geométricos;
- operações matemáticas;
- estatísticas básicas;
- f-strings;
- formatação de resultados;
- entrada, processamento e saída de dados.

---

## 📊 Desafios concluídos

| Nº | Desafio | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Divisão segura | [`desafio01_divisao_segura.py`](desafio01_divisao_segura.py) | `try/except` e divisão por zero | ✅ |
| 02 | Média de notas segura | [`desafio02_media_notas_segura.py`](desafio02_media_notas_segura.py) | Validação, exceções e funções | ✅ |
| 03 | Conversor seguro | [`desafio03_conversor_seguro.py`](desafio03_conversor_seguro.py) | Conversão e tratamento de exceções | ✅ |
| 04 | Calculadora com funções | [`desafio04_calculadora_funcoes.py`](desafio04_calculadora_funcoes.py) | Modularização e funções | ✅ |
| 05 | Fatorial seguro | [`desafio05_fatorial_seguro.py`](desafio05_fatorial_seguro.py) | Recursão e validação | ✅ |
| 06 | Validação de idade | [`desafio06_validacao_idade.py`](desafio06_validacao_idade.py) | Função, validação e exceção | ✅ |
| 07 | Menu modular | [`desafio07_menu_modular.py`](desafio07_menu_modular.py) | Decomposição e funções | ✅ |
| 08 | Geometria modular | [`desafio08_geometria_modular.py`](desafio08_geometria_modular.py) | Várias funções reutilizáveis | ✅ |
| 09 | Estatísticas de números | [`desafio09_estatisticas_numeros.py`](desafio09_estatisticas_numeros.py) | Funções e estatísticas | ✅ |
| 10 | Calculadora avançada | [`desafio10_calculadora_avancada.py`](desafio10_calculadora_avancada.py) | Integração dos conteúdos da Semana 03 | ✅ |

---

## 🔎 Descrição dos desafios

### 01 — Divisão segura

O programa solicita dois números e realiza uma divisão utilizando tratamento de exceções.

São tratadas duas situações principais:

- entrada que não possa ser convertida para número;
- tentativa de divisão por zero.

Exemplo de tratamento:

```python
try:
    resultado = numero1 / numero2

except ValueError:
    print("Entrada inválida.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Principais conceitos:

- `try`;
- `except`;
- `ValueError`;
- `ZeroDivisionError`;
- conversão para `float`;
- divisão;
- tratamento de erros.

Arquivo: [`desafio01_divisao_segura.py`](desafio01_divisao_segura.py)

---

### 02 — Média de notas segura

O programa trabalha com notas e cálculo de média, combinando funções e validação das entradas.

A lógica é separada em funções para tornar o código mais organizado e reutilizável.

Principais conceitos:

- definição de funções;
- parâmetros;
- retorno de valores;
- conversão para `float`;
- média aritmética;
- validação;
- tratamento de exceções.

Arquivo: [`desafio02_media_notas_segura.py`](desafio02_media_notas_segura.py)

---

### 03 — Conversor seguro

O programa realiza conversões numéricas utilizando tratamento de exceções para impedir que entradas inválidas interrompam sua execução.

Principais conceitos:

- entrada de dados;
- conversão numérica;
- `try`;
- `except`;
- `ValueError`;
- validação;
- tratamento de exceções;
- apresentação de resultados.

Arquivo: [`desafio03_conversor_seguro.py`](desafio03_conversor_seguro.py)

---

### 04 — Calculadora com funções

O programa implementa operações de uma calculadora por meio de funções independentes.

Exemplo de decomposição:

```python
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b
```

A separação das operações em funções reduz repetição de código e facilita sua manutenção.

Principais conceitos:

- `def`;
- parâmetros;
- argumentos;
- `return`;
- decomposição;
- modularização;
- operações aritméticas.

Arquivo: [`desafio04_calculadora_funcoes.py`](desafio04_calculadora_funcoes.py)

---

### 05 — Fatorial seguro

O programa calcula o fatorial de um número utilizando uma função recursiva e validação dos dados informados.

Conceitualmente:

```text
n! = n × (n - 1)!
```

Caso-base:

```text
0! = 1
1! = 1
```

A recursão ocorre quando uma função chama a si própria até atingir uma condição de parada.

Principais conceitos:

- funções;
- recursão;
- caso-base;
- retorno de valores;
- validação;
- tratamento de entradas inválidas.

Arquivo: [`desafio05_fatorial_seguro.py`](desafio05_fatorial_seguro.py)

---

### 06 — Validação de idade

O programa recebe uma idade e realiza sua validação antes de prosseguir com o processamento.

A atividade reforça a separação entre:

```text
entrada
    ↓
validação
    ↓
processamento
    ↓
saída
```

Principais conceitos:

- função;
- parâmetros;
- validação;
- conversão para `int`;
- estruturas condicionais;
- tratamento de exceções.

Arquivo: [`desafio06_validacao_idade.py`](desafio06_validacao_idade.py)

---

### 07 — Menu modular

O programa organiza um menu em partes menores, utilizando funções para separar as diferentes responsabilidades da aplicação.

A estrutura modular evita concentrar toda a lógica em um único bloco de código.

Exemplo conceitual:

```python
def exibir_menu():
    pass


def executar_opcao():
    pass
```

Principais conceitos:

- decomposição de problemas;
- modularização;
- funções;
- menus;
- estruturas condicionais;
- reutilização de código;
- organização lógica.

Arquivo: [`desafio07_menu_modular.py`](desafio07_menu_modular.py)

---

### 08 — Geometria modular

O programa reúne cálculos geométricos organizados em diferentes funções.

Cada cálculo pode ser implementado de forma independente, permitindo reutilização e manutenção mais simples.

Exemplo conceitual:

```python
def area_retangulo(base, altura):
    return base * altura
```

Principais conceitos:

- várias funções;
- parâmetros;
- `return`;
- cálculos geométricos;
- modularização;
- reutilização de código;
- organização do programa.

Arquivo: [`desafio08_geometria_modular.py`](desafio08_geometria_modular.py)

---

### 09 — Estatísticas de números

O programa processa valores numéricos e utiliza funções reutilizáveis para produzir informações estatísticas.

O desafio reforça a ideia de separar cada responsabilidade em uma função específica.

Principais conceitos:

- funções;
- reutilização de código;
- cálculos numéricos;
- estatísticas;
- organização dos dados;
- parâmetros;
- retorno de valores.

Arquivo: [`desafio09_estatisticas_numeros.py`](desafio09_estatisticas_numeros.py)

---

### 10 — Calculadora avançada

O desafio final integra diferentes conteúdos trabalhados durante a Semana 03 em uma aplicação mais completa.

A calculadora combina:

- funções;
- decomposição;
- modularização;
- validação;
- tratamento de exceções;
- operações matemáticas;
- organização do fluxo do programa.

Esse desafio funciona como exercício de consolidação da Semana 03, reunindo conceitos estudados nos desafios anteriores.

Principais conceitos:

- funções;
- parâmetros;
- `return`;
- modularização;
- tratamento de exceções;
- validação;
- menu;
- operações aritméticas;
- reutilização de código;
- integração de conhecimentos.

Arquivo: [`desafio10_calculadora_avancada.py`](desafio10_calculadora_avancada.py)

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
- definição das funções;
- entrada de dados;
- processamento;
- tratamento de exceções;
- saída de dados.

Exemplo da estrutura utilizada:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 03 - Tratamento de Exceções e Modularização
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
├── desafio01_divisao_segura.py
├── desafio02_media_notas_segura.py
├── desafio03_conversor_seguro.py
├── desafio04_calculadora_funcoes.py
├── desafio05_fatorial_seguro.py
├── desafio06_validacao_idade.py
├── desafio07_menu_modular.py
├── desafio08_geometria_modular.py
├── desafio09_estatisticas_numeros.py
└── desafio10_calculadora_avancada.py
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
python semana-03\03-desafios-extras\desafio01_divisao_segura.py
```

Exemplo para executar o desafio de fatorial:

```bat
python semana-03\03-desafios-extras\desafio05_fatorial_seguro.py
```

Exemplo para executar o desafio final:

```bat
python semana-03\03-desafios-extras\desafio10_calculadora_avancada.py
```

---

## 💡 Aprendizados consolidados

A conclusão desta etapa permitiu desenvolver e consolidar as seguintes competências:

- interpretar problemas e transformá-los em algoritmos;
- decompor problemas maiores em partes menores;
- definir funções;
- utilizar parâmetros e argumentos;
- retornar valores com `return`;
- reutilizar funções;
- reduzir repetição de código;
- organizar programas em blocos lógicos;
- aplicar tratamento de exceções;
- tratar entradas inválidas com `ValueError`;
- tratar divisão por zero com `ZeroDivisionError`;
- validar dados antes do processamento;
- compreender o fluxo `try/except`;
- desenvolver funções recursivas;
- compreender o caso-base da recursão;
- modularizar operações;
- separar responsabilidades;
- criar menus organizados;
- implementar cálculos geométricos;
- trabalhar com cálculos estatísticos;
- testar programas com diferentes entradas;
- interpretar mensagens de erro;
- corrigir problemas de sintaxe e lógica;
- documentar os códigos;
- versionar cada desafio separadamente;
- publicar a evolução dos estudos no GitHub.

---

## 📈 Progresso

| Indicador | Resultado |
|---|---:|
| Desafios planejados | 10 |
| Desafios concluídos | 10 |
| Total de arquivos Python | 10 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

## ✅ Status da etapa

> **Etapa concluída:** todos os 10 desafios extras planejados para a Semana 03 foram desenvolvidos, testados, documentados, versionados individualmente e publicados no GitHub.

Os desafios extras permanecem identificados como **atividades complementares e autorais de consolidação**, sem serem confundidos com as práticas e os exercícios oficiais do curso.

---

## 🔗 Navegação

- [⬅️ Voltar para a Semana 03](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🧩 Acessar os exercícios oficiais](../02-exercicios/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.
