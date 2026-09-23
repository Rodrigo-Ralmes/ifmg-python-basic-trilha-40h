# 🧩 Semana 03 — Modularização e Tratamento de Exceções

Esta pasta reúne todo o conteúdo prático desenvolvido durante a **Semana 03 do curso Python Básico — +IFMG**, integrante da trilha de formação **Python e Big Data — 160 horas**.

A etapa é dedicada ao estudo de **tratamento de exceções, funções, parâmetros, retorno de valores, recursão, módulos, bibliotecas, modularização e decomposição de problemas**.

O conteúdo corresponde às **páginas 47 a 59** do e-book oficial do curso.

---

## 🎯 Objetivo da semana

O objetivo da Semana 03 é compreender como construir programas mais organizados, reutilizáveis e resistentes a erros por meio da modularização e do tratamento de exceções.

Durante esta etapa, foram trabalhados conhecimentos fundamentais como:

- tratamento de exceções;
- estrutura `try`;
- estrutura `except`;
- exceções genéricas;
- exceções específicas;
- `Exception`;
- `ValueError`;
- `ZeroDivisionError`;
- identificação de exceções;
- criação de funções;
- parâmetros;
- argumentos;
- retorno de valores;
- parâmetros opcionais;
- argumentos nomeados;
- recursão;
- condição de parada;
- módulos;
- bibliotecas;
- importação de funções;
- reutilização de código;
- decomposição de problemas;
- funções auxiliares;
- função principal;
- variável global;
- organização de programas;
- execução por `__name__ == "__main__"`;
- testes;
- correção de erros;
- documentação;
- versionamento com Git;
- publicação no GitHub.

---

## 📚 Conteúdo oficial

A Semana 03 corresponde ao conteúdo **Modularização e Tratamento de Exceções** do material didático do curso Python Básico do +IFMG.

### 3.1 Introdução

Apresentação dos conceitos relacionados à organização de programas e tratamento de erros.

### 3.2 Tratamento de exceções

Conteúdos estudados:

- erros durante a execução;
- `try`;
- `except`;
- tratamento genérico de erros;
- identificação do tipo de exceção;
- `Exception`;
- `ValueError`;
- `ZeroDivisionError`;
- repetição de entrada após erro.

### 3.3 Modularização

Conteúdos estudados:

- divisão do programa em partes menores;
- reutilização de código;
- organização lógica das funcionalidades.

### 3.3.1 Funções

Conteúdos estudados:

- declaração com `def`;
- chamada de funções;
- código reutilizável;
- variáveis locais.

### 3.3.2 Passagem de parâmetros e retorno de resultado

Conteúdos estudados:

- parâmetros;
- argumentos;
- passagem de valores;
- comando `return`;
- composição de chamadas de funções.

### 3.3.3 Nomes de parâmetros e parâmetros opcionais

Conteúdos estudados:

- argumentos nomeados;
- parâmetros com valor padrão;
- parâmetros opcionais.

### 3.3.4 Recursão

Conteúdos estudados:

- função chamando a si mesma;
- condição de parada;
- cálculo recursivo;
- fatorial.

### 3.3.5 Módulos e bibliotecas

Conteúdos estudados:

- criação de módulos próprios;
- importação de módulos;
- importação de funções;
- reutilização de código entre arquivos.

### 3.4 Decomposição de problemas

Conteúdos estudados:

- divisão de problemas maiores;
- criação de funções específicas;
- separação de responsabilidades;
- função principal;
- integração de diferentes partes do programa.

### 3.7 Revisão

Ao final da semana, o conteúdo é retomado por meio da revisão da terceira semana, consolidando os conceitos estudados antes do avanço para a Semana 04.

---

## 🧠 Metodologia de aprendizagem

A Semana 03 foi organizada em três níveis progressivos:

```text
Práticas fundamentais
        ↓
Exercícios oficiais
        ↓
Desafios extras
```

### 1. Práticas fundamentais

As práticas foram utilizadas para experimentar isoladamente os conceitos apresentados no material, começando pelo tratamento de exceções e avançando até a construção de uma calculadora modular completa.

### 2. Exercícios oficiais

Os exercícios oficiais permitiram aplicar os conteúdos do e-book em problemas envolvendo entrada segura de números inteiros, funções para datas e funções para cálculo de MDC e MMC.

### 3. Desafios extras

Os desafios extras foram desenvolvidos como **atividades autorais de consolidação**, sem serem confundidos com os exercícios oficiais do IFMG.

Eles ampliaram a aplicação dos conteúdos da semana em situações envolvendo validação, exceções, funções, recursão, decomposição e modularização.

O processo completo utilizado foi:

```text
Estudo do conteúdo
        ↓
Compreensão do conceito
        ↓
Criação da prática
        ↓
Execução no Spyder
        ↓
Resolução do exercício oficial
        ↓
Desenvolvimento do desafio extra
        ↓
Teste com diferentes entradas
        ↓
Identificação e correção de erros
        ↓
Documentação
        ↓
Versionamento individual com Git
        ↓
Publicação no GitHub
```

---

## 📊 Resumo geral

| Categoria | Planejado | Concluído | Percentual | Status |
|---|---:|---:|---:|:---:|
| Práticas fundamentais | 16 | 16 | 100% | ✅ |
| Exercícios oficiais | 3 | 3 | 100% | ✅ |
| Desafios extras | 10 | 10 | 100% | ✅ |
| **Total de códigos** | **29** | **29** | **100%** | **✅** |

```text
████████████████████ 100%
```

---

# 🧪 01 — Práticas fundamentais

As práticas foram desenvolvidas para experimentar progressivamente os conteúdos da Semana 03, seguindo a sequência apresentada no material didático.

Pasta: [`01-praticas`](01-praticas/README.md)

## Práticas concluídas

| Nº | Prática | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Tratamento simples de exceção | [`pratica01_excecao_simples.py`](01-praticas/pratica01_excecao_simples.py) | ✅ |
| 02 | Tratamento de exceção com repetição | [`pratica02_excecao_com_repeticao.py`](01-praticas/pratica02_excecao_com_repeticao.py) | ✅ |
| 03 | Identificando o tipo da exceção | [`pratica03_identificar_tipo_excecao.py`](01-praticas/pratica03_identificar_tipo_excecao.py) | ✅ |
| 04 | Exceções específicas | [`pratica04_excecoes_especificas.py`](01-praticas/pratica04_excecoes_especificas.py) | ✅ |
| 05 | Primeira função criada pelo programador | [`pratica05_funcao_saudacao.py`](01-praticas/pratica05_funcao_saudacao.py) | ✅ |
| 06 | Função cubo sem retorno | [`pratica06_funcao_cubo_sem_retorno.py`](01-praticas/pratica06_funcao_cubo_sem_retorno.py) | ✅ |
| 07 | Função cubo com retorno | [`pratica07_funcao_cubo_com_retorno.py`](01-praticas/pratica07_funcao_cubo_com_retorno.py) | ✅ |
| 08 | Parâmetros nomeados e opcionais | [`pratica08_parametros_opcionais.py`](01-praticas/pratica08_parametros_opcionais.py) | ✅ |
| 09 | Recursão e cálculo do fatorial | [`pratica09_recursao_fatorial.py`](01-praticas/pratica09_recursao_fatorial.py) | ✅ |
| 10 | Criação de módulo matemático | [`pratica10_modulo_mat.py`](01-praticas/pratica10_modulo_mat.py) | ✅ |
| 11 | Utilização de módulo próprio | [`pratica11_principal_modulos.py`](01-praticas/pratica11_principal_modulos.py) | ✅ |
| 12 | Script executável | [`pratica12_script_executavel.py`](01-praticas/pratica12_script_executavel.py) | ✅ |
| 13 | Função `calcula()` | [`pratica13_funcao_calcula.py`](01-praticas/pratica13_funcao_calcula.py) | ✅ |
| 14 | Função de histórico | [`pratica14_funcao_historico.py`](01-praticas/pratica14_funcao_historico.py) | ✅ |
| 15 | Função principal da calculadora | [`pratica15_funcao_principal_calculadora.py`](01-praticas/pratica15_funcao_principal_calculadora.py) | ✅ |
| 16 | Calculadora modular completa | [`pratica16_calculadora_completa.py`](01-praticas/pratica16_calculadora_completa.py) | ✅ |

## Conteúdos consolidados nas práticas

As 16 práticas permitiram consolidar:

- captura de exceções com `try/except`;
- repetição de entrada após erro;
- identificação do tipo de exceção;
- tratamento de exceções específicas;
- `ValueError`;
- `ZeroDivisionError`;
- criação de funções com `def`;
- chamada de funções;
- parâmetros;
- argumentos;
- retorno com `return`;
- parâmetros opcionais;
- argumentos nomeados;
- recursão;
- condição de parada;
- cálculo de fatorial;
- criação de módulos;
- importação de módulos próprios;
- separação entre módulo e programa principal;
- utilização de `__name__ == "__main__"`;
- decomposição de programas;
- funções auxiliares;
- função principal;
- integração de funções em aplicações maiores.

Para consultar a documentação completa, acesse:

[📘 Documentação das práticas](01-praticas/README.md)

---

# 🧩 02 — Exercícios oficiais

Os exercícios oficiais foram desenvolvidos a partir das atividades propostas no material didático da Semana 03.

Pasta: [`02-exercicios`](02-exercicios/README.md)

## Exercícios concluídos

| Nº | Exercício | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Função `input_int()` | [`ex01_input_int.py`](02-exercicios/ex01_input_int.py) | ✅ |
| 02 | Ano bissexto e quantidade de dias do mês | [`ex02_funcoes_data.py`](02-exercicios/ex02_funcoes_data.py) | ✅ |
| 03 | MDC e MMC | [`ex03_mdc_mmc.py`](02-exercicios/ex03_mdc_mmc.py) | ✅ |

---

## Exercício 01 — Função `input_int()`

O exercício implementa uma função para solicitar um número inteiro ao usuário e repetir a entrada quando ocorrer uma conversão inválida.

O objetivo é impedir que uma entrada inadequada encerre o programa inesperadamente.

Exemplo conceitual:

```python
while True:
    try:
        valor = int(input("Digite um número inteiro: "))
        return valor
    except ValueError:
        print("Entrada inválida.")
```

Principais conceitos:

- função;
- `while`;
- `try`;
- `except`;
- `ValueError`;
- `int()`;
- repetição após erro;
- retorno de valor.

---

## Exercício 02 — Ano bissexto e quantidade de dias do mês

O exercício implementa funções para:

- verificar se um ano é bissexto;
- determinar a quantidade de dias de determinado mês;
- solicitar mês e ano;
- apresentar os resultados das funções.

Exemplo da lógica do ano bissexto:

```python
if ano % 400 == 0:
    return True
elif ano % 4 == 0 and not ano % 100 == 0:
    return True
else:
    return False
```

A função de quantidade de dias utiliza o resultado da função de ano bissexto quando o mês informado é fevereiro.

Principais conceitos:

- funções;
- parâmetros;
- retorno booleano;
- estruturas condicionais;
- composição de funções;
- reutilização de código;
- função principal;
- `__name__ == "__main__"`.

---

## Exercício 03 — MDC e MMC

O exercício implementa funções para calcular:

- Máximo Divisor Comum — MDC;
- Mínimo Múltiplo Comum — MMC.

Para o MDC, é utilizado o algoritmo de Euclides.

Para o MMC, é utilizada a relação:

```text
MMC(n1, n2) = n1 × n2 / MDC(n1, n2)
```

Na implementação em Python:

```python
def mmc(n1, n2):
    return n1 * n2 // mdc(n1, n2)
```

Principais conceitos:

- funções;
- parâmetros;
- retorno de valores;
- algoritmo de Euclides;
- operador `%`;
- divisão inteira;
- composição de funções;
- modularização;
- função principal;
- reutilização de código.

Para consultar a documentação completa, acesse:

[📘 Documentação dos exercícios oficiais](02-exercicios/README.md)

---

# 🚀 03 — Desafios extras

Os desafios extras foram desenvolvidos como **exercícios autorais de consolidação**, com o objetivo de ampliar a aplicação dos conteúdos estudados na Semana 03.

Eles não correspondem aos exercícios oficiais do material didático do +IFMG.

Pasta: [`03-desafios-extras`](03-desafios-extras/README.md)

## Desafios concluídos

| Nº | Desafio | Arquivo | Status |
|---:|---|---|:---:|
| 01 | Divisão segura | [`desafio01_divisao_segura.py`](03-desafios-extras/desafio01_divisao_segura.py) | ✅ |
| 02 | Média de notas segura | [`desafio02_media_notas_segura.py`](03-desafios-extras/desafio02_media_notas_segura.py) | ✅ |
| 03 | Conversor seguro | [`desafio03_conversor_seguro.py`](03-desafios-extras/desafio03_conversor_seguro.py) | ✅ |
| 04 | Calculadora com funções | [`desafio04_calculadora_funcoes.py`](03-desafios-extras/desafio04_calculadora_funcoes.py) | ✅ |
| 05 | Fatorial seguro | [`desafio05_fatorial_seguro.py`](03-desafios-extras/desafio05_fatorial_seguro.py) | ✅ |
| 06 | Validação de idade | [`desafio06_validacao_idade.py`](03-desafios-extras/desafio06_validacao_idade.py) | ✅ |
| 07 | Menu modular | [`desafio07_menu_modular.py`](03-desafios-extras/desafio07_menu_modular.py) | ✅ |
| 08 | Geometria modular | [`desafio08_geometria_modular.py`](03-desafios-extras/desafio08_geometria_modular.py) | ✅ |
| 09 | Estatísticas de números | [`desafio09_estatisticas_numeros.py`](03-desafios-extras/desafio09_estatisticas_numeros.py) | ✅ |
| 10 | Calculadora avançada | [`desafio10_calculadora_avancada.py`](03-desafios-extras/desafio10_calculadora_avancada.py) | ✅ |

## Conteúdos consolidados nos desafios

Os desafios permitiram ampliar a aplicação de:

- `try/except`;
- `ValueError`;
- `ZeroDivisionError`;
- validação de entradas;
- funções;
- parâmetros;
- retorno de valores;
- decomposição de problemas;
- modularização;
- recursão;
- funções reutilizáveis;
- menus;
- cálculos geométricos;
- estatísticas numéricas;
- integração entre diferentes funções.

Para consultar a documentação completa, acesse:

[📘 Documentação dos desafios extras](03-desafios-extras/README.md)

---

## 🧱 Conceitos centrais da Semana 03

### Tratamento de exceções

O bloco `try/except` permite tratar erros ocorridos durante a execução do programa.

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido.")
```

Com isso, situações previsíveis podem ser tratadas sem encerrar abruptamente o programa.

### Exceções específicas

Quando possível, foram utilizadas exceções específicas.

Exemplos:

```python
except ValueError:
```

```python
except ZeroDivisionError:
```

Isso torna o tratamento do erro mais claro e permite apresentar mensagens adequadas para cada situação.

### Funções

As funções permitem reunir instruções relacionadas em blocos reutilizáveis.

```python
def somar(a, b):
    return a + b
```

A chamada:

```python
resultado = somar(10, 5)
```

produz:

```text
15
```

### Parâmetros e argumentos

Na definição:

```python
def cubo(numero):
    return numero ** 3
```

`numero` é um parâmetro.

Na chamada:

```python
cubo(5)
```

`5` é o argumento enviado para a função.

### Retorno de valores

O comando `return` devolve um resultado para o ponto onde a função foi chamada.

```python
def dobro(numero):
    return numero * 2
```

Isso permite armazenar, reutilizar e combinar resultados de diferentes funções.

### Parâmetros opcionais

Um parâmetro pode possuir um valor padrão:

```python
def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")
```

Assim, a função pode ser utilizada com ou sem um argumento explícito.

### Recursão

Uma função recursiva chama a si própria.

Exemplo conceitual do fatorial:

```python
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)
```

A condição:

```python
if n <= 1:
```

funciona como **condição de parada** da recursão.

### Módulos

A modularização permite separar funções em arquivos diferentes.

Exemplo:

```python
from modulo_mat import somar
```

Isso favorece:

- reutilização;
- organização;
- manutenção;
- separação de responsabilidades.

### Função principal

Programas maiores podem centralizar o fluxo principal em uma função:

```python
def principal():
    pass
```

E controlar a execução direta com:

```python
if __name__ == "__main__":
    principal()
```

Essa organização permite distinguir a execução do programa da importação de suas funções por outros módulos.

### Decomposição de problemas

Um problema maior pode ser dividido em funções menores:

```text
Problema
   ↓
Função 1
   ↓
Função 2
   ↓
Função 3
   ↓
Função principal
```

Essa estratégia reduz complexidade e melhora a legibilidade do código.

---

## ⚠️ Erros, exceções e aprendizados

Durante a Semana 03, o tratamento de erros deixou de ser apenas uma etapa de depuração e passou a fazer parte da própria lógica dos programas.

### Conversão inválida

Uma entrada como:

```text
abc
```

não pode ser convertida diretamente com:

```python
int("abc")
```

Isso gera:

```text
ValueError
```

A solução foi tratar essa situação com:

```python
except ValueError:
```

---

### Divisão por zero

Uma operação como:

```python
10 / 0
```

gera:

```text
ZeroDivisionError
```

A situação pode ser tratada especificamente:

```python
except ZeroDivisionError:
```

---

### Recursão sem condição de parada

Uma função recursiva precisa obrigatoriamente possuir uma condição que encerre as chamadas.

Sem isso, as chamadas continuam até ultrapassar o limite de recursão.

Por esse motivo, o fatorial utiliza um caso-base:

```python
if n <= 1:
    return 1
```

---

### Diferença entre `print()` e `return`

`print()` apresenta uma informação no console.

```python
print(resultado)
```

`return` devolve um valor para quem chamou a função.

```python
return resultado
```

Essa diferença é fundamental para criar funções reutilizáveis.

---

### Organização entre módulo e programa principal

Funções reutilizáveis podem ser mantidas separadas do fluxo principal do programa.

Essa separação facilita:

- leitura;
- reutilização;
- testes;
- manutenção;
- expansão do programa.

---

## 🗂️ Padrão de organização dos códigos

Os códigos da Semana 03 foram organizados com cabeçalhos contendo:

- curso;
- trilha;
- semana;
- tipo da atividade;
- número e título;
- nome do arquivo;
- autoria;
- objetivo;
- conteúdos praticados;
- status.

Estrutura utilizada:

```python
# =============================================================================
# Curso: Python Básico - +IFMG
# Trilha: Python e Big Data - 160h
# Semana: 03 - Modularização e Tratamento de Exceções
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

Dependendo do objetivo do programa, os códigos também foram organizados em blocos como:

```python
# =============================================================================
# FUNÇÕES
# =============================================================================


# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================


# =============================================================================
# TRATAMENTO DE EXCEÇÕES
# =============================================================================
```

---

## 📁 Estrutura da Semana 03

```text
semana-03/
├── README.md
│
├── 01-praticas/
│   ├── README.md
│   ├── pratica01_excecao_simples.py
│   ├── pratica02_excecao_com_repeticao.py
│   ├── pratica03_identificar_tipo_excecao.py
│   ├── pratica04_excecoes_especificas.py
│   ├── pratica05_funcao_saudacao.py
│   ├── pratica06_funcao_cubo_sem_retorno.py
│   ├── pratica07_funcao_cubo_com_retorno.py
│   ├── pratica08_parametros_opcionais.py
│   ├── pratica09_recursao_fatorial.py
│   ├── pratica10_modulo_mat.py
│   ├── pratica11_principal_modulos.py
│   ├── pratica12_script_executavel.py
│   ├── pratica13_funcao_calcula.py
│   ├── pratica14_funcao_historico.py
│   ├── pratica15_funcao_principal_calculadora.py
│   └── pratica16_calculadora_completa.py
│
├── 02-exercicios/
│   ├── README.md
│   ├── ex01_input_int.py
│   ├── ex02_funcoes_data.py
│   └── ex03_mdc_mmc.py
│
└── 03-desafios-extras/
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

## ▶️ Como executar os códigos

### Execução pelo Spyder

1. Abra o Spyder.
2. Acesse a pasta do projeto.
3. Entre em `semana-03`.
4. Abra o arquivo desejado.
5. Execute o programa.
6. Informe os valores solicitados, quando necessário.
7. Observe o resultado no console.
8. Realize novos testes para validar diferentes situações.

### Execução pelo terminal

Acesse a raiz do repositório:

```bat
cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h
```

Exemplo de prática:

```bat
python semana-03\01-praticas\pratica01_excecao_simples.py
```

Exemplo de exercício oficial:

```bat
python semana-03\02-exercicios\ex01_input_int.py
```

Exemplo de desafio extra:

```bat
python semana-03\03-desafios-extras\desafio01_divisao_segura.py
```

Exemplo da última prática:

```bat
python semana-03\01-praticas\pratica16_calculadora_completa.py
```

Exemplo do último exercício oficial:

```bat
python semana-03\02-exercicios\ex03_mdc_mmc.py
```

Exemplo do último desafio:

```bat
python semana-03\03-desafios-extras\desafio10_calculadora_avancada.py
```

---

## 🔄 Fluxo de versionamento utilizado

Cada atividade foi versionada individualmente.

Fluxo utilizado:

```text
Alteração
   ↓
git status
   ↓
git add
   ↓
git status
   ↓
git commit
   ↓
git push
   ↓
git status
```

Exemplo:

```bat
git status
git add semana-03/01-praticas/nome_do_arquivo.py
git status
git commit -m "feat: adiciona atividade da semana 03"
git push origin main
git status
```

Para documentação:

```bat
git status
git add semana-03/README.md
git status
git commit -m "docs: adiciona README principal da semana 03"
git push origin main
git status
```

### Convenção utilizada nos commits

| Prefixo | Utilização |
|---|---|
| `feat` | Inclusão de prática, exercício ou desafio |
| `docs` | Criação ou atualização de documentação |
| `fix` | Correção de erro |
| `refactor` | Reorganização do código sem alterar o resultado |

---

## 💡 Aprendizados consolidados

Ao concluir a Semana 03, foram consolidados os seguintes aprendizados:

### Tratamento de exceções

- compreender o conceito de exceção;
- identificar erros ocorridos em tempo de execução;
- utilizar `try`;
- utilizar `except`;
- tratar exceções genéricas;
- tratar exceções específicas;
- utilizar `ValueError`;
- utilizar `ZeroDivisionError`;
- impedir encerramentos inesperados;
- repetir entradas após erros;
- criar mensagens adequadas para cada situação.

### Funções

- criar funções com `def`;
- chamar funções;
- utilizar parâmetros;
- fornecer argumentos;
- utilizar argumentos nomeados;
- definir parâmetros opcionais;
- retornar valores;
- diferenciar `print()` de `return`;
- combinar chamadas de funções;
- reutilizar código.

### Recursão

- compreender chamadas recursivas;
- estabelecer uma condição de parada;
- construir um caso-base;
- calcular fatorial recursivamente;
- compreender o fluxo de retorno das chamadas.

### Modularização

- dividir programas em partes menores;
- criar módulos próprios;
- importar módulos;
- importar funções;
- separar funcionalidades;
- reutilizar funções entre arquivos;
- estruturar uma função principal;
- utilizar `__name__ == "__main__"`;
- integrar módulos em programas maiores.

### Decomposição de problemas

- analisar um problema maior;
- separar responsabilidades;
- criar funções específicas;
- integrar resultados;
- organizar o fluxo do programa;
- reduzir repetição;
- melhorar legibilidade e manutenção.

### Organização

- manter padrão de cabeçalhos;
- documentar objetivos;
- identificar conteúdos praticados;
- organizar práticas, exercícios e desafios;
- manter READMEs independentes;
- criar links de navegação;
- documentar a evolução da semana.

### Git e GitHub

- utilizar `git status`;
- selecionar arquivos individualmente com `git add`;
- criar commits específicos;
- utilizar mensagens descritivas;
- publicar com `git push`;
- verificar sincronização com `origin/main`;
- diferenciar arquivos rastreados e não rastreados;
- manter histórico granular da aprendizagem;
- versionar documentação com prefixo `docs`.

---

## 🏆 Resultados da Semana 03

A Semana 03 foi concluída com:

- **16 práticas fundamentais**;
- **3 exercícios oficiais**;
- **10 desafios extras autorais de consolidação**;
- **29 arquivos Python**;
- **3 READMEs específicos das categorias**;
- **1 README principal da Semana 03**;
- conteúdos das páginas **47 a 59** estudados;
- códigos executados e testados no Spyder;
- atividades documentadas;
- versionamento individual;
- publicação no GitHub;
- consolidação de tratamento de exceções;
- consolidação de funções e parâmetros;
- consolidação de recursão;
- consolidação de módulos;
- consolidação de decomposição de problemas.

---

## 📈 Progresso final

| Indicador | Resultado |
|---|---:|
| Práticas fundamentais | 16/16 |
| Exercícios oficiais | 3/3 |
| Desafios extras | 10/10 |
| Arquivos Python | 29 |
| READMEs da Semana 03 | 4 |
| Percentual da semana | **100%** |

```text
Práticas             ████████████████████ 100%
Exercícios oficiais  ████████████████████ 100%
Desafios extras      ████████████████████ 100%
Semana 03            ████████████████████ 100%
```

---

## ✅ Status da semana

> **Semana 03 concluída com sucesso:** todas as práticas planejadas, os exercícios oficiais e os desafios extras foram desenvolvidos, testados, documentados, versionados e publicados no GitHub.

A Semana 03 consolida a transição de programas mais lineares para códigos estruturados em funções, módulos e componentes reutilizáveis, com tratamento explícito de situações de erro.

---

## 🔗 Navegação

- [🧪 Práticas fundamentais](01-praticas/README.md)
- [🧩 Exercícios oficiais](02-exercicios/README.md)
- [🚀 Desafios extras](03-desafios-extras/README.md)
- [⬅️ Semana 02](../semana-02/README.md)
- [➡️ Semana 04](../semana-04/README.md)
- [🏠 Voltar ao início do repositório](../README.md)

---

## 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.
