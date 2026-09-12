from DSL_arvore_binaria import DSLBinaryTree

# MANIPULAÇÃO DE ARVORE BINARIA UTILIZANDO LINGUAGEM NATURAL

dls_arvore_binaria = DSLBinaryTree()


dls_arvore_binaria.insert_comands("""
inserir 10 20 5 25
em_ordem
""")

numero_para_buscar = 10
resultado_de_busca = dls_arvore_binaria.insert_comands(f"buscar {numero_para_buscar}")


print(f"a busca de {numero_para_buscar} resultou em {resultado_de_busca}")