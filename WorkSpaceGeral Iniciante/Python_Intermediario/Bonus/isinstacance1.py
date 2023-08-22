lista_de_tipos_iteraveis = [
    (1, 2, 3, 4, 5),
    {1, 2, 4},
    [1, 2, 3, 4, 5],
    2,
    2.5,
    300,
    "string",
]

for itens in lista_de_tipos_iteraveis:
    if isinstance(itens, str):
        print(itens.upper())
    if isinstance(itens, int):
        print(itens + 2)
