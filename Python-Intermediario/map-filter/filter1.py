import pprint


def printando(p):
    return pprint.pprint(list(p), sort_dicts=False)


lista_de_produtos = [
    {"Nome": "TV", "Preco": 1200.75},
    {"Nome": "Celular", "Preco": 799.99},
    {"Nome": "Notebook", "Preco": 1500.50},
    {"Nome": "Fone de Ouvido", "Preco": 49.90},
    {"Nome": "Mouse", "Preco": 19.75},
    {"Nome": "Teclado", "Preco": 39.30},
    {"Nome": "Cmera", "Preco": 299.45},
    {"Nome": "Impressora", "Preco": 199.00},
    {"Nome": "Tablet", "Preco": 349.85},
    {"Nome": "Smartwatch", "Preco": 99.50},
]


print("Lista original: ")
printando(lista_de_produtos)
print("----------------------------------")


print("Lista produtos > 100 atualizados sem filter: ")
lista_de_produtos_att_1 = [
    {**produtos} for produtos in lista_de_produtos if produtos["Preco"] > 150
]
printando(lista_de_produtos_att_1)
print("----------------------------------")


print("Lista produtos < 180 atualizados com filter: ")
lista_de_produtos_att_2 = filter(lambda p: p["Preco"] <= 180, lista_de_produtos)
printando(lista_de_produtos_att_2)
