lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [1, 2, 3, 4, 5]

print("Sem List Comprehension")
soma_de_listas = []
for i in range(len(lista_2)):
    soma_de_listas.append(lista_1[i] + lista_2[i])

print(soma_de_listas)

print("----------------------------------------------------")


print("Com List Comprehension(Sem metodo python)")


def soma_de_lista(lista_1, lista_2):
    intervalo = min(len(lista_1), len(lista_2))
    return [(lista_1[i] + lista_2[i]) for i in range(intervalo)]


print(soma_de_lista(lista_1, lista_2))


print("----------------------------------------------------")


def soma_de_lista_2(lista_1, lista_2):
    return [x + y for x, y in zip(lista_1, lista_2)]


print("Com List Comprehension com metodo python)")

print(soma_de_lista_2(lista_1, lista_2))
