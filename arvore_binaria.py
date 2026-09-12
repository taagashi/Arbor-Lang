from node import Node

class Binary_seach_tree:
    def __init__(self):
        self.node = None

    def inserir(self, new_value):
        self.node = self.__inserir(new_value, self.node)

    def buscar(self, target):
        return self.__buscar(target, self.node)

    def pre_ordem(self):
        self.__pre_ordem(self.node)
        print()

    def em_ordem(self):
        self.__em_ordem(self.node)
        print()

    def pos_ordem(self):
        self.__pos_ordem(self.node)
        print()

    def deletar(self, target):
        self.node = self.__deletar(target, self.node)

    # RENATA, AQUI SAO OS METODOS RECURSIVOS
    def __buscar(self, target, node):
        if node.value == target:
            return target
        elif node is None:
            return None

        if target > node.value:
            self.__buscar(target, node.right)
        elif target < node.value:
            self.__buscar(target, node.left)

    def __pre_ordem(self, node:Node):
        if node is None:
            return

        print(node.value, end=' ')
        self.__pre_ordem(node.left)
        self.__pre_ordem(node.right)

    def __em_ordem(self, node:Node):
        if node is None:
            return

        self.__em_ordem(node.left)
        print(node.value, end=' ')
        self.__em_ordem(node.right)

    def __pos_ordem(self, node:Node):
        if node is None:
            return

        self.__pos_ordem(node.left)
        self.__pos_ordem(node.right)
        print(node.value, end=' ')

    def __inserir(self, new_value, node):
        if node is None:
            return Node(new_value)

        if new_value > node.value:
            node.right = self.__inserir(new_value, node.right)
        elif new_value < node.value:
            node.left = self.__inserir(new_value, node.left)

        return node

    def __menor(self, node:Node):
        if node.left is None:
            return node

        self.__menor(node.left)

    def __deletar(self, target, node:Node):
        if node is None:
            return None

        if target > node.value:
            node.right = self.__deletar(target, node.right)
        elif target < node.value:
            node.left = self.__deletar(target, node.left)

        else:
            if node.left is None and node.right is None:
                return None

            if node.right is not None:
                return node.right

            if node.left is not None:
                return node.left

            if node.left is not None and node.right is not None:
                sucessor:Node = self.__menor(node.right)
                node.value = sucessor.value
                node.right = self.__deletar(sucessor.value, node.right)

        return node
