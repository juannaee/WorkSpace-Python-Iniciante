lista = [
    {"ID": 1, "Name": "Juan"},
    {"ID": 2, "Name": "Samuel"},
    {"ID": 3, "Name": "Brenno"},
    {"ID": 4, "Name": "Jairo"},
]


def exibir_list(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda x: x["ID"], reverse=False)
exibir_list(l1)
