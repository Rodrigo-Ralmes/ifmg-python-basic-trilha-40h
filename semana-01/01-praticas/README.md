# 🧪 Práticas — Semana 01

Esta pasta reúne as práticas desenvolvidas durante a **Semana 01** do curso **Python Básico — +IFMG**.

As atividades foram utilizadas para experimentar, testar e consolidar os fundamentos iniciais da linguagem Python antes da aplicação desses conhecimentos em exercícios e desafios mais estruturados.

---

## 🎯 Objetivo

O objetivo desta etapa é transformar os conteúdos estudados em pequenas implementações práticas, permitindo observar diretamente o funcionamento da linguagem Python.

Cada arquivo apresenta um conteúdo específico, facilitando:

- a compreensão dos conceitos fundamentais;
- a realização de testes isolados;
- a identificação dos tipos de dados;
- o uso de variáveis;
- a entrada e saída de informações;
- a aplicação de operadores;
- a criação de funções;
- a manipulação de strings;
- a utilização do módulo `math`;
- o desenvolvimento progressivo do raciocínio lógico.

---

## 🧠 Metodologia

As práticas foram desenvolvidas de maneira progressiva.

Cada novo arquivo acrescenta um conceito ou recurso da linguagem Python:

```text
Saída de dados
      ↓
Tipos de dados
      ↓
Variáveis
      ↓
Entrada de dados
      ↓
Operadores aritméticos
      ↓
Operadores relacionais
      ↓
Operadores lógicos
      ↓
Funções
      ↓
Strings
      ↓
Módulo math
```

O processo utilizado em cada prática foi:

1. leitura do conteúdo;
2. identificação do conceito principal;
3. criação de exemplos;
4. execução no Spyder;
5. observação dos resultados no console;
6. alteração dos valores para novos testes;
7. correção de possíveis erros;
8. documentação do código;
9. versionamento individual com Git;
10. publicação no GitHub.

---

## 📚 Conteúdos relacionados

As práticas desta etapa envolvem os seguintes conteúdos:

- `print()`;
- comentários;
- tipos de dados;
- `int`;
- `float`;
- `str`;
- `bool`;
- variáveis;
- atribuição de valores;
- `input()`;
- conversão de tipos;
- operadores aritméticos;
- operadores relacionais;
- operadores lógicos;
- criação de funções;
- parâmetros;
- retorno de valores;
- strings;
- concatenação;
- métodos de strings;
- f-strings;
- importação de módulos;
- módulo `math`;
- constantes matemáticas;
- funções matemáticas.

---

## 📊 Práticas concluídas

| Nº | Prática | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Saída de dados com `print()` | [`pratica01_print.py`](pratica01_print.py) | Exibição de informações no console | ✅ |
| 02 | Tipos de dados | [`pratica02_tipos_dados.py`](pratica02_tipos_dados.py) | `int`, `float`, `str` e `bool` | ✅ |
| 03 | Variáveis | [`pratica03_variaveis.py`](pratica03_variaveis.py) | Criação, atribuição e utilização de variáveis | ✅ |
| 04 | Entrada e saída de dados | [`pratica04_input_output.py`](pratica04_input_output.py) | `input()`, conversão de tipos e `print()` | ✅ |
| 05 | Operadores aritméticos | [`pratica05_operadores_aritmeticos.py`](pratica05_operadores_aritmeticos.py) | Operações matemáticas em Python | ✅ |
| 06 | Operadores relacionais | [`pratica06_operadores_relacionais.py`](pratica06_operadores_relacionais.py) | Comparação entre valores | ✅ |
| 07 | Operadores lógicos | [`pratica07_operadores_logicos.py`](pratica07_operadores_logicos.py) | `and`, `or` e `not` | ✅ |
| 08 | Funções | [`pratica08_funcoes.py`](pratica08_funcoes.py) | Criação e chamada de funções | ✅ |
| 09 | Strings | [`pratica09_strings.py`](pratica09_strings.py) | Manipulação e formatação de textos | ✅ |
| 10 | Biblioteca `math` | [`pratica10_math.py`](pratica10_math.py) | Funções e constantes matemáticas | ✅ |

---

## 🔎 Descrição das práticas

### 01 — Saída de dados com `print()`

A primeira prática apresenta a função `print()`, utilizada para exibir informações no console.

Exemplo:

```python
print("Olá, Python!")
```

A função também pode apresentar números:

```python
print(10)
print(3.14)
```

Diferentes informações podem ser exibidas separadamente:

```python
print("Curso: Python Básico")
print("Instituição: +IFMG")
print("Semana: 01")
```

Também é possível apresentar vários elementos em uma única instrução:

```python
print("Python", "Big Data", "Programação")
```

### Principais conceitos

- função `print()`;
- saída de dados;
- textos;
- números inteiros;
- números decimais;
- apresentação de vários valores;
- execução de comandos;
- observação dos resultados no console.

Arquivo: [`pratica01_print.py`](pratica01_print.py)

---

### 02 — Tipos de dados

Esta prática apresenta alguns dos principais tipos de dados existentes em Python.

#### Números inteiros

Os números inteiros pertencem ao tipo `int`.

```python
idade = 47
```

#### Números decimais

Os números com casas decimais pertencem ao tipo `float`.

```python
altura = 1.74
```

#### Textos

Os valores textuais pertencem ao tipo `str`.

```python
nome = "Rodrigo"
```

#### Valores lógicos

Os valores `True` e `False` pertencem ao tipo `bool`.

```python
curso_concluido = True
```

A função `type()` permite verificar o tipo de determinado valor ou variável:

```python
print(type(idade))
print(type(altura))
print(type(nome))
print(type(curso_concluido))
```

Resultado esperado:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### Principais conceitos

- tipos de dados;
- `int`;
- `float`;
- `str`;
- `bool`;
- valores numéricos;
- valores textuais;
- valores lógicos;
- função `type()`.

Arquivo: [`pratica02_tipos_dados.py`](pratica02_tipos_dados.py)

---

### 03 — Variáveis

Uma variável é um espaço utilizado para armazenar um valor durante a execução do programa.

Exemplo:

```python
nome = "Rodrigo"
idade = 47
altura = 1.74
```

Nesse exemplo:

- `nome` armazena uma string;
- `idade` armazena um número inteiro;
- `altura` armazena um número decimal.

Os valores armazenados podem ser utilizados posteriormente:

```python
print(nome)
print(idade)
print(altura)
```

Também é possível realizar cálculos utilizando variáveis:

```python
numero1 = 10
numero2 = 5
resultado = numero1 + numero2

print(resultado)
```

### Boas práticas para nomes de variáveis

Os nomes devem ser claros e descritivos:

```python
salario_mensal = 3500.00
quantidade_horas = 160
nome_completo = "Rodrigo de Almeida Silveira"
```

Evite nomes pouco explicativos:

```python
x = 3500.00
y = 160
z = "Rodrigo"
```

### Principais conceitos

- criação de variáveis;
- atribuição de valores;
- armazenamento de dados;
- reutilização de valores;
- atualização de variáveis;
- nomes descritivos;
- convenção `snake_case`.

Arquivo: [`pratica03_variaveis.py`](pratica03_variaveis.py)

---

### 04 — Entrada e saída de dados

A função `input()` permite solicitar uma informação ao usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")
```

Por padrão, o valor recebido por `input()` é uma string.

Para trabalhar com números, é necessário converter a entrada.

#### Conversão para inteiro

```python
idade = int(input("Digite sua idade: "))
```

#### Conversão para número decimal

```python
altura = float(input("Digite sua altura: "))
```

Os valores podem ser apresentados com `print()`:

```python
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
```

### Exemplo de execução

```text
Digite seu nome: Rodrigo
Digite sua idade: 47
Digite sua altura: 1.74

Nome: Rodrigo
Idade: 47 anos
Altura: 1.74 m
```

### Principais conceitos

- função `input()`;
- entrada de dados;
- conversão para `int`;
- conversão para `float`;
- armazenamento em variáveis;
- função `print()`;
- f-strings;
- formatação decimal.

Arquivo: [`pratica04_input_output.py`](pratica04_input_output.py)

---

### 05 — Operadores aritméticos

Os operadores aritméticos são utilizados para realizar cálculos matemáticos.

Considere:

```python
numero1 = 10
numero2 = 3
```

#### Adição

```python
soma = numero1 + numero2
```

#### Subtração

```python
subtracao = numero1 - numero2
```

#### Multiplicação

```python
multiplicacao = numero1 * numero2
```

#### Divisão

```python
divisao = numero1 / numero2
```

#### Divisão inteira

```python
divisao_inteira = numero1 // numero2
```

#### Resto da divisão

```python
resto = numero1 % numero2
```

#### Exponenciação

```python
potencia = numero1 ** numero2
```

### Resumo dos operadores

| Operador | Operação | Exemplo |
|:---:|---|---|
| `+` | Adição | `10 + 3` |
| `-` | Subtração | `10 - 3` |
| `*` | Multiplicação | `10 * 3` |
| `/` | Divisão | `10 / 3` |
| `//` | Divisão inteira | `10 // 3` |
| `%` | Resto da divisão | `10 % 3` |
| `**` | Exponenciação | `10 ** 3` |

### Principais conceitos

- operadores aritméticos;
- adição;
- subtração;
- multiplicação;
- divisão;
- divisão inteira;
- operador de resto;
- exponenciação;
- precedência das operações.

Arquivo: [`pratica05_operadores_aritmeticos.py`](pratica05_operadores_aritmeticos.py)

---

### 06 — Operadores relacionais

Os operadores relacionais comparam dois valores.

O resultado de uma comparação é sempre:

```python
True
```

ou:

```python
False
```

Considere:

```python
numero1 = 10
numero2 = 5
```

Exemplos:

```python
print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)
```

### Resumo dos operadores

| Operador | Significado | Exemplo |
|:---:|---|---|
| `==` | Igual a | `10 == 5` |
| `!=` | Diferente de | `10 != 5` |
| `>` | Maior que | `10 > 5` |
| `<` | Menor que | `10 < 5` |
| `>=` | Maior ou igual a | `10 >= 5` |
| `<=` | Menor ou igual a | `10 <= 5` |

### Atenção

O operador `=` atribui um valor a uma variável:

```python
idade = 47
```

O operador `==` realiza uma comparação:

```python
idade == 47
```

### Principais conceitos

- comparação de valores;
- igualdade;
- diferença;
- maior que;
- menor que;
- maior ou igual;
- menor ou igual;
- resultados booleanos.

Arquivo: [`pratica06_operadores_relacionais.py`](pratica06_operadores_relacionais.py)

---

### 07 — Operadores lógicos

Os operadores lógicos permitem combinar ou inverter condições.

Os três operadores principais são:

```python
and
or
not
```

#### Operador `and`

Retorna `True` quando todas as condições são verdadeiras:

```python
idade = 47
possui_cadastro = True

resultado = idade >= 18 and possui_cadastro
print(resultado)
```

#### Operador `or`

Retorna `True` quando pelo menos uma condição é verdadeira:

```python
tem_ingresso = False
esta_na_lista = True

resultado = tem_ingresso or esta_na_lista
print(resultado)
```

#### Operador `not`

Inverte um valor lógico:

```python
sistema_bloqueado = False

print(not sistema_bloqueado)
```

### Tabela lógica

| Condição A | Condição B | `A and B` | `A or B` |
|:---:|:---:|:---:|:---:|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

### Principais conceitos

- lógica booleana;
- combinação de condições;
- operador `and`;
- operador `or`;
- operador `not`;
- valores `True` e `False`;
- expressões lógicas.

Arquivo: [`pratica07_operadores_logicos.py`](pratica07_operadores_logicos.py)

---

### 08 — Funções

Uma função é um bloco de código criado para executar uma tarefa específica.

A palavra-chave `def` é utilizada para definir uma função.

Exemplo:

```python
def apresentar_mensagem():
    print("Olá, Python!")
```

Para executar a função, ela deve ser chamada:

```python
apresentar_mensagem()
```

Uma função pode receber parâmetros:

```python
def apresentar_nome(nome):
    print(f"Olá, {nome}!")
```

Chamada:

```python
apresentar_nome("Rodrigo")
```

Uma função também pode retornar um resultado:

```python
def somar(numero1, numero2):
    return numero1 + numero2
```

Utilização:

```python
resultado = somar(10, 5)
print(resultado)
```

### Benefícios das funções

As funções ajudam a:

- organizar o código;
- evitar repetições;
- dividir problemas maiores;
- reaproveitar instruções;
- facilitar testes;
- melhorar a manutenção.

### Principais conceitos

- definição de funções;
- palavra-chave `def`;
- chamada de função;
- parâmetros;
- argumentos;
- palavra-chave `return`;
- retorno de valores;
- reutilização de código.

Arquivo: [`pratica08_funcoes.py`](pratica08_funcoes.py)

---

### 09 — Strings

Strings são sequências de caracteres utilizadas para armazenar textos.

Exemplo:

```python
nome = "Rodrigo de Almeida Silveira"
```

É possível concatenar strings com o operador `+`:

```python
nome = "Rodrigo"
sobrenome = "Silveira"

nome_completo = nome + " " + sobrenome
print(nome_completo)
```

Também é possível utilizar f-strings:

```python
print(f"Nome completo: {nome_completo}")
```

### Métodos de strings

#### Converter para letras maiúsculas

```python
print(nome.upper())
```

#### Converter para letras minúsculas

```python
print(nome.lower())
```

#### Formatar as iniciais

```python
print(nome.title())
```

#### Remover espaços externos

```python
texto = "  Python  "
print(texto.strip())
```

#### Substituir parte do texto

```python
mensagem = "Estou aprendendo Java"
print(mensagem.replace("Java", "Python"))
```

#### Contar caracteres

```python
print(len(nome))
```

### Principais conceitos

- strings;
- caracteres;
- concatenação;
- f-strings;
- método `upper()`;
- método `lower()`;
- método `title()`;
- método `strip()`;
- método `replace()`;
- função `len()`.

Arquivo: [`pratica09_strings.py`](pratica09_strings.py)

---

### 10 — Biblioteca `math`

O módulo `math` disponibiliza constantes e funções matemáticas.

Para utilizá-lo, é necessário realizar sua importação:

```python
import math
```

### Constante π

```python
print(math.pi)
```

### Raiz quadrada

```python
raiz = math.sqrt(25)
print(raiz)
```

### Potência

```python
potencia = math.pow(2, 3)
print(potencia)
```

Também é possível utilizar o operador `**`:

```python
potencia = 2 ** 3
```

### Arredondamento para cima

```python
print(math.ceil(4.2))
```

### Arredondamento para baixo

```python
print(math.floor(4.8))
```

### Fatorial

```python
print(math.factorial(5))
```

### Exemplos de utilização

Cálculo da área de um círculo:

```python
raio = 5
area = math.pi * (raio ** 2)

print(f"Área: {area:.2f}")
```

Cálculo da hipotenusa:

```python
cateto1 = 3
cateto2 = 4

hipotenusa = math.sqrt((cateto1 ** 2) + (cateto2 ** 2))

print(f"Hipotenusa: {hipotenusa:.2f}")
```

### Principais conceitos

- importação de módulos;
- módulo `math`;
- constante `math.pi`;
- função `math.sqrt()`;
- função `math.pow()`;
- função `math.ceil()`;
- função `math.floor()`;
- função `math.factorial()`;
- cálculos matemáticos.

Arquivo: [`pratica10_math.py`](pratica10_math.py)

---

## 🗂️ Organização dos códigos

Os arquivos seguem um padrão de documentação contendo:

- curso;
- trilha;
- semana;
- tipo da atividade;
- número e nome da prática;
- nome do arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status;
- implementação dos exemplos;
- saída de dados.

Exemplo do cabeçalho utilizado:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 01
# Tipo: Prática de aprendizagem
# Prática: número e nome da prática
# Arquivo: nome_do_arquivo.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Descrição do objetivo da prática.
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
01-praticas/
├── README.md
├── pratica01_print.py
├── pratica02_tipos_dados.py
├── pratica03_variaveis.py
├── pratica04_input_output.py
├── pratica05_operadores_aritmeticos.py
├── pratica06_operadores_relacionais.py
├── pratica07_operadores_logicos.py
├── pratica08_funcoes.py
├── pratica09_strings.py
└── pratica10_math.py
```

---

## ▶️ Como executar

### Execução pelo Spyder

1. Abra o Spyder.
2. Acesse a pasta `semana-01/01-praticas`.
3. Abra o arquivo desejado.
4. Execute o programa.
5. Observe os resultados no console.
6. Altere os valores para realizar novos testes.

### Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

Execute uma prática:

```bat
python semana-01\01-praticas\pratica01_print.py
```

Exemplo para executar a prática sobre funções:

```bat
python semana-01\01-praticas\pratica08_funcoes.py
```

Exemplo para executar a prática sobre strings:

```bat
python semana-01\01-praticas\pratica09_strings.py
```

Exemplo para executar a prática sobre o módulo `math`:

```bat
python semana-01\01-praticas\pratica10_math.py
```

---

## 💡 Aprendizados consolidados

A conclusão das práticas permitiu desenvolver e consolidar os seguintes conhecimentos:

- exibir informações no console;
- diferenciar os principais tipos de dados;
- verificar tipos com `type()`;
- criar e utilizar variáveis;
- atribuir valores;
- solicitar dados ao usuário;
- converter entradas para `int` e `float`;
- realizar operações aritméticas;
- compreender divisão comum e divisão inteira;
- obter o resto de uma divisão;
- utilizar exponenciação;
- comparar valores;
- trabalhar com resultados booleanos;
- combinar condições;
- criar e chamar funções;
- utilizar parâmetros e argumentos;
- retornar valores;
- armazenar e manipular textos;
- utilizar métodos de strings;
- formatar mensagens com f-strings;
- importar módulos;
- utilizar constantes e funções matemáticas;
- interpretar mensagens de erro;
- realizar testes com valores diferentes;
- documentar códigos;
- versionar arquivos separadamente;
- publicar a evolução dos estudos no GitHub.

---

## 📈 Progresso

| Indicador | Resultado |
|---|---:|
| Práticas planejadas | 10 |
| Práticas concluídas | 10 |
| Total de arquivos Python | 10 |
| Percentual de conclusão | 100% |

```text
████████████████████ 100%
```

---

## ✅ Status da etapa

> **Etapa concluída:** todas as práticas planejadas para a Semana 01 foram desenvolvidas, testadas, documentadas, versionadas e publicadas no GitHub.

---

## 🔗 Navegação

- [⬅️ Voltar para a Semana 01](../README.md)
- [🧩 Acessar os exercícios oficiais](../02-exercicios/README.md)
- [🚀 Acessar os desafios extras](../03-desafios-extras/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.