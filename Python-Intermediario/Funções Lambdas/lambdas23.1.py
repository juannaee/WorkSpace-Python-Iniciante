def executa(funcao, *args):
    return funcao(*args)


print(executa(lambda x, y: x + y, 10, 10))
print(executa(lambda x, y: x - y, 10, 5))

mutiplicador = executa(lambda x: lambda y: x * y, 10)
print(mutiplicador(2))


lista = [
    {"ID": 1, "STATUS": "ATIVE"},
    {"ID": 2, "STATUS": "INATIVE"},
    {"ID": 1, "STATUS": "ATIVE"},
    {"ID": 1, "STATUS": "ATIVE"},
    {"ID": 2, "STATUS": "INATIVE"},
]


def exibir_lista(lista):
    for i in lista:
        print(i)


l1 = sorted(lista, key=lambda x: x["ID"], reverse=True)
exibir_lista(l1)

lista_2 = [
    {"ID": 1, "STATUS": "ONLINE"},
    {"ID": 0, "STATUS": "OFFLINE"},
    {"ID": 0, "STATUS": "OFFLINE"},
]

print()
l2 = sorted(lista, key=lambda x: x["ID"])
exibir_lista(l2)
