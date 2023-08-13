from itertools import zip_longest


def ziper(lista_1, lista_2):
    intervalo = min(len(lista_1), len(lista_2))
    return [(lista_1[i], lista_2[i]) for i in range(intervalo)]


lista_1 = [1, 2]
lista_2 = ["lista1", "lista2", "lista3"]

print(ziper(lista_1, lista_2))


print(list(zip(lista_1, lista_2)))
print(list(zip_longest(lista_1, lista_2, fillvalue="Sem atribuicao")))
