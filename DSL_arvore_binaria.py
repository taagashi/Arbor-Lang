from gramatica_arvore_binaria import Interpreter

class DSLBinaryTree:
    def __init__(self):
        self.interpreter = Interpreter()

    def insert_comands(self, comands):
        return self.interpreter.interpret(comands)