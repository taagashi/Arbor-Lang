# Arbor-Lang

Arbor-Lang é um projeto de uma DSL (linguagem específica de domínio) para manipulação de árvores binárias de busca, desenvolvido em Python com o Lark para definir e interpretar a gramática.

O objetivo é permitir a manipulação dessas árvores por meio de frases em linguagem natural. **Hoje, a DSL ainda não é 100% linguagem natural:** ela reconhece comandos com uma sintaxe específica. A interpretação de comandos dentro de frases livres é uma evolução planejada.

## Como funciona hoje

O interpretador recebe uma entrada com um ou mais comandos definidos na gramática e executa as operações sobre a árvore. Por exemplo:

```text
inserir 10 4 9 5
pre_ordem
em_ordem
pos_ordem
deletar 4
```

O comando `inserir` aceita vários números de uma vez. As operações previstas na gramática atual são:

| Comando | Operação |
| --- | --- |
| `inserir 10 4 9 5` | Insere um ou mais números inteiros na árvore. |
| `buscar 10` | Busca um número na árvore. |
| `pre_ordem` | Lista os valores na ordem: raiz, esquerda e direita. |
| `em_ordem` | Lista os valores na ordem: esquerda, raiz e direita (ordem crescente em uma árvore binária de busca). |
| `pos_ordem` | Lista os valores na ordem: esquerda, direita e raiz. |
| `deletar 10` | Solicita a remoção do número informado. |

Os comandos também podem ser escritos na mesma linha:

```text
inserir 10 20 30 2 em_ordem
```

Atualmente, a entrada precisa respeitar a gramática. Espaços e quebras de linha são ignorados, mas palavras adicionais de uma frase em português ainda não são aceitas.

## Objetivo: comandos dentro de frases em linguagem natural

A ideia é permitir entradas como:

```text
quero inserir 10 20 30 2 e depois quero listar com o em_ordem
```

Nesse exemplo, o interpretador deverá identificar as palavras-chave da gramática e seus argumentos dentro da frase, extraindo:

1. `inserir 10 20 30 2`
2. `em_ordem`

Em seguida, deverá executar as operações na ordem em que aparecem: primeiro inserir os números e depois listar a árvore em ordem crescente, produzindo:

```text
2 10 20 30
```

Assim, o usuário poderá fornecer uma entrada maior, com palavras e expressões ao redor dos comandos, e o interpretador deverá reconhecer os trechos relevantes para realizar as operações. A proposta é reconhecer palavras-chave e argumentos dentro do texto, sem exigir que toda a frase faça parte da gramática.

**Esse reconhecimento dentro de frases livres ainda não está implementado; ele é o objetivo de evolução do projeto.**
