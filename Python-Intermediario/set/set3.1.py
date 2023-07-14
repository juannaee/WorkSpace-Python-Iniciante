lista_de_listas = [
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    [1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 9, 2, 6, 6, 5, 4],
    [120, 120, 3, 3, 5, 6, 8, 7, 5, 9, 8, 7],
]


def pegar_numero_duplicata(lista_de_numeros):
    numeros_checkado = set()
    numero_duplicado = -1

    print(lista_de_numeros)

    for numero in lista_de_numeros:
        if numero in numeros_checkado:
            numero_duplicado = numero
            break
        numeros_checkado.add(numero)

    if numero != -1:
        return "Numero duplicata: ", numero_duplicado
    return "Não existem numeros duplicatas"


lista_numero = 0
for i, listas in enumerate(lista_de_listas):
    lista_numero = i + 1
    print("Lista:", lista_numero)
    print(pegar_numero_duplicata(listas))
    print()
