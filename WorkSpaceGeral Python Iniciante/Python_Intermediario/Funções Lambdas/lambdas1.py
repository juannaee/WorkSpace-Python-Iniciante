# Sem Lambda functions

lista = [
    {"Idade": 20, "Nome": "John", "Sobrenome": "Gabriel"},
    {"Idade": 21, "Nome": "Juan", "Sobrenome": "Guilherme"},
    {"Idade": 19, "Nome": "Bianca", "Sobrenome": "Maria"},
    {"Idade": 29, "Nome": "Samuel", "Sobrenome": "Lessan"},
]


def ordenar(item):
    return item["Nome"]


lista.sort(key=ordenar)

for dicts in lista:
    print(dicts)


# Com Lambda functions


print()


def exibir_lista(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item["Idade"], reverse=True)

exibir_lista(l1)
