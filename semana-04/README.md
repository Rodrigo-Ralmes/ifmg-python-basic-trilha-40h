# 🧩 Semana 04 — Coleções de Dados

Esta pasta reúne todo o conteúdo prático desenvolvido durante a **Semana 04 do curso Python Básico — +IFMG**, integrante da trilha de formação **Python e Big Data — 160 horas**.

A etapa é dedicada ao estudo das principais **coleções de dados da linguagem Python**, incluindo **listas, matrizes, tuplas, conjuntos e dicionários**, além da integração desses recursos com estruturas condicionais, estruturas de repetição, funções e modularização.

O conteúdo corresponde às **páginas 61 a 82** do e-book oficial do curso.

---

## 🎯 Objetivo da semana

O objetivo da Semana 04 é compreender como armazenar, organizar, acessar e manipular conjuntos de informações utilizando diferentes estruturas de dados da linguagem Python.

Durante esta etapa, são trabalhados conhecimentos fundamentais como:

- coleções de dados;
- listas;
- criação de listas;
- acesso por índices;
- índices negativos;
- alteração de elementos;
- inclusão de elementos;
- `append()`;
- `insert()`;
- `pop()`;
- `clear()`;
- `len()`;
- `range()`;
- `enumerate()`;
- operador `in`;
- operador `not in`;
- fatiamento de listas;
- list comprehension;
- matrizes;
- listas de listas;
- acesso por linha e coluna;
- tuplas;
- desempacotamento de tuplas;
- imutabilidade;
- listas contendo tuplas;
- conjuntos;
- `set`;
- união;
- interseção;
- diferença;
- subconjuntos;
- superconjuntos;
- `add()`;
- `remove()`;
- dicionários;
- pares chave-valor;
- consulta por chave;
- atualização de valores;
- `items()`;
- `keys()`;
- `values()`;
- composição de diferentes coleções;
- integração entre listas, tuplas, conjuntos e dicionários.

---

## 📚 Conteúdo oficial

A Semana 04 corresponde ao conteúdo **Coleções de Dados** do material didático do curso Python Básico do +IFMG.

### 4.1 Introdução

Apresentação da necessidade de estruturas capazes de armazenar vários elementos de dados.

São introduzidos os principais tipos de coleções utilizados durante a semana:

- listas;
- tuplas;
- conjuntos;
- dicionários.

---

### 4.2 Listas

As listas são estruturas sequenciais e mutáveis utilizadas para armazenar vários valores.

Conteúdos estudados:

- criação de listas;
- listas vazias;
- índices;
- leitura de elementos;
- alteração de elementos;
- inclusão de elementos;
- remoção de elementos;
- percurso de listas;
- `append()`;
- `insert()`;
- `pop()`;
- `clear()`.

---

### 4.2.1 Resolvendo o problema dos preços acima da média com listas

Aplicação de listas para armazenar os preços de vários produtos.

O problema permite trabalhar:

- armazenamento sequencial;
- acumuladores;
- cálculo de média;
- segundo percurso da lista;
- identificação de valores acima da média;
- associação entre posição do elemento e produto;
- utilização de `range()`;
- utilização de `enumerate()`.

---

### 4.2.2 Matrizes

As matrizes são implementadas em Python utilizando **listas de listas**.

Conteúdos estudados:

- matrizes bidimensionais;
- linhas;
- colunas;
- listas aninhadas;
- laços aninhados;
- acesso com:

```python
matriz[linha][coluna]
```

A aplicação utilizada envolve:

- produtos;
- fornecedores;
- preços;
- média por produto;
- média por fornecedor.

---

### 4.2.3 Inicialização e seleção de elementos

Nesta etapa são estudadas diferentes maneiras de inicializar e selecionar dados de uma lista.

Exemplos:

```python
lista = list(range(10))
```

```python
lista = [0] * 10
```

Também são estudados:

- compreensão de listas;
- `split()`;
- `len()`;
- índices negativos;
- fatiamento;
- cópia de listas;
- operador `in`;
- operador `not in`.

Exemplos de seleção:

```python
lista[:]
lista[1:]
lista[:-1]
lista[3:7]
```

---

### 4.2.4 Implementando o jogo da forca com listas

O jogo da forca é utilizado como aplicação integradora do conteúdo sobre listas.

O programa utiliza funções como:

```python
valida_palavra()
novo_jogo()
tem_letra()
mostra_jogo()
valida_letra()
principal()
```

Também integra conteúdos já estudados anteriormente:

- funções;
- parâmetros;
- valores de retorno;
- listas;
- strings;
- `enumerate()`;
- `len()`;
- `join()`;
- `upper()`;
- `strip()`;
- `while`;
- `if`;
- `continue`;
- `break`.

---

### 4.3 Tuplas

As tuplas permitem agrupar uma quantidade fixa de elementos.

Conteúdos estudados:

- criação de tuplas;
- acesso por índices;
- imutabilidade;
- comparação de tuplas;
- desempacotamento;
- tuplas dentro de listas.

Exemplo:

```python
produto = (nome, preco)
```

Desempacotamento:

```python
nome, preco = produto
```

---

### 4.4 Conjuntos

Os conjuntos representam coleções não ordenadas que não armazenam valores repetidos.

Conteúdos estudados:

- criação com `set()`;
- pertinência;
- união;
- interseção;
- diferença;
- subconjunto;
- superconjunto;
- `add()`;
- `remove()`.

Exemplos:

```python
s1 | s2
s1 & s2
s1 - s2
s1 <= s2
s1 >= s2
```

---

### 🎲 Jogo de Bingo

O jogo de bingo integra diferentes estruturas de dados estudadas durante a semana.

São utilizados:

- listas;
- conjuntos;
- tuplas;
- funções;
- repetição;
- condicionais;
- biblioteca `random`;
- função `shuffle()`.

Principais funções:

```python
gera_numeros()
gera_cartela()
gera_jogadores()
remove_numero()
mostra_jogo()
busca_vencedores()
principal()
```

---

### 4.5 Dicionários

Os dicionários armazenam informações utilizando pares **chave-valor**.

Exemplo:

```python
produto = {
    "nome": "Teclado",
    "preco": 100.00
}
```

Conteúdos estudados:

- criação de dicionários;
- dicionários vazios;
- inclusão de valores;
- alteração de valores;
- consulta por chave;
- percurso de dicionários;
- `items()`;
- `keys()`;
- `values()`;
- `copy()`;
- `update()`;
- `popitem()`;
- dicionários contendo outros dicionários.

---

### 🛒 Caixa de supermercado

O caixa de supermercado representa uma aplicação integradora do conteúdo sobre dicionários.

O programa combina:

- dicionários;
- dicionários aninhados;
- listas;
- tuplas;
- funções;
- condicionais;
- estruturas de repetição;
- menus.

Principais funções:

```python
cad_produto()
listar_produtos()
venda()
relatorio_vendas()
menu()
principal()
```

---

### 4.6 Exercícios

A Semana 04 possui três exercícios oficiais destinados à consolidação do conteúdo.

Os exercícios abordam:

1. equação do segundo grau com retorno das raízes em uma tupla;
2. cálculo da velocidade média de uma viagem utilizando lista de trechos;
3. contagem da frequência de números utilizando dicionário.

---

### 4.7 Respostas dos exercícios

O material apresenta soluções de referência para conferência.

A metodologia utilizada neste repositório consiste em:

1. interpretar o problema;
2. desenvolver uma solução própria;
3. executar no Spyder;
4. realizar testes;
5. comparar posteriormente com a solução apresentada no material.

---

### 4.8 Revisão

A revisão encerra a Semana 04 e também o conteúdo didático do curso Python Básico.

A recomendação é revisitar os programas desenvolvidos e tentar reconstruí-los sem consultar as soluções anteriores.

---

# 🧠 Metodologia de aprendizagem

A Semana 04 mantém a mesma metodologia aplicada nas semanas anteriores:

```text
Estudo do conteúdo oficial
        ↓
Compreensão do conceito
        ↓
Implementação das práticas
        ↓
Execução no Spyder
        ↓
Testes com diferentes valores
        ↓
Correção e melhoria
        ↓
Exercícios oficiais
        ↓
Desafios extras
        ↓
Documentação
        ↓
Versionamento com Git
        ↓
Publicação no GitHub
```

As atividades são organizadas em três níveis progressivos:

```text
🧪 Práticas fundamentais
        ↓
🧩 Exercícios oficiais
        ↓
🚀 Desafios extras
```

---

# 📁 Estrutura da Semana 04

```text
semana-04/
│
├── 01-praticas/
│   ├── pratica01_media_precos_sem_lista.py
│   ├── pratica02_precos_acima_media_lista.py
│   ├── pratica03_lista_por_indices.py
│   ├── pratica04_lista_enumerate.py
│   ├── pratica05_cotacao_fornecedores.py
│   ├── pratica06_matriz_precos.py
│   ├── pratica07_inicializacao_listas.py
│   ├── pratica08_compreensao_selecao_listas.py
│   ├── pratica09_jogo_forca.py
│   ├── pratica10_tuplas_datas.py
│   ├── pratica11_tuplas_produtos.py
│   ├── pratica12_operacoes_conjuntos.py
│   ├── pratica13_jogo_bingo.py
│   ├── pratica14_dicionarios.py
│   ├── pratica15_caixa_supermercado.py
│   └── README.md
│
├── 02-exercicios-oficiais/
│   ├── ex01_equacao_segundo_grau.py
│   ├── ex02_velocidade_media_viagem.py
│   ├── ex03_frequencia_numeros.py
│   └── README.md
│
├── 03-desafios-extras/
│   ├── desafio01_maior_menor_lista.py
│   ├── desafio02_media_notas_lista.py
│   ├── desafio03_remover_duplicados.py
│   ├── desafio04_ordenar_lista.py
│   ├── desafio05_cadastro_alunos_tuplas.py
│   ├── desafio06_estatisticas_lista.py
│   ├── desafio07_intersecao_conjuntos.py
│   ├── desafio08_controle_estoque_dicionario.py
│   ├── desafio09_contador_palavras.py
│   ├── desafio10_agenda_contatos.py
│   ├── desafio11_boletim_alunos.py
│   ├── desafio12_sistema_votacao.py
│   ├── desafio13_carrinho_compras.py
│   ├── desafio14_controle_funcionarios.py
│   ├── desafio15_mini_projeto_biblioteca.py
│   └── README.md
│
└── README.md
```

---

# 🧪 Práticas fundamentais

As práticas foram organizadas seguindo progressivamente os conceitos estudados no e-book.

| Nº | Prática | Arquivo |
|---:|---|---|
| 01 | Média de preços sem lista | [`pratica01_media_precos_sem_lista.py`](01-praticas/pratica01_media_precos_sem_lista.py) |
| 02 | Preços acima da média usando lista | [`pratica02_precos_acima_media_lista.py`](01-praticas/pratica02_precos_acima_media_lista.py) |
| 03 | Percurso de lista utilizando índices | [`pratica03_lista_por_indices.py`](01-praticas/pratica03_lista_por_indices.py) |
| 04 | Percurso utilizando `enumerate()` | [`pratica04_lista_enumerate.py`](01-praticas/pratica04_lista_enumerate.py) |
| 05 | Cotação de fornecedores | [`pratica05_cotacao_fornecedores.py`](01-praticas/pratica05_cotacao_fornecedores.py) |
| 06 | Matriz de preços | [`pratica06_matriz_precos.py`](01-praticas/pratica06_matriz_precos.py) |
| 07 | Inicialização de listas | [`pratica07_inicializacao_listas.py`](01-praticas/pratica07_inicializacao_listas.py) |
| 08 | Compreensão e seleção de listas | [`pratica08_compreensao_selecao_listas.py`](01-praticas/pratica08_compreensao_selecao_listas.py) |
| 09 | Jogo da forca | [`pratica09_jogo_forca.py`](01-praticas/pratica09_jogo_forca.py) |
| 10 | Tuplas representando datas | [`pratica10_tuplas_datas.py`](01-praticas/pratica10_tuplas_datas.py) |
| 11 | Produtos utilizando tuplas | [`pratica11_tuplas_produtos.py`](01-praticas/pratica11_tuplas_produtos.py) |
| 12 | Operações com conjuntos | [`pratica12_operacoes_conjuntos.py`](01-praticas/pratica12_operacoes_conjuntos.py) |
| 13 | Jogo de bingo | [`pratica13_jogo_bingo.py`](01-praticas/pratica13_jogo_bingo.py) |
| 14 | Manipulação de dicionários | [`pratica14_dicionarios.py`](01-praticas/pratica14_dicionarios.py) |
| 15 | Caixa de supermercado | [`pratica15_caixa_supermercado.py`](01-praticas/pratica15_caixa_supermercado.py) |

[📘 Acessar documentação completa das práticas](01-praticas/README.md)

---

# 🧩 Exercícios oficiais

| Nº | Exercício | Arquivo |
|---:|---|---|
| 01 | Equação do segundo grau com tuplas | [`ex01_equacao_segundo_grau.py`](02-exercicios-oficiais/ex01_equacao_segundo_grau.py) |
| 02 | Velocidade média de uma viagem | [`ex02_velocidade_media_viagem.py`](02-exercicios-oficiais/ex02_velocidade_media_viagem.py) |
| 03 | Frequência de números com dicionário | [`ex03_frequencia_numeros.py`](02-exercicios-oficiais/ex03_frequencia_numeros.py) |

[📘 Acessar documentação completa dos exercícios oficiais](02-exercicios-oficiais/README.md)

---

# 🚀 Desafios extras

Os desafios extras foram acrescentados para ampliar e consolidar os conhecimentos desenvolvidos durante a Semana 04.

| Nº | Desafio | Arquivo |
|---:|---|---|
| 01 | Maior e menor valor da lista | [`desafio01_maior_menor_lista.py`](03-desafios-extras/desafio01_maior_menor_lista.py) |
| 02 | Média de notas | [`desafio02_media_notas_lista.py`](03-desafios-extras/desafio02_media_notas_lista.py) |
| 03 | Remoção de valores duplicados | [`desafio03_remover_duplicados.py`](03-desafios-extras/desafio03_remover_duplicados.py) |
| 04 | Ordenação de lista | [`desafio04_ordenar_lista.py`](03-desafios-extras/desafio04_ordenar_lista.py) |
| 05 | Cadastro de alunos com tuplas | [`desafio05_cadastro_alunos_tuplas.py`](03-desafios-extras/desafio05_cadastro_alunos_tuplas.py) |
| 06 | Estatísticas de uma lista | [`desafio06_estatisticas_lista.py`](03-desafios-extras/desafio06_estatisticas_lista.py) |
| 07 | Interseção de conjuntos | [`desafio07_intersecao_conjuntos.py`](03-desafios-extras/desafio07_intersecao_conjuntos.py) |
| 08 | Controle de estoque | [`desafio08_controle_estoque_dicionario.py`](03-desafios-extras/desafio08_controle_estoque_dicionario.py) |
| 09 | Contador de palavras | [`desafio09_contador_palavras.py`](03-desafios-extras/desafio09_contador_palavras.py) |
| 10 | Agenda de contatos | [`desafio10_agenda_contatos.py`](03-desafios-extras/desafio10_agenda_contatos.py) |
| 11 | Boletim de alunos | [`desafio11_boletim_alunos.py`](03-desafios-extras/desafio11_boletim_alunos.py) |
| 12 | Sistema simples de votação | [`desafio12_sistema_votacao.py`](03-desafios-extras/desafio12_sistema_votacao.py) |
| 13 | Carrinho de compras | [`desafio13_carrinho_compras.py`](03-desafios-extras/desafio13_carrinho_compras.py) |
| 14 | Controle de funcionários | [`desafio14_controle_funcionarios.py`](03-desafios-extras/desafio14_controle_funcionarios.py) |
| 15 | Mini projeto de biblioteca | [`desafio15_mini_projeto_biblioteca.py`](03-desafios-extras/desafio15_mini_projeto_biblioteca.py) |

[📘 Acessar documentação completa dos desafios extras](03-desafios-extras/README.md)

---

# 💡 Aprendizados consolidados

Ao concluir a Semana 04, são consolidados conhecimentos relacionados a:

### Programação

- criar e manipular listas;
- percorrer listas;
- acessar elementos por índice;
- utilizar `enumerate()`;
- utilizar `len()`;
- aplicar list comprehension;
- realizar fatiamento;
- construir matrizes;
- percorrer matrizes com laços aninhados;
- utilizar tuplas;
- desempacotar tuplas;
- compreender estruturas imutáveis;
- utilizar conjuntos;
- executar operações entre conjuntos;
- trabalhar com dicionários;
- criar associações chave-valor;
- percorrer dicionários;
- utilizar coleções aninhadas;
- selecionar a coleção mais adequada para cada problema;
- integrar diferentes estruturas de dados.

### Raciocínio lógico

- identificar quando um problema exige armazenamento de múltiplos valores;
- escolher estruturas adequadas aos dados;
- organizar informações relacionadas;
- calcular médias;
- buscar elementos;
- eliminar duplicidades;
- contabilizar ocorrências;
- modelar problemas utilizando coleções;
- dividir problemas maiores em funções menores;
- combinar conhecimentos das quatro semanas.

### Organização

- separar práticas, exercícios e desafios;
- manter nomenclatura padronizada;
- documentar cada etapa;
- estruturar programas maiores;
- utilizar funções auxiliares;
- organizar arquivos em pastas específicas;
- criar documentação navegável pelo GitHub.

### Git e GitHub

- verificar alterações com `git status`;
- selecionar arquivos com `git add`;
- registrar alterações com `git commit`;
- publicar alterações com `git push`;
- criar commits individualizados;
- escrever mensagens de commit descritivas;
- manter histórico da evolução das atividades;
- documentar a conclusão da semana.

---

# 🏆 Resultados da Semana 04

A organização planejada da Semana 04 contém:

- **15 práticas fundamentais**;
- **3 exercícios oficiais**;
- **15 desafios extras**;
- **33 arquivos Python**;
- README específico para práticas;
- README específico para exercícios;
- README específico para desafios;
- README principal da Semana 04.

---

# 📊 Resumo da Semana 04

| Categoria | Quantidade |
|---|---:|
| 🧪 Práticas fundamentais | 15 |
| 🧩 Exercícios oficiais | 3 |
| 🚀 Desafios extras | 15 |
| **Total de códigos Python** | **33** |

---

# 📈 Progresso

```text
Práticas             15 arquivos
Exercícios oficiais   3 arquivos
Desafios extras      15 arquivos
                     ───────────
Total                 33 arquivos
```

A atualização do percentual de conclusão deve acompanhar a execução, validação e publicação de cada atividade no repositório.

---

# 🧱 Evolução durante o curso

A progressão das quatro semanas do Python Básico pode ser observada da seguinte maneira:

```text
SEMANA 01
Fundamentos da linguagem
        ↓
SEMANA 02
Controle de fluxo
        ↓
SEMANA 03
Modularização e tratamento de exceções
        ↓
SEMANA 04
Coleções de dados
```

A Semana 04 utiliza conhecimentos construídos em todas as etapas anteriores.

Exemplo:

```text
Coleções
   │
   ├── Listas
   ├── Tuplas
   ├── Conjuntos
   └── Dicionários
        │
        ↓
Estruturas condicionais
        │
        ↓
Estruturas de repetição
        │
        ↓
Funções
        │
        ↓
Modularização
        │
        ↓
Programas mais completos
```

---

# 🎓 Encerramento do conteúdo

A Semana 04 representa a última semana de conteúdos do curso **Python Básico — +IFMG**.

Após o estudo dos conteúdos, execução das atividades e revisão, o fluxo de encerramento do curso é:

```text
Semana 04
    ↓
Revisão da Quarta Semana
    ↓
Revisão geral do curso
    ↓
Avaliação Final
    ↓
Conclusão do Python Básico
```

---

# 🔗 Navegação

- [🧪 Práticas fundamentais](01-praticas/README.md)
- [🧩 Exercícios oficiais](02-exercicios-oficiais/README.md)
- [🚀 Desafios extras](03-desafios-extras/README.md)
- [⬅️ Semana 03](../semana-03/README.md)
- [🏠 Voltar ao Python Básico](../README.md)

---

# 👨‍💻 Autor

**Rodrigo de Almeida Silveira**

Projeto desenvolvido como parte da trilha de estudos em **Python e Big Data — 160 horas**, iniciada pelo curso de **Python Básico — +IFMG**.