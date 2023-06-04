def criar_produto(tipo_produto):
    def produto(nome_produto):
        return f"{tipo_produto = },{nome_produto = }"

    return produto


produto_1 = criar_produto("Eletronico")
produto_2 = criar_produto("Frios")
produto_3 = criar_produto("Quimico")

print(produto_1("Micro-Ondas"))
print(produto_2("Queijo"))
print(produto_3("Uranio"))
