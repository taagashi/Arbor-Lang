from DSL_arvore_binaria import DSLBinaryTree

dsl_arvore_binaria = DSLBinaryTree()


print(dsl_arvore_binaria.insert_comands("""
quero inserir 10, 20 e 30 
buscar o numero 20
buscar 30
e organizar a arvore em_ordem
deletar 20 
e visualizar em pre_ordem 
"""))