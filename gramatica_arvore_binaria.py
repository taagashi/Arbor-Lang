from lark import Lark, Transformer
from arvore_binaria import Binary_seach_tree

gramatica = """
    inicio: operacao+
    operacao: INSERIR NUMERO+
            | BUSCAR NUMERO 
            | PRE_ORDEM 
            | EM_ORDEM 
            | POS_ORDEM 
            | DELETAR NUMERO
    
    
    PRE_ORDEM: "pre_ordem"
    EM_ORDEM: "em_ordem"
    POS_ORDEM: "pos_ordem"

    INSERIR: "inserir"
    BUSCAR: "buscar"
    DELETAR: "deletar"
        
    NUMERO: /-?[0-9]+/

    %import common.WS
    %ignore WS
"""


class Interpreter(Transformer):
    def __init__(self):
        super().__init__()

        self.binary_tree = Binary_seach_tree()
        self.parser = Lark(gramatica, start='inicio')

    def NUMERO(self, token):
        return int(token)

    def interpret(self, comands):
        self.parser = Lark(gramatica, start='inicio')
        tree = self.parser.parse(comands)
        return self.transform(tree)

    def inicio(self, itens):
        return itens[0] if len(itens) == 1 else itens[1]

    def operacao(self, itens):
        operacao = str(itens[0])

        if operacao == 'inserir':
            for item in itens[1:]:
                self.binary_tree.inserir(item)

        elif operacao == 'pre_ordem':
            self.binary_tree.pre_ordem()

        elif operacao == 'em_ordem':
            self.binary_tree.em_ordem()

        elif operacao == 'pos_ordem':
            self.binary_tree.pos_ordem()

        elif operacao == 'buscar':
            return self.binary_tree.buscar(itens[1])

        elif operacao == 'deletar':
            self.binary_tree.deletar(itens[1])
