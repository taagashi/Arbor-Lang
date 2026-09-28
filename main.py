from DSL_arvore_binaria import DSLBinaryTree

dsl_arvore_binaria = DSLBinaryTree()


print(dsl_arvore_binaria.insert_comands("""
quero inserir 10, 20, 5, 25, 3, 40
encontrar o maior valor
e saber qual a altura da árvore
buscar o numero 5 e organizar a arvore em_ordem deletar 20 e 
visualizar em pre_ordem 
"""))