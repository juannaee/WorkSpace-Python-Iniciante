print("#########################")


def mutiplication(x, y):
    return x * y


def divide(x, y):
    return x / y


lista_de_numeros = [i for i in range(11)]


lista_de_numeros_multiplicado = [
    mutiplication(numeros, 2) for numeros in lista_de_numeros
]

lista_de_numeros_divididos = [divide(numeros, 2) for numeros in lista_de_numeros]

print("Lista de numeros original:", lista_de_numeros)
print("lista de numeros multiplicado por 2:", lista_de_numeros_multiplicado)
print("lista de numeros dividos por 2:", lista_de_numeros_divididos)
