**# 🚀 Desafios Extras — Semana 02**

Esta pasta reúne os desafios extras desenvolvidos durante a **\*\*Semana 02\*\*** do curso **\*\*Python Básico — +IFMG\*\***.

Os desafios complementam as práticas e os exercícios oficiais da semana, permitindo aplicar e ampliar os conhecimentos adquiridos sobre **\*\*estruturas de decisão e estruturas de repetição\*\***.

Nesta etapa, os programas passam a possuir um fluxo de execução mais elaborado, permitindo tomar decisões, repetir instruções, controlar critérios de parada, utilizar contadores e acumuladores e resolver problemas progressivamente mais complexos.

**---**

**## 🎯 Objetivo**

Consolidar os conteúdos estudados durante a Semana 02 por meio do desenvolvimento de programas completos utilizando estruturas de controle de fluxo.

Os desafios foram elaborados para exercitar:

\- interpretação de problemas;

\- identificação das entradas;

\- definição das variáveis;

\- construção de condições;

\- utilização de estruturas condicionais;

\- utilização de estruturas de repetição;

\- comparação de valores;

\- utilização de contadores;

\- utilização de acumuladores;

\- definição de condições de parada;

\- controle de iterações;

\- tratamento de diferentes possibilidades;

\- execução e teste dos programas;

\- identificação e correção de erros;

\- documentação dos códigos;

\- versionamento individual com Git;

\- publicação dos códigos no GitHub.

**---**

**## 🧠 Metodologia**

Cada desafio foi desenvolvido seguindo um fluxo sequencial e lógico:

\`\`\`text

Problema

    ↓

Análise

    ↓

Definição das entradas

    ↓

Identificação das condições

    ↓

Identificação das repetições

    ↓

Definição das variáveis

    ↓

Implementação em Python

    ↓

Teste no Spyder

    ↓

Análise dos resultados

    ↓

Correção

    ↓

Documentação

    ↓

Versionamento com Git

    ↓

Publicação no GitHub

\`\`\`

Internamente, os códigos seguem o mesmo padrão de organização utilizado durante a trilha:

\`\`\`python

\# =============================================================================

\# ENTRADA DE DADOS

\# =============================================================================



\# =============================================================================

\# PROCESSAMENTO

\# =============================================================================



\# =============================================================================

\# SAÍDA DE DADOS

\# =============================================================================

\`\`\`

Quando necessário, também podem ser utilizadas seções específicas:

\`\`\`python

\# =============================================================================

\# INICIALIZAÇÃO

\# =============================================================================

\`\`\`

\`\`\`python

\# =============================================================================

\# VALIDAÇÃO

\# =============================================================================

\`\`\`

Essa estrutura facilita a leitura, o teste, a manutenção e a compreensão dos algoritmos.

**---**

**## 📚 Conteúdos praticados**

Durante o desenvolvimento dos desafios da Semana 02, são utilizados os seguintes conceitos:

\- \`input()\`;

\- \`int()\`;

\- \`float()\`;

\- \`str\`;

\- variáveis;

\- operadores aritméticos;

\- operadores relacionais;

\- operadores lógicos;

\- operador de resto \`%\`;

\- \`if\`;

\- \`elif\`;

\- \`else\`;

\- condições simples;

\- condições compostas;

\- estruturas condicionais aninhadas;

\- \`while\`;

\- \`while True\`;

\- \`for\`;

\- \`range()\`;

\- \`break\`;

\- \`continue\`;

\- contadores;

\- acumuladores;

\- comparação de valores;

\- maior e menor valor;

\- média aritmética;

\- divisibilidade;

\- sequências numéricas;

\- f-strings;

\- formatação com \`.2f\`;

\- métodos de strings;

\- \`strip()\`;

\- \`lower()\`.

**---**

**## 📊 Desafios concluídos**

\| Nº | Desafio | Arquivo | Conteúdo principal | Status |

\|---:|---|---|---|:---:|

\| 01 | Classificador de número | [\`desafio01\_classificador\_numero.py\`]\(desafio01\_classificador\_numero.py) | \`if/elif/else\` e paridade | ⬜ |

\| 02 | Situação do aluno | [\`desafio02\_situacao\_aluno.py\`]\(desafio02\_situacao\_aluno.py) | Decisão múltipla | ⬜ |

\| 03 | Maior e menor de cinco números | [\`desafio03\_maior\_menor\_cinco\_numeros.py\`]\(desafio03\_maior\_menor\_cinco\_numeros.py) | \`for\` e comparação | ⬜ |

\| 04 | Tabuada | [\`desafio04\_tabuada.py\`]\(desafio04\_tabuada.py) | \`for\` e \`range()\` | ⬜ |

\| 05 | Soma dos pares de um intervalo | [\`desafio05\_soma\_pares\_intervalo.py\`]\(desafio05\_soma\_pares\_intervalo.py) | Acumulador e \`%\` | ⬜ |

\| 06 | Contador de sinais | [\`desafio06\_contador\_sinais.py\`]\(desafio06\_contador\_sinais.py) | Contadores | ⬜ |

\| 07 | Senha com três tentativas | [\`desafio07\_senha\_tres\_tentativas.py\`]\(desafio07\_senha\_tres\_tentativas.py) | \`while\` e \`break\` | ⬜ |

\| 08 | Calculadora com menu | [\`desafio08\_calculadora\_menu.py\`]\(desafio08\_calculadora\_menu.py) | \`while\`, \`break\`, \`continue\` | ⬜ |

\| 09 | Fibonacci | [\`desafio09\_fibonacci.py\`]\(desafio09\_fibonacci.py) | Sequências e repetição | ⬜ |

\| 10 | Número primo | [\`desafio10\_numero\_primo.py\`]\(desafio10\_numero\_primo.py) | Divisibilidade e \`break\` | ⬜ |

\| 11 | Estatísticas da turma | [\`desafio11\_estatisticas\_turma.py\`]\(desafio11\_estatisticas\_turma.py) | Contadores e acumuladores | ⬜ |

**---**

**# 🔎 Descrição dos desafios**

**## 01 — Classificador de número**

O programa solicita um número inteiro e identifica se o valor é:

\- positivo;

\- negativo;

\- zero.

Quando o valor for diferente de zero, o programa também identifica se ele é:

\- par;

\- ímpar.

A identificação de números pares utiliza:

\`\`\`python

numero % 2 == 0

\`\`\`

Principais conceitos:

\- entrada de dados;

\- conversão para \`int\`;

\- estruturas condicionais;

\- \`if\`;

\- \`elif\`;

\- \`else\`;

\- condições aninhadas;

\- operador \`%\`.

Arquivo:

[\`desafio01\_classificador\_numero.py\`]\(desafio01\_classificador\_numero.py)

**---**

**## 02 — Situação do aluno**

O programa solicita duas notas e calcula a média do aluno.

\`\`\`text

Média = (nota 1 + nota 2) / 2

\`\`\`

Depois, uma estrutura \`if/elif/else\` determina sua situação.

Exemplo de critérios:

\`\`\`text

Média >= 60 → Aprovado

Média >= 40 → Recuperação

Média < 40  → Reprovado

\`\`\`

Principais conceitos:

\- entrada de dados;

\- conversão para \`float\`;

\- média aritmética;

\- \`if\`;

\- \`elif\`;

\- \`else\`;

\- formatação decimal.

Arquivo:

[\`desafio02\_situacao\_aluno.py\`]\(desafio02\_situacao\_aluno.py)

**---**

**## 03 — Maior e menor de cinco números**

O programa solicita cinco números.

Durante a repetição, duas variáveis armazenam continuamente:

\`\`\`text

maior valor

menor valor

\`\`\`

Sempre que um novo número é informado, o programa realiza comparações e atualiza essas variáveis quando necessário.

Principais conceitos:

\- \`for\`;

\- \`range()\`;

\- comparação;

\- operadores relacionais;

\- atualização de variáveis;

\- maior valor;

\- menor valor.

Arquivo:

[\`desafio03\_maior\_menor\_cinco\_numeros.py\`]\(desafio03\_maior\_menor\_cinco\_numeros.py)

**---**

**## 04 — Tabuada**

O programa solicita um número inteiro e apresenta sua tabuada de multiplicação de 1 até 10.

Exemplo:

\`\`\`text

7 x 1 = 7

7 x 2 = 14

7 x 3 = 21

...

7 x 10 = 70

\`\`\`

A repetição utiliza:

\`\`\`python

for multiplicador in range(1, 11):

\`\`\`

Principais conceitos:

\- entrada de dados;

\- \`for\`;

\- \`range()\`;

\- multiplicação;

\- repetição definida;

\- f-string.

Arquivo:

[\`desafio04\_tabuada.py\`]\(desafio04\_tabuada.py)

**---**

**## 05 — Soma dos pares de um intervalo**

O programa solicita o início e o fim de um intervalo numérico.

Em seguida, percorre todos os valores e identifica quais números são pares:

\`\`\`python

numero % 2 == 0

\`\`\`

Os números pares são adicionados a um acumulador:

\`\`\`python

soma += numero

\`\`\`

Principais conceitos:

\- \`for\`;

\- \`range()\`;

\- estrutura condicional;

\- operador \`%\`;

\- acumulador;

\- intervalos numéricos.

Arquivo:

[\`desafio05\_soma\_pares\_intervalo.py\`]\(desafio05\_soma\_pares\_intervalo.py)

**---**

**## 06 — Contador de sinais**

O programa solicita dez valores e classifica cada um como:

\- positivo;

\- negativo;

\- zero.

Para cada categoria é utilizado um contador específico:

\`\`\`python

positivos += 1

negativos += 1

zeros += 1

\`\`\`

Principais conceitos:

\- contadores;

\- \`for\`;

\- \`range()\`;

\- \`if\`;

\- \`elif\`;

\- \`else\`;

\- classificação de dados.

Arquivo:

[\`desafio06\_contador\_sinais.py\`]\(desafio06\_contador\_sinais.py)

**---**

**## 07 — Senha com três tentativas**

O programa simula um processo simples de autenticação.

O usuário possui no máximo três tentativas para informar a senha correta.

O controle utiliza:

\`\`\`python

while tentativas < 3:

\`\`\`

Quando a senha correta é informada:

\`\`\`python

break

\`\`\`

encerra imediatamente o laço.

Principais conceitos:

\- strings;

\- \`while\`;

\- contador;

\- condição de parada;

\- \`break\`;

\- comparação de valores;

\- controle de tentativas.

Arquivo:

[\`desafio07\_senha\_tres\_tentativas.py\`]\(desafio07\_senha\_tres\_tentativas.py)

**---**

**## 08 — Calculadora com menu**

O programa apresenta continuamente um menu contendo operações matemáticas.

Exemplo:

\`\`\`text

\+ Adição

\- Subtração

\* Multiplicação

/ Divisão

S Sair

\`\`\`

O menu permanece ativo utilizando:

\`\`\`python

while True:

\`\`\`

O comando:

\`\`\`python

break

\`\`\`

encerra o programa.

Já:

\`\`\`python

continue

\`\`\`

permite ignorar a execução restante de uma iteração e retornar ao menu.

Principais conceitos:

\- menu;

\- \`while True\`;

\- \`if/elif/else\`;

\- \`break\`;

\- \`continue\`;

\- operadores aritméticos;

\- validação de operação.

Arquivo:

[\`desafio08\_calculadora\_menu.py\`]\(desafio08\_calculadora\_menu.py)

**---**

**## 09 — Sequência de Fibonacci**

O programa solicita a quantidade de termos desejada e gera a sequência de Fibonacci.

Exemplo:

\`\`\`text

0 1 1 2 3 5 8 13 21 34

\`\`\`

Cada novo termo é calculado pela soma dos dois anteriores:

\`\`\`python

proximo = primeiro + segundo

\`\`\`

Principais conceitos:

\- variáveis auxiliares;

\- repetição;

\- \`for\`;

\- \`range()\`;

\- atualização de valores;

\- sequência numérica.

Arquivo:

[\`desafio09\_fibonacci.py\`]\(desafio09\_fibonacci.py)

**---**

**## 10 — Número primo**

O programa solicita um número inteiro e verifica se ele é primo.

Um número primo possui exatamente dois divisores positivos:

\`\`\`text

1

o próprio número

\`\`\`

Durante a verificação, o operador:

\`\`\`python

%

\`\`\`

é utilizado para testar a divisibilidade.

Quando um divisor é encontrado, a busca pode ser interrompida utilizando:

\`\`\`python

break

\`\`\`

Principais conceitos:

\- divisibilidade;

\- operador \`%\`;

\- \`for\`;

\- \`range()\`;

\- \`if\`;

\- \`break\`;

\- variável booleana.

Arquivo:

[\`desafio10\_numero\_primo.py\`]\(desafio10\_numero\_primo.py)

**---**

**## 11 — Estatísticas da turma**

O programa solicita a quantidade de alunos e registra suas notas.

Durante o processamento, calcula:

\- quantidade de alunos;

\- soma das notas;

\- média geral;

\- maior nota;

\- menor nota;

\- quantidade de aprovados;

\- quantidade de reprovados.

Exemplo do acumulador:

\`\`\`python

soma\_notas += nota

\`\`\`

Exemplo de contador:

\`\`\`python

aprovados += 1

\`\`\`

Principais conceitos:

\- \`for\`;

\- \`range()\`;

\- contador;

\- acumulador;

\- média;

\- maior valor;

\- menor valor;

\- estruturas condicionais.

Arquivo:

[\`desafio11\_estatisticas\_turma.py\`]\(desafio11\_estatisticas\_turma.py)

**---**

**# 🔧 Conceitos importantes**

**## Contador**

Um contador registra quantas vezes determinado evento ocorre.

Exemplo:

\`\`\`python

contador += 1

\`\`\`

equivale a:

\`\`\`python

contador = contador + 1

\`\`\`

**---**

**## Acumulador**

Um acumulador adiciona progressivamente valores.

Exemplo:

\`\`\`python

soma += numero

\`\`\`

equivale a:

\`\`\`python

soma = soma + numero

\`\`\`

**---**

**## Operador de resto**

O operador:

\`\`\`python

%

\`\`\`

retorna o resto de uma divisão.

Exemplo:

\`\`\`python

10 % 2

\`\`\`

resultado:

\`\`\`text

0

\`\`\`

Por isso, uma condição comum para verificar se um número é par é:

\`\`\`python

numero % 2 == 0

\`\`\`

**---**

**## \`break\`**

O comando:

\`\`\`python

break

\`\`\`

encerra imediatamente o laço em execução.

**---**

**## \`continue\`**

O comando:

\`\`\`python

continue

\`\`\`

encerra somente a iteração atual e passa para a próxima repetição.

**---**

**## \`while\`**

É utilizado principalmente quando não sabemos previamente quantas repetições serão necessárias.

Exemplo:

\`\`\`python

while resposta == "s":

\`\`\`

**---**

**## \`for\`**

É utilizado principalmente quando existe uma quantidade conhecida de repetições ou uma sequência a ser percorrida.

Exemplo:

\`\`\`python

for numero in range(1, 11):

\`\`\`

**---**

**## \`range()\`**

A função \`range()\` permite gerar sequências numéricas.

Exemplo:

\`\`\`python

range(1, 6)

\`\`\`

produz:

\`\`\`text

1

2

3

4

5

\`\`\`

O limite final não faz parte da sequência.

**---**

**# 🗂️ Organização dos códigos**

Todos os desafios seguem o padrão de documentação utilizado no projeto.

Exemplo:

\`\`\`python

\# -\*- coding: utf-8 -\*-

\# =============================================================================

\# Curso: Python Básico - +IFMG

\# Trilha: Python & Big Data - 160h

\# Semana: 02 - Controle de Fluxo

\# Tipo: Desafio extra

\# Atividade: Desafio XX - Nome do desafio

\# Arquivo: nome\_do\_arquivo.py

\# Autor: Rodrigo Ralmes

\#

\# Objetivo:

\# Descrição do objetivo do programa.

\#

\# Conteúdos praticados:

\# - conteúdo

\# - conteúdo

\#

\# Status: Concluído

\# =============================================================================

\`\`\`

Os códigos também são organizados em seções:

\`\`\`python

\# =============================================================================

\# ENTRADA DE DADOS

\# =============================================================================

\`\`\`

\`\`\`python

\# =============================================================================

\# PROCESSAMENTO

\# =============================================================================

\`\`\`

\`\`\`python

\# =============================================================================

\# SAÍDA DE DADOS

\# =============================================================================

\`\`\`

**---**

**# 📁 Estrutura da pasta**

\`\`\`text

03-desafios-extras/

├── README.md

├── desafio01\_classificador\_numero.py

├── desafio02\_situacao\_aluno.py

├── desafio03\_maior\_menor\_cinco\_numeros.py

├── desafio04\_tabuada.py

├── desafio05\_soma\_pares\_intervalo.py

├── desafio06\_contador\_sinais.py

├── desafio07\_senha\_tres\_tentativas.py

├── desafio08\_calculadora\_menu.py

├── desafio09\_fibonacci.py

├── desafio10\_numero\_primo.py

└── desafio11\_estatisticas\_turma.py

\`\`\`

**---**

**# ▶️ Como executar**

**## Execução pelo Spyder**

1\. Abra o Spyder.

2\. Acesse a pasta \`03-desafios-extras\`.

3\. Abra o arquivo desejado.

4\. Execute o código.

5\. Informe os dados solicitados.

6\. Analise o resultado apresentado no console.

7\. Caso necessário, ajuste o código e execute novamente.

**---**

**## Execução pelo terminal**

Acesse a raiz do repositório:

\`\`\`bat

cd E:\Projetos\GitHub\ifmg-python-basic-trilha-40h

\`\`\`

Exemplo:

\`\`\`bat

python semana-02\03-desafios-extras\desafio01\_classificador\_numero.py

\`\`\`

Tabuada:

\`\`\`bat

python semana-02\03-desafios-extras\desafio04\_tabuada.py

\`\`\`

Calculadora:

\`\`\`bat

python semana-02\03-desafios-extras\desafio08\_calculadora\_menu.py

\`\`\`

Número primo:

\`\`\`bat

python semana-02\03-desafios-extras\desafio10\_numero\_primo.py

\`\`\`

**---**

**# 🔄 Fluxo de desenvolvimento**

Cada desafio seguiu esta sequência:

\`\`\`text

Criar o arquivo

       ↓

Implementar o algoritmo

       ↓

Executar no Spyder

       ↓

Testar diferentes entradas

       ↓

Verificar o resultado

       ↓

Corrigir eventuais erros

       ↓

Alterar Status para Concluído

       ↓

git status

       ↓

git add

       ↓

git commit

       ↓

git push

       ↓

git status

\`\`\`

**---**

**# 🔀 Fluxo de versionamento**

Cada desafio foi versionado individualmente.

Exemplo:

\`\`\`bat

git status

git add 03-desafios-extras/desafio01\_classificador\_numero.py

git status

git commit -m "feat: adiciona desafio 01 classificador numero semana 02"

git push

git status

\`\`\`

**---**

**# 🏷️ Convenção de commits**

\| Prefixo | Utilização |

\|---|---|

\| \`feat\` | Inclusão de novo desafio |

\| \`docs\` | Criação ou atualização de documentação |

\| \`fix\` | Correção de erro |

\| \`refactor\` | Reorganização do código sem alterar seu resultado |

**---**

**# 💡 Aprendizados consolidados**

Com a conclusão desta etapa, foram consolidados conhecimentos relacionados a:

\- interpretação de problemas;

\- criação de algoritmos;

\- utilização de condições;

\- utilização de estruturas condicionais;

\- construção de múltiplas alternativas;

\- estruturas aninhadas;

\- operadores relacionais;

\- operadores lógicos;

\- repetição com \`while\`;

\- repetição com \`for\`;

\- utilização de \`range()\`;

\- interrupção de laços com \`break\`;

\- controle de iterações com \`continue\`;

\- criação de contadores;

\- criação de acumuladores;

\- comparação de valores;

\- identificação de maior e menor valor;

\- cálculo de médias;

\- processamento de intervalos numéricos;

\- divisibilidade;

\- sequências numéricas;

\- criação de menus;

\- controle de tentativas;

\- organização de código;

\- documentação;

\- testes;

\- depuração;

\- versionamento com Git;

\- publicação no GitHub.

**---**

**# 📈 Progresso**

\| Indicador | Resultado |

\|---|---:|

\| Desafios planejados | 11 |

\| Desafios concluídos | 11 |

\| Arquivos Python planejados | 11 |

\| README | 1 |

\| Percentual de conclusão | 100% |

\`\`\`text

████████████████████ 100%

\`\`\`

Todos os 11 desafios foram concluídos, testados, documentados, versionados e publicados no GitHub.

**---**

**# ✅ Status da etapa**

\> **\*\*Etapa em andamento:\*\*** os desafios extras da Semana 02 estão sendo desenvolvidos progressivamente, seguindo a mesma metodologia de organização, execução, documentação e versionamento utilizada durante a Semana 01.

**---**

**# 🔗 Navegação**

\- [⬅️ Voltar para a Semana 02]\(../README.md)

\- [🧪 Acessar as práticas]\(../01-praticas/README.md)

\- [🧩 Acessar os exercícios]\(../02-exercicios/README.md)

\- [🏠 Voltar ao início do repositório]\(../../README.md)

**---**

**# 👨‍💻 Autor**

**\*\*Rodrigo de Almeida Silveira\*\***

Projeto desenvolvido como parte da trilha de estudos em **\*\*Python e Big Data — 160 horas\*\***, iniciada pelo curso de **\*\*Python Básico — +IFMG\*\***.