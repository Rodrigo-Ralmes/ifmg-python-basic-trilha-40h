# 🐍 Semana 01 — Fundamentos de Python

Esta pasta reúne todo o conteúdo prático desenvolvido durante a **Semana 01** do curso **Python Básico — +IFMG**.

A etapa foi organizada em práticas de aprendizagem, exercícios oficiais e desafios extras, permitindo estudar os fundamentos da linguagem Python e aplicá-los progressivamente na resolução de problemas.

---

## 🎯 Objetivo da semana

O objetivo da Semana 01 é compreender e aplicar os fundamentos iniciais da programação com Python.

Durante esta etapa, foram trabalhados conhecimentos essenciais para a construção dos próximos conteúdos do curso, incluindo:

- raciocínio lógico;
- interpretação de problemas;
- estrutura sequencial;
- entrada de dados;
- processamento de informações;
- saída de dados;
- tipos de dados;
- variáveis;
- operadores;
- funções;
- strings;
- módulos;
- fórmulas matemáticas;
- testes;
- correção de erros;
- documentação;
- versionamento com Git;
- publicação no GitHub.

---

## 🧠 Metodologia de aprendizagem

A Semana 01 foi organizada em três níveis progressivos:

```text
Práticas fundamentais
        ↓
Exercícios oficiais
        ↓
Desafios extras
```

### 1. Práticas fundamentais

As práticas foram utilizadas para conhecer e testar recursos específicos da linguagem Python de forma isolada.

### 2. Exercícios oficiais

Os exercícios permitiram aplicar os conceitos estudados na resolução de problemas estruturados.

### 3. Desafios extras

Os desafios ampliaram o aprendizado por meio de situações envolvendo cálculos, conversões, porcentagens, medidas, condições e formatação de dados.

O processo completo utilizado foi:

```text
Estudo do conteúdo
        ↓
Criação de uma prática
        ↓
Execução no Spyder
        ↓
Resolução de exercício
        ↓
Desenvolvimento de desafio
        ↓
Teste dos resultados
        ↓
Identificação e correção de erros
        ↓
Documentação do código
        ↓
Versionamento com Git
        ↓
Publicação no GitHub
```

---

## 📊 Resumo geral

| Categoria | Planejado | Concluído | Percentual | Status |
|---|---:|---:|---:|:---:|
| Práticas fundamentais | 10 | 10 | 100% | ✅ |
| Exercícios oficiais | 3 | 3 | 100% | ✅ |
| Desafios principais | 11 | 11 | 100% | ✅ |
| Versões ampliadas | 1 | 1 | 100% | ✅ |
| **Total de códigos** | **25** | **25** | **100%** | **✅** |

```text
████████████████████ 100%
```

---

# 🧪 01 — Práticas fundamentais

As práticas foram desenvolvidas para experimentar e compreender os recursos fundamentais da linguagem Python.

Pasta: [`01-praticas`](01-praticas/README.md)

## Práticas concluídas

| Nº | Prática | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Saída de dados com `print()` | [`pratica01_print.py`](01-praticas/pratica01_print.py) | ✅ |
| 02 | Tipos de dados | [`pratica02_tipos_dados.py`](01-praticas/pratica02_tipos_dados.py) | ✅ |
| 03 | Variáveis | [`pratica03_variaveis.py`](01-praticas/pratica03_variaveis.py) | ✅ |
| 04 | Entrada e saída de dados | [`pratica04_input_output.py`](01-praticas/pratica04_input_output.py) | ✅ |
| 05 | Operadores aritméticos | [`pratica05_operadores_aritmeticos.py`](01-praticas/pratica05_operadores_aritmeticos.py) | ✅ |
| 06 | Operadores relacionais | [`pratica06_operadores_relacionais.py`](01-praticas/pratica06_operadores_relacionais.py) | ✅ |
| 07 | Operadores lógicos | [`pratica07_operadores_logicos.py`](01-praticas/pratica07_operadores_logicos.py) | ✅ |
| 08 | Funções | [`pratica08_funcoes.py`](01-praticas/pratica08_funcoes.py) | ✅ |
| 09 | Strings | [`pratica09_strings.py`](01-praticas/pratica09_strings.py) | ✅ |
| 10 | Biblioteca `math` | [`pratica10_math.py`](01-praticas/pratica10_math.py) | ✅ |

## Conteúdos consolidados nas práticas

As práticas permitiram estudar:

- função `print()`;
- tipos `int`, `float`, `str` e `bool`;
- função `type()`;
- criação de variáveis;
- atribuição de valores;
- entrada com `input()`;
- conversão de tipos;
- operadores aritméticos;
- operadores relacionais;
- operadores lógicos;
- criação de funções;
- parâmetros e argumentos;
- retorno de valores;
- strings;
- métodos de strings;
- f-strings;
- importação de módulos;
- biblioteca `math`;
- constantes e funções matemáticas.

Para consultar a documentação completa, acesse:

[📘 Documentação das práticas](01-praticas/README.md)

---

# 🧩 02 — Exercícios oficiais

Os exercícios oficiais foram desenvolvidos para aplicar os conceitos estudados em problemas estruturados.

Pasta: [`02-exercicios`](02-exercicios/README.md)

## Exercícios concluídos

| Nº | Exercício | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Área de um triângulo | [`ex01_area_triangulo.py`](02-exercicios/ex01_area_triangulo.py) | ✅ |
| 02A | Conversão de segundos para HMS | [`ex02a_segundos_para_hms.py`](02-exercicios/ex02a_segundos_para_hms.py) | ✅ |
| 03 | Cálculo de juros simples | [`ex03_juros_simples.py`](02-exercicios/ex03_juros_simples.py) | ✅ |

## Exercício 01 — Área de um triângulo

O programa solicita a base e a altura de um triângulo e calcula sua área.

```text
Área = (base × altura) / 2
```

Principais conceitos:

- `input()`;
- `float()`;
- multiplicação;
- divisão;
- cálculo de área;
- saída formatada.

---

## Exercício 02A — Conversão de segundos para HMS

O programa solicita uma quantidade total de segundos e converte o valor informado para horas, minutos e segundos.

```text
Horas = total de segundos // 3600
Restante = total de segundos % 3600
Minutos = restante // 60
Segundos = restante % 60
```

Principais conceitos:

- `input()`;
- `int()`;
- divisão inteira;
- operador de resto;
- conversão de tempo;
- saída formatada.

---

## Exercício 03 — Cálculo de juros simples

O programa solicita o capital inicial, a taxa de juros e a quantidade de períodos. Depois, calcula os juros e o montante final.

```text
Taxa decimal = Taxa percentual / 100
Juros = Capital × Taxa decimal × Tempo
Montante = Capital + Juros
```

Principais conceitos:

- `input()`;
- `float()`;
- `int()`;
- porcentagem;
- juros simples;
- montante;
- formatação monetária.

Para consultar a documentação completa, acesse:

[📘 Documentação dos exercícios oficiais](02-exercicios/README.md)

---

# 🚀 03 — Desafios extras

Os desafios extras foram desenvolvidos para ampliar e consolidar os conhecimentos adquiridos durante a semana.

Pasta: [`03-desafios-extras`](03-desafios-extras/README.md)

## Desafios concluídos

| Nº | Desafio | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Média de duas notas | [`desafio01_media_duas_notas.py`](03-desafios-extras/desafio01_media_duas_notas.py) | ✅ |
| 02 | Conversor de temperatura | [`desafio02_conversor_temperatura.py`](03-desafios-extras/desafio02_conversor_temperatura.py) | ✅ |
| 02.01 | Conversor de temperatura ampliado | [`desafio02_01_conversor_temperatura.py`](03-desafios-extras/desafio02_01_conversor_temperatura.py) | ✅ |
| 03 | Calculadora de IMC | [`desafio03_calculadora_imc.py`](03-desafios-extras/desafio03_calculadora_imc.py) | ✅ |
| 04 | Salário por horas trabalhadas | [`desafio04_salario_horas_trabalhadas.py`](03-desafios-extras/desafio04_salario_horas_trabalhadas.py) | ✅ |
| 05 | Consumo de combustível | [`desafio05_consumo_combustivel.py`](03-desafios-extras/desafio05_consumo_combustivel.py) | ✅ |
| 06 | Conversor de metros | [`desafio06_conversor_metros.py`](03-desafios-extras/desafio06_conversor_metros.py) | ✅ |
| 07 | Preço com desconto | [`desafio07_preco_com_desconto.py`](03-desafios-extras/desafio07_preco_com_desconto.py) | ✅ |
| 08 | Reajuste salarial | [`desafio08_reajuste_salarial.py`](03-desafios-extras/desafio08_reajuste_salarial.py) | ✅ |
| 09 | Circunferência | [`desafio09_circunferencia.py`](03-desafios-extras/desafio09_circunferencia.py) | ✅ |
| 10 | Hipotenusa | [`desafio10_hipotenusa.py`](03-desafios-extras/desafio10_hipotenusa.py) | ✅ |
| 11 | Formatação de dados do usuário | [`desafio11_formatacao_dados_usuario.py`](03-desafios-extras/desafio11_formatacao_dados_usuario.py) | ✅ |

## Conteúdos consolidados nos desafios

Os desafios permitiram aplicar:

- média aritmética;
- conversão de temperaturas;
- estruturas condicionais;
- cálculo de IMC;
- cálculo salarial;
- consumo médio de combustível;
- conversão de unidades;
- porcentagem;
- desconto;
- reajuste salarial;
- comprimento da circunferência;
- área do círculo;
- exponenciação;
- Teorema de Pitágoras;
- módulo `math`;
- raiz quadrada;
- manipulação de strings;
- formatação de dados.

Para consultar a documentação completa, acesse:

[📘 Documentação dos desafios extras](03-desafios-extras/README.md)

---

## 🧮 Fórmulas utilizadas

Durante a Semana 01, diferentes fórmulas foram implementadas em Python.

### Área do triângulo

```text
Área = (base × altura) / 2
```

```python
area = (base * altura) / 2
```

### Média aritmética

```text
Média = (nota 1 + nota 2) / 2
```

```python
media = (nota1 + nota2) / 2
```

### Celsius para Fahrenheit

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

```python
fahrenheit = (celsius * 9 / 5) + 32
```

### Fahrenheit para Celsius

```text
Celsius = (Fahrenheit - 32) / 1,8
```

```python
celsius = (fahrenheit - 32) / 1.8
```

### Índice de Massa Corporal

```text
IMC = peso / altura²
```

```python
imc = peso / (altura ** 2)
```

### Salário por horas trabalhadas

```text
Salário = horas trabalhadas × valor da hora
```

```python
salario = horas_trabalhadas * valor_hora
```

### Consumo médio de combustível

```text
Consumo médio = distância / combustível
```

```python
consumo_medio = distancia / combustivel
```

### Valor do desconto

```text
Desconto = preço × (percentual / 100)
```

```python
valor_desconto = preco * (percentual_desconto / 100)
```

### Preço final

```text
Preço final = preço - desconto
```

```python
preco_final = preco - valor_desconto
```

### Reajuste salarial

```text
Reajuste = salário × (percentual / 100)
Novo salário = salário + reajuste
```

```python
valor_reajuste = salario * (percentual / 100)
salario_novo = salario + valor_reajuste
```

### Comprimento da circunferência

```text
Comprimento = 2 × π × raio
```

```python
comprimento = 2 * pi * raio
```

### Área do círculo

```text
Área = π × raio²
```

```python
area = pi * (raio ** 2)
```

### Hipotenusa

```text
Hipotenusa = √(cateto 1² + cateto 2²)
```

```python
hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))
```

---

## 🔢 Operadores estudados

### Operadores aritméticos

| Operador | Descrição | Exemplo |
|:---:|---|---|
| `+` | Adição | `10 + 5` |
| `-` | Subtração | `10 - 5` |
| `*` | Multiplicação | `10 * 5` |
| `/` | Divisão | `10 / 5` |
| `//` | Divisão inteira | `10 // 3` |
| `%` | Resto da divisão | `10 % 3` |
| `**` | Exponenciação | `10 ** 2` |

### Operadores relacionais

| Operador | Descrição |
|:---:|---|
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |

### Operadores lógicos

| Operador | Descrição |
|:---:|---|
| `and` | Todas as condições devem ser verdadeiras |
| `or` | Pelo menos uma condição deve ser verdadeira |
| `not` | Inverte o resultado lógico |

---

## ⚠️ Erros identificados e aprendizados

Durante o desenvolvimento, alguns erros contribuíram diretamente para o aprendizado.

### Utilização de `^` como potência

Código incorreto:

```python
area = pi * (raio ^ 2)
```

O operador `^` representa uma operação XOR bit a bit e não uma potência.

Código correto:

```python
area = pi * (raio ** 2)
```

---

### Sobrescrita da função `print()`

Código incorreto:

```python
print = f"Resultado: {valor}"
```

Esse comando cria uma variável chamada `print` e substitui temporariamente a referência à função nativa.

Código correto:

```python
print(f"Resultado: {valor}")
```

---

### Entrada decimal com vírgula

Por padrão, o Python espera o ponto como separador decimal:

```text
7.6
```

A entrada abaixo pode produzir erro durante a conversão para `float`:

```text
7,6
```

---

### Caminho duplicado no Git

Quando o terminal já está dentro da pasta de um arquivo, basta utilizar seu nome:

```bat
git add arquivo.py
```

Não é necessário repetir todo o caminho desde a raiz.

---

### `push` antes do `commit`

O comando `git push` publica commits existentes.

A sequência correta é:

```text
Alterar o arquivo
      ↓
git add
      ↓
git commit
      ↓
git push
```

---

## 🗂️ Padrão de organização dos códigos

Os exercícios e desafios foram organizados com um cabeçalho contendo:

- curso;
- trilha;
- semana;
- tipo da atividade;
- número e título;
- nome do arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status da atividade.

Estrutura utilizada:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Prática, exercício oficial ou desafio extra
# Atividade: número e título
# Arquivo: nome_do_arquivo.py
# Autor: Rodrigo de Almeida Silveira
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

Os programas mais estruturados também foram separados em:

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

---

## 📁 Estrutura da Semana 01

```text
semana-01/
├── README.md
│
├── 01-praticas/
│   ├── README.md
│   ├── pratica01_print.py
│   ├── pratica02_tipos_dados.py
│   ├── pratica03_variaveis.py
│   ├── pratica04_input_output.py
│   ├── pratica05_operadores_aritmeticos.py
│   ├── pratica06_operadores_relacionais.py
│   ├── pratica07_operadores_logicos.py
│   ├── pratica08_funcoes.py
│   ├── pratica09_strings.py
│   └── pratica10_math.py
│
├── 02-exercicios/
│   ├── README.md
│   ├── ex01_area_triangulo.py
│   ├── ex02a_segundos_para_hms.py
│   └── ex03_juros_simples.py
│
└── 03-desafios-extras/
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

## ▶️ Como executar os códigos

### Execução pelo Spyder

1. Abra o Spyder.
2. Acesse a pasta do projeto.
3. Abra o arquivo desejado.
4. Execute o programa.
5. Informe os valores solicitados.
6. Verifique o resultado no console.

### Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

Exemplo de prática:

```bat
python semana-01\01-praticas\pratica01_print.py
```

Exemplo de exercício oficial:

```bat
python semana-01\02-exercicios\ex01_area_triangulo.py
```

Exemplo de desafio extra:

```bat
python semana-01\03-desafios-extras\desafio01_media_duas_notas.py
```

---

## 🔄 Fluxo de versionamento utilizado

Cada código foi versionado individualmente seguindo esta sequência:

```bat
git status
git add nome_do_arquivo.py
git status
git commit -m "feat: adiciona descrição da atividade"
git push
git status
```

Para alterações exclusivamente documentais, foi utilizado o prefixo `docs`:

```bat
git status
git add README.md
git status
git commit -m "docs: atualiza documentação da semana 01"
git push
git status
```

### Convenção utilizada nos commits

| Prefixo | Utilização |
|---|---|
| `feat` | Inclusão de uma prática, exercício ou desafio |
| `docs` | Criação ou atualização de documentação |
| `fix` | Correção de um erro no código |
| `refactor` | Reorganização do código sem mudar o resultado |

---

## 💡 Aprendizados consolidados

Ao concluir a Semana 01, foram consolidados os seguintes aprendizados:

### Programação

- compreender o funcionamento básico do Python;
- criar e executar arquivos `.py`;
- exibir informações no console;
- trabalhar com diferentes tipos de dados;
- armazenar valores em variáveis;
- solicitar informações ao usuário;
- converter dados para `int` e `float`;
- realizar operações aritméticas;
- comparar valores;
- combinar condições;
- criar funções;
- utilizar parâmetros e retornos;
- manipular strings;
- importar e utilizar módulos;
- aplicar fórmulas matemáticas;
- formatar valores numéricos e monetários.

### Raciocínio lógico

- interpretar enunciados;
- identificar os dados de entrada;
- determinar o processamento necessário;
- apresentar resultados;
- dividir problemas em etapas menores;
- testar diferentes valores;
- conferir os resultados manualmente;
- identificar erros de sintaxe;
- identificar erros de lógica;
- corrigir implementações.

### Organização

- padronizar cabeçalhos;
- separar entrada, processamento e saída;
- utilizar nomes de variáveis descritivos;
- organizar práticas, exercícios e desafios;
- documentar os conteúdos estudados;
- criar READMEs específicos para cada pasta.

### Git e GitHub

- verificar alterações com `git status`;
- selecionar arquivos com `git add`;
- registrar alterações com `git commit`;
- publicar commits com `git push`;
- compreender a diferença entre arquivos não rastreados e preparados;
- criar commits individuais;
- utilizar mensagens de commit descritivas;
- verificar a sincronização com o GitHub;
- acompanhar a evolução do projeto pelo histórico de commits.

---

## 🏆 Resultados da Semana 01

A Semana 01 foi concluída com:

- **10 práticas fundamentais**;
- **3 exercícios oficiais**;
- **11 desafios principais**;
- **1 versão ampliada**;
- **25 arquivos Python**;
- documentação específica para cada categoria;
- códigos testados no Spyder;
- versionamento individual;
- publicação completa no GitHub.

---

## ✅ Status da semana

> **Semana 01 concluída com sucesso:** todos os conteúdos planejados foram estudados, implementados, testados, documentados, versionados e publicados no GitHub.

---

## 🔗 Navegação

- [🧪 Práticas fundamentais](01-praticas/README.md)
- [🧩 Exercícios oficiais](02-exercicios/README.md)
- [🚀 Desafios extras](03-desafios-extras/README.md)
- [🏠 Voltar ao início do repositório](../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.