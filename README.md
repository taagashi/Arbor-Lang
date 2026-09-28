# Arbor-Lang

Arbor-Lang é um projeto de uma DSL (linguagem específica de domínio) para manipulação de árvores binárias de busca, desenvolvido em Python com o Lark para definir e interpretar a gramática.

O projeto permite manipular essas árvores por meio de comandos escritos diretamente ou inseridos em frases em linguagem natural. Um normalizador identifica as palavras-chave e os números relevantes antes de enviar a entrada para a gramática.

## Como funciona hoje

O interpretador recebe uma entrada com um ou mais comandos definidos na gramática e executa as operações sobre a árvore. Por exemplo:

```text
inserir 10 4 9 5
pre_ordem
em_ordem
pos_ordem
mapa_arvore
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
| `mapa_arvore` | Exibe a árvore no terminal, com os valores menores à esquerda, os maiores à direita e setas indicando os ramos. |
| `deletar 10` | Solicita a remoção do número informado. |
| `maior` | Retorna o maior valor armazenado. |
| `menor` | Retorna o menor valor armazenado. |
| `altura` | Retorna a altura da árvore. |

### Visualização da árvore

Depois de inserir os valores, use `mapa_arvore` para desenhar a estrutura no terminal:

```text
inserir 10 5 15 3 7 12 20
mapa_arvore
```

Saída esperada:

```text
          10
     ◀─────┴─────▶
      5           15
   ◀──┴──▶     ◀──┴──▶
   3     7     12    20
```

Cada nível é mostrado abaixo do anterior. A seta `◀` aponta para um filho à esquerda e `▶` aponta para um filho à direita, mantendo a propriedade da árvore binária de busca.

Os comandos também podem ser escritos na mesma linha:

```text
inserir 10 20 30 2 em_ordem
```

## Comandos em frases em linguagem natural

Além da sintaxe direta, é possível enviar uma frase com palavras adicionais. O normalizador filtra o texto e mantém apenas as palavras-chave da DSL e os números. Por exemplo:

```text
gostaria de inserir 10 20 30 e logo depois ver como esta o mapa_arvore, buscar 20 e assim por diante para no final fazer em_ordem e deletar 20 e quero ver o mapa_arvore de novo
```

Depois da normalização, a entrada fica equivalente a:

```text
inserir 10 20 30 mapa_arvore buscar 20 em_ordem deletar 20 mapa_arvore
```

O interpretador então envia essa sequência para a gramática e executa as operações na ordem em que aparecem: insere os valores, exibe o mapa, busca o valor `20`, lista a árvore em ordem, remove o valor `20` e exibe o mapa novamente.

Palavras que não fazem parte da gramática são descartadas durante a normalização, sem interferir na execução dos comandos reconhecidos.
