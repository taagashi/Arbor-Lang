from lark import Lark, Transformer
from arvore_binaria import Binary_seach_tree
from nomalizador import Normalizer

gramatica = """
    inicio: operacao+
    operacao: INSERIR NUMERO+
            | BUSCAR NUMERO 
            | PRE_ORDEM 
            | EM_ORDEM 
            | POS_ORDEM 
            | DELETAR NUMERO
            | MAIOR
            | MENOR
            | ALTURA
    
    
    PRE_ORDEM: "pre_ordem"
    EM_ORDEM: "em_ordem"
    POS_ORDEM: "pos_ordem"

    INSERIR: "inserir"
    BUSCAR: "buscar"
    DELETAR: "deletar"
    MAIOR: "maior"
    MENOR: "menor"
    ALTURA: "altura"
        
    NUMERO: /-?[0-9]+/

    %import common.WS
    %ignore WS
"""


class Interpreter(Transformer):
    def __init__(self):
        super().__init__()

        self.binary_tree = Binary_seach_tree()
        self.normalizer = Normalizer()
        self.parser = Lark(gramatica, start='inicio')

    def NUMERO(self, token):
        return int(token)

    def interpret(self, comands):
        self.parser = Lark(gramatica, start='inicio')
        tree = self.parser.parse(self.normalizer.normalize(comands))
        # print(tree.pretty())
        return self.transform(tree)

    def inicio(self, itens):
        valores_buscados = []
        for item in itens:
            if item is not None:
                valores_buscados.append(item)
        return valores_buscados

    def operacao(self, itens):
        operacao = str(itens[0])

        if operacao == 'inserir':
            for item in itens[1:]:
                self.binary_tree.inserir(item)
            return None

        elif operacao == 'pre_ordem':
            self.binary_tree.pre_ordem()
            return None

        elif operacao == 'em_ordem':
            self.binary_tree.em_ordem()
            return None

        elif operacao == 'pos_ordem':
            self.binary_tree.pos_ordem()
            return None

        elif operacao == 'buscar':
            return (operacao, self.binary_tree.buscar(itens[1]))

        elif operacao == 'deletar':
            self.binary_tree.deletar(itens[1])
            return None

        elif operacao == 'maior':
            return (operacao, self.binary_tree.maior())

        elif operacao == 'menor':
            return (operacao, self.binary_tree.menor())

        elif operacao == 'altura':
            return (operacao, self.binary_tree.altura())