from node import Node

class Binary_seach_tree:
    def __init__(self):
        self.node = None

    def inserir(self, new_value):
        self.node = self.__inserir(new_value, self.node)

    def buscar(self, target):
        return self.__buscar(target, self.node)

    def pre_ordem(self):
        print('Pre ordem: ', end='')
        self.__pre_ordem(self.node)
        print()

    def em_ordem(self):
        print('Em ordem: ', end='')
        self.__em_ordem(self.node)
        print()

    def pos_ordem(self):
        print('Pos ordem: ', end='')
        self.__pos_ordem(self.node)
        print()

    def mapa_arvore(self):
        if self.node is None:
            print('(árvore vazia)')
            return

        nos_por_nivel = []
        posicoes = {}
        self.__posicionar_nos(self.node, 0, nos_por_nivel, posicoes)
        maior_largura = max(len(str(no.value)) for nos in nos_por_nivel for no in nos)
        espacamento = maior_largura + 4
        largura = max(1, (len(posicoes) - 1) * espacamento + maior_largura + 2)
        posicoes = {no: rank * espacamento + maior_largura // 2 + 1 for no, rank in posicoes.items()}
        linhas = [[' '] * largura for _ in range(len(nos_por_nivel) * 2 - 1)]

        for nivel, nos in enumerate(nos_por_nivel):
            y_no = nivel * 2
            for no in nos:
                x = posicoes[no]
                texto = str(no.value)
                inicio = x - len(texto) // 2
                for deslocamento, caractere in enumerate(texto):
                    linhas[y_no][inicio + deslocamento] = caractere

                if no.left is not None:
                    self.__desenhar_aresta(linhas[y_no + 1], x, posicoes[no.left], 'left')
                if no.right is not None:
                    self.__desenhar_aresta(linhas[y_no + 1], x, posicoes[no.right], 'right')

        for linha in linhas:
            print(''.join(linha).rstrip())

    def __posicionar_nos(self, node: Node, nivel: int, nos_por_nivel, posicoes, indice=None):
        if node is None:
            return 0 if indice is None else indice

        if len(nos_por_nivel) <= nivel:
            nos_por_nivel.append([])

        proximo_indice = self.__posicionar_nos(node.left, nivel + 1, nos_por_nivel, posicoes, indice)
        posicoes[node] = proximo_indice
        nos_por_nivel[nivel].append(node)
        proximo_indice += 1
        return self.__posicionar_nos(node.right, nivel + 1, nos_por_nivel, posicoes, proximo_indice)

    def __desenhar_aresta(self, linha, inicio, fim, lado):
        if inicio == fim:
            return

        direcao = 1 if fim > inicio else -1
        for x in range(inicio, fim, direcao):
            linha[x] = '─'

        linha[fim] = '▶' if lado == 'right' else '◀'

    def maior(self):
        return self.__maior(self.node).value

    def menor(self):
        return self.__menor(self.node).value

    def altura(self):
        return self.__altura(self.node)

    def deletar(self, target):
        self.node = self.__deletar(target, self.node)

    def __buscar(self, target, node:Node):
        if node is None:
            return None
        elif node.value == target:
            return target

        if target > node.value:
            return self.__buscar(target, node.right)
        elif target < node.value:
            return self.__buscar(target, node.left)

    def __em_ordem(self, node:Node):
        if node is None:
            return

        self.__em_ordem(node.left)
        print(node.value, end=' ')
        self.__em_ordem(node.right)

    def __pre_ordem(self, node:Node):
        if node is None:
            return

        print(node.value, end=' ')
        self.__pre_ordem(node.left)
        self.__pre_ordem(node.right)

    def __pos_ordem(self, node:Node):
        if node is None:
            return

        self.__pos_ordem(node.left)
        self.__pos_ordem(node.right)
        print(node.value, end=' ')

    def __inserir(self, new_value, node:Node):
        if node is None:
            return Node(new_value)

        if new_value > node.value:
            node.right = self.__inserir(new_value, node.right)
        elif new_value < node.value:
            node.left = self.__inserir(new_value, node.left)

        return node

    def __maior(self, node:Node):
        if node.right is None:
            return node

        return self.__maior(node.right)

    def __menor(self, node:Node):
        if node.left is None:
            return node

        return self.__menor(node.left)

    def __altura(self, node:Node):
        if node is None:
            return -1
        
        hleft = self.__altura(node.left)  
        hright = self.__altura(node.right)

        if hright > hleft:
            return hright + 1
        return hleft + 1

    def __deletar(self, target, node: Node):
        if node is None:
            return None

        if target > node.value:
            node.right = self.__deletar(target, node.right)

        elif target < node.value:
            node.left = self.__deletar(target, node.left)

        else:
            if node.left is None and node.right is None:
                return None

            if node.left is not None and node.right is not None:
                sucessor: Node = self.__menor(node.right)
                node.value = sucessor.value
                node.right = self.__deletar(sucessor.value, node.right)

            elif node.right is not None:
                return node.right

            elif node.left is not None:
                return node.left

        return node
