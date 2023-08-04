produtos = [
    {"Produto_1": "Computador", "preco": 2500},
    {"Produto_2": "Celular", "preco": 3500},
    {"Produto_2": "TV", "preco": 8500},
]

produtos_preco_ajustado = [{*produto} for produto in produtos]

print(produtos_preco_ajustado)
