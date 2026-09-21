# 🧩 Exercícios Oficiais — Semana 03

Esta pasta reúne os exercícios oficiais desenvolvidos durante a **Semana 03** do curso **Python Básico — +IFMG**.

Os exercícios foram utilizados para consolidar os conteúdos relacionados a **tratamento de exceções, funções, modularização, retorno de valores, decomposição de problemas e construção de algoritmos reutilizáveis**, mantendo o mesmo padrão de organização e documentação adotado nas Semanas 01 e 02.

---

## 🎯 Objetivo

O objetivo desta etapa é consolidar os conhecimentos da Semana 03 por meio da resolução de exercícios envolvendo:

- definição e chamada de funções;
- parâmetros;
- retorno de valores com `return`;
- tratamento de exceções;
- `try`;
- `except`;
- `ValueError`;
- repetição controlada com `while True`;
- validação de entrada;
- decomposição de problemas em funções menores;
- reutilização de código;
- funções auxiliares;
- regras de calendário;
- identificação de ano bissexto;
- quantidade de dias de um mês;
- cálculo do máximo divisor comum — MDC;
- algoritmo de Euclides;
- cálculo do mínimo múltiplo comum — MMC;
- função principal;
- organização do fluxo de execução.

---

## 🧠 Metodologia

Cada exercício foi desenvolvido seguindo um processo sequencial e lógico:

```text
Leitura do problema
        ↓
Identificação das entradas
        ↓
Decomposição do problema
        ↓
Definição das funções necessárias
        ↓
Definição dos parâmetros
        ↓
Implementação do processamento
        ↓
Tratamento de possíveis erros
        ↓
Definição dos valores de retorno
        ↓
Construção da função principal
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
Versionamento individual com Git
        ↓
Publicação no GitHub
```

A organização dos exercícios desta semana passa a enfatizar a separação de responsabilidades.

Exemplo conceitual:

```python
def funcao_auxiliar(...):
    # processamento específico
    return resultado


def principal():
    # entrada de dados
    # chamada das funções
    # apresentação dos resultados


principal()
```

Essa organização permite compreender com clareza:

- qual função recebe determinada responsabilidade;
- quais dados entram em cada função;
- como os parâmetros são utilizados;
- como os resultados são devolvidos;
- como uma função pode utilizar outra função;
- como o programa principal coordena a execução.

---

## 📚 Conteúdos praticados

Durante o desenvolvimento dos exercícios, foram utilizados os seguintes conteúdos:

- `def`;
- funções;
- parâmetros;
- argumentos;
- `return`;
- `input()`;
- `int()`;
- `print()`;
- variáveis;
- variáveis locais;
- funções auxiliares;
- função principal;
- `while True`;
- `try`;
- `except`;
- `ValueError`;
- validação de entrada;
- operadores relacionais;
- operadores lógicos;
- operador `%`;
- divisão inteira `//`;
- estruturas condicionais;
- `if`;
- `elif`;
- `else`;
- retorno antecipado;
- decomposição de problemas;
- reutilização de código;
- algoritmo de Euclides;
- cálculo de MDC;
- cálculo de MMC;
- regras de ano bissexto;
- validação de mês;
- modularização lógica do programa.

---

# 📊 Exercícios concluídos

| Nº | Exercício | Arquivo | Conteúdo principal | Status |
|---:|---|---|---|:---:|
| 01 | Entrada de número inteiro com validação | [`ex01_input_int.py`](ex01_input_int.py) | Função, `while True`, `try/except`, `ValueError` e `return` | ✅ |
| 02 | Funções para data | [`ex02_funcoes_data.py`](ex02_funcoes_data.py) | Ano bissexto, dias do mês, funções e decomposição | ✅ |
| 03 | MDC e MMC | [`ex03_mdc_mmc.py`](ex03_mdc_mmc.py) | Algoritmo de Euclides, funções, `%`, `//` e `return` | ✅ |

---

# 🔎 Descrição dos exercícios

## 01 — Entrada de número inteiro com validação

O primeiro exercício implementa uma função responsável por solicitar um número inteiro ao usuário e garantir que a entrada seja válida.

A função utilizada é:

```python
input_int(mensagem)
```

Ela recebe uma mensagem como parâmetro, solicita a entrada com `input()`, tenta converter o valor para `int` e retorna o número quando a conversão é realizada com sucesso.

### Estrutura conceitual

```python
def input_int(mensagem):

    while True:

        try:
            return int(input(mensagem))

        except ValueError:
            print("Número inválido! Tente novamente.")
```

### Funcionamento

O fluxo pode ser representado por:

```text
Chamada da função
        ↓
Exibição da mensagem
        ↓
Usuário digita um valor
        ↓
int(...)
        ↓
Conversão válida?
   ┌────┴────┐
  Sim       Não
   ↓         ↓
return    ValueError
   ↓         ↓
 número   mensagem de erro
             ↓
        nova tentativa
```

### Papel do `while True`

O laço:

```python
while True:
```

mantém a função em execução enquanto o usuário não informar um valor que possa ser convertido para inteiro.

### Papel do `try`

O bloco:

```python
try:
```

contém a operação que pode gerar erro:

```python
int(input(mensagem))
```

### Papel do `except ValueError`

Se o usuário informar um texto que não possa ser convertido para inteiro, ocorre um `ValueError`.

Exemplo:

```text
abc
```

Nesse caso, a exceção é tratada e o programa apresenta:

```text
Número inválido! Tente novamente.
```

Depois disso, o laço solicita uma nova entrada.

### Papel do `return`

Quando a entrada é válida:

```python
return int(input(mensagem))
```

o valor inteiro é devolvido para o ponto do programa que chamou a função.

### Exemplo conceitual de execução

```text
Informe um número inteiro: abc
Número inválido! Tente novamente.

Informe um número inteiro: 25

Número informado: 25
```

### Principais conceitos

- criação de funções;
- parâmetro;
- chamada de função;
- `while True`;
- `try`;
- `except`;
- `ValueError`;
- validação;
- conversão com `int()`;
- repetição até entrada válida;
- `return`.

Arquivo: [`ex01_input_int.py`](ex01_input_int.py)

---

## 02 — Funções para data

O segundo exercício organiza o tratamento de informações de data em funções independentes.

A solução utiliza funções para:

- verificar se um ano é bissexto;
- determinar a quantidade de dias de determinado mês;
- coordenar a entrada e a saída por meio de uma função principal.

As funções centrais são:

```python
ano_bissexto(ano)
dias_mes(ano, mes)
principal()
```

---

### Função `ano_bissexto(ano)`

A função recebe um ano e verifica as regras utilizadas para determinar se ele é bissexto.

As regras são baseadas em divisibilidade por:

- `400`;
- `4`;
- `100`.

A lógica é:

```text
Divisível por 400
        ↓
      bissexto

ou

Divisível por 4
e não divisível por 100
        ↓
      bissexto
```

Uma representação possível da regra é:

```python
if ano % 400 == 0:
    return True

if ano % 4 == 0 and ano % 100 != 0:
    return True

return False
```

### Exemplos conceituais

```text
2000 → bissexto
2024 → bissexto
1900 → não bissexto
2025 → não bissexto
```

---

### Função `dias_mes(ano, mes)`

A função recebe:

```text
ano
mês
```

e retorna a quantidade correspondente de dias.

Os meses são tratados conforme três grupos principais.

### Meses com 31 dias

```text
1, 3, 5, 7, 8, 10, 12
```

Resultado:

```text
31
```

### Meses com 30 dias

```text
4, 6, 9, 11
```

Resultado:

```text
30
```

### Fevereiro

Para o mês:

```text
2
```

a quantidade de dias depende do resultado da função:

```python
ano_bissexto(ano)
```

Assim:

```text
ano bissexto     → 29 dias
ano não bissexto → 28 dias
```

### Mês inválido

Quando o número informado não representa um mês válido, a função retorna:

```python
-1
```

Esse valor permite que a função principal identifique a situação e apresente:

```text
Mês inválido.
```

---

### Função `principal()`

A função principal coordena o exercício.

Ela é responsável por:

```text
solicitar o ano
        ↓
solicitar o mês
        ↓
verificar o ano
        ↓
calcular os dias do mês
        ↓
validar o mês
        ↓
apresentar o resultado
```

### Decomposição do problema

Em vez de colocar toda a lógica em um único bloco, o exercício separa responsabilidades:

```text
ano_bissexto()
      ↓
responsável pela regra do ano

dias_mes()
      ↓
responsável pela quantidade de dias

principal()
      ↓
responsável pela interação e coordenação
```

Esse modelo torna o código:

- mais organizado;
- mais legível;
- mais reutilizável;
- mais fácil de testar;
- mais simples de manter.

### Principais conceitos

- funções;
- parâmetros;
- `return`;
- decomposição;
- operadores relacionais;
- operadores lógicos;
- operador `%`;
- `if`;
- regras de negócio;
- reutilização de uma função dentro de outra;
- validação;
- função principal.

Arquivo: [`ex02_funcoes_data.py`](ex02_funcoes_data.py)

---

## 03 — MDC e MMC

O terceiro exercício implementa funções independentes para calcular:

- **MDC — Máximo Divisor Comum**;
- **MMC — Mínimo Múltiplo Comum**.

A solução utiliza:

```python
mdc(n1, n2)
mmc(n1, n2)
principal()
```

---

### Função `mdc(n1, n2)`

A função calcula o máximo divisor comum utilizando o **algoritmo de Euclides**.

A estrutura utilizada é:

```python
def mdc(n1, n2):

    while True:

        resto = n1 % n2

        if resto == 0:
            return n2

        n1 = n2
        n2 = resto
```

### Ideia do algoritmo de Euclides

O algoritmo realiza divisões sucessivas utilizando o resto.

Exemplo conceitual para:

```text
n1 = 48
n2 = 18
```

Primeira etapa:

```text
48 % 18 = 12
```

Então:

```text
n1 = 18
n2 = 12
```

Segunda etapa:

```text
18 % 12 = 6
```

Então:

```text
n1 = 12
n2 = 6
```

Terceira etapa:

```text
12 % 6 = 0
```

Como o resto chegou a zero:

```text
MDC = 6
```

### Fluxo do algoritmo

```text
n1, n2
   ↓
n1 % n2
   ↓
resto = 0?
 ┌────┴────┐
Sim       Não
 ↓         ↓
return n2  n1 = n2
           n2 = resto
              ↓
          repete cálculo
```

---

### Função `mmc(n1, n2)`

O MMC é calculado utilizando o MDC.

A expressão utilizada é:

```python
return n1 * n2 // mdc(n1, n2)
```

Isso corresponde à relação:

```text
MMC(a, b) = (a × b) / MDC(a, b)
```

No programa é utilizada divisão inteira:

```python
//
```

### Exemplo conceitual

Para:

```text
n1 = 12
n2 = 18
```

temos:

```text
MDC = 6
```

Então:

```text
MMC = (12 × 18) // 6
MMC = 216 // 6
MMC = 36
```

---

### Função `principal()`

A função `principal()` coordena a execução do programa.

Ela solicita dois números inteiros:

```python
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
```

Depois chama:

```python
mdc(n1, n2)
mmc(n1, n2)
```

e apresenta os resultados.

A estrutura observada é:

```python
def principal():

    print("Informe dois números inteiros:")

    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))

    print(f"MDC: {mdc(n1, n2)}")
    print(f"MMC: {mmc(n1, n2)}")
```

---

### Relação entre as funções

Este exercício demonstra claramente reutilização de código:

```text
principal()
   │
   ├── mdc(n1, n2)
   │
   └── mmc(n1, n2)
          │
          └── mdc(n1, n2)
```

Ou seja, a função:

```python
mmc()
```

reutiliza a função:

```python
mdc()
```

Essa é uma aplicação direta de modularização e decomposição de problemas.

### Principais conceitos

- funções;
- parâmetros;
- retorno;
- `while True`;
- operador `%`;
- divisão inteira `//`;
- algoritmo de Euclides;
- MDC;
- MMC;
- reutilização de função;
- decomposição;
- função principal;
- entrada e saída de dados.

Arquivo: [`ex03_mdc_mmc.py`](ex03_mdc_mmc.py)

---

# 🧩 Decomposição de problemas

Um dos conceitos mais importantes consolidado nesta etapa é a decomposição.

Em vez de desenvolver um programa como um único bloco extenso, um problema pode ser dividido em funções menores.

Exemplo:

```text
Problema principal
        ↓
divisão em responsabilidades
        ↓
função A
função B
função C
        ↓
integração pela função principal
```

Nos exercícios desta semana:

```text
Exercício 01
input_int()
    ↓
entrada + validação

Exercício 02
ano_bissexto()
dias_mes()
principal()
    ↓
regras de data + coordenação

Exercício 03
mdc()
mmc()
principal()
    ↓
algoritmos matemáticos + coordenação
```

---

# 🔁 Funções e reutilização

Uma função permite definir uma lógica uma vez e utilizá-la sempre que necessário.

Exemplo:

```python
def dobro(numero):
    return numero * 2
```

Depois:

```python
resultado = dobro(10)
```

A função recebe:

```text
10
```

processa:

```text
10 × 2
```

e devolve:

```text
20
```

Nos exercícios da Semana 03, esse princípio é utilizado para separar tarefas específicas e evitar duplicação de código.

---

# ↩️ Retorno de valores

O comando:

```python
return
```

devolve um resultado produzido pela função.

Exemplo:

```python
def soma(a, b):
    return a + b
```

Chamada:

```python
resultado = soma(10, 5)
```

Resultado:

```text
15
```

Além de devolver valores, `return` também encerra a execução da função naquele ponto.

Esse comportamento é utilizado nos exercícios para:

- devolver números válidos;
- retornar resultados lógicos;
- retornar quantidade de dias;
- retornar o MDC;
- retornar o MMC;
- indicar situações inválidas.

---

# 🛡️ Tratamento de exceções

O Exercício 01 aplica diretamente o tratamento de exceções.

Estrutura básica:

```python
try:
    # operação que pode gerar erro

except ValueError:
    # tratamento do erro
```

Isso permite evitar que uma entrada inválida interrompa a execução do programa.

Exemplo:

```text
Entrada: abc
        ↓
int("abc")
        ↓
ValueError
        ↓
except ValueError
        ↓
mensagem amigável
        ↓
nova tentativa
```

---

# 🧮 Operadores utilizados

## Operador de resto `%`

O operador:

```python
%
```

retorna o resto da divisão.

Exemplo:

```python
10 % 3
```

Resultado:

```text
1
```

Foi utilizado em:

- verificação de divisibilidade;
- regras de ano bissexto;
- algoritmo de Euclides.

---

## Divisão inteira `//`

O operador:

```python
//
```

retorna o quociente inteiro da divisão.

Exemplo:

```python
20 // 6
```

Resultado:

```text
3
```

No exercício de MMC, é utilizado em:

```python
n1 * n2 // mdc(n1, n2)
```

---

# 🗂️ Organização dos códigos

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
- funções utilizadas;
- processamento;
- saída.

Exemplo:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python & Big Data - 160 horas
# Semana: 03
# Tipo: Exercício
# Atividade: 01 - Nome do exercício
# Arquivo: nome_do_arquivo.py
# Autor: Rodrigo de Almeida Silveira
#
# Objetivo:
# Descrição do objetivo do programa.
#
# Conteúdos:
# - funções
# - parâmetros
# - return
#
# Status: Concluído
# =============================================================================
```

---

# 📁 Estrutura da pasta

```text
02-exercicios/
├── README.md
├── ex01_input_int.py
├── ex02_funcoes_data.py
└── ex03_mdc_mmc.py
```

---

# ▶️ Como executar

## Execução pelo Spyder

1. Abra o Spyder.
2. Acesse a pasta:

```text
semana-03/02-exercicios
```

3. Abra o exercício desejado.
4. Execute o arquivo.
5. Informe os valores solicitados no console.
6. Analise o resultado.
7. Repita os testes utilizando valores diferentes.

---

## Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd /d E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

### Exercício 01

```bat
python semana-03\02-exercicios\ex01_input_int.py
```

### Exercício 02

```bat
python semana-03\02-exercicios\ex02_funcoes_data.py
```

### Exercício 03

```bat
python semana-03\02-exercicios\ex03_mdc_mmc.py
```

---

# 🌳 Versionamento individual

Cada exercício foi versionado separadamente.

Fluxo utilizado:

```text
Exercício concluído
        ↓
git status
        ↓
git add arquivo.py
        ↓
git status
        ↓
git commit
        ↓
git push origin main
        ↓
git status
        ↓
GitHub atualizado
```

Commits organizados por exercício:

```text
feat: adiciona exercicio 01 de entrada inteira
feat: adiciona exercicio 02 de funcoes de data
feat: adiciona exercicio 03 de mdc e mmc
```

Essa estratégia mantém o histórico do repositório:

- organizado;
- rastreável;
- incremental;
- fácil de revisar;
- coerente com o processo de aprendizagem.

---

# 💡 Aprendizados consolidados

A conclusão dos exercícios permitiu consolidar:

- interpretar problemas;
- decompor problemas maiores;
- identificar responsabilidades distintas;
- criar funções;
- definir parâmetros;
- enviar argumentos;
- devolver resultados com `return`;
- compreender o encerramento de uma função pelo `return`;
- validar entradas;
- tratar `ValueError`;
- utilizar `try`;
- utilizar `except`;
- criar laços de repetição para novas tentativas;
- utilizar `while True`;
- reutilizar funções;
- chamar uma função dentro de outra;
- separar entrada, processamento e saída;
- implementar regras de calendário;
- verificar anos bissextos;
- determinar a quantidade de dias de um mês;
- validar números de mês;
- utilizar o operador `%`;
- aplicar testes de divisibilidade;
- implementar o algoritmo de Euclides;
- calcular MDC;
- calcular MMC;
- utilizar divisão inteira;
- construir uma função principal;
- estruturar programas de forma mais modular;
- testar diferentes cenários;
- identificar e corrigir erros;
- documentar os programas;
- versionar cada exercício separadamente;
- publicar o desenvolvimento no GitHub.

---

# 📈 Progresso

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

# ✅ Status da etapa

> **Etapa concluída:** todos os exercícios oficiais planejados para a Semana 03 foram desenvolvidos, testados, documentados, versionados individualmente e publicados no GitHub.

---

# 🔗 Navegação

- [⬅️ Voltar para a Semana 03](../README.md)
- [🧪 Acessar as práticas](../01-praticas/README.md)
- [🏠 Voltar ao início do repositório](../../README.md)

---

# 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.
