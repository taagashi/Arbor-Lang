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