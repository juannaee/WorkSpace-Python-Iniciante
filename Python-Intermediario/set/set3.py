lista_de_listas_de_inteiros = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 5, 9, 8, 7, 8, 95, 4, 5, 8, 5, 2, 1, 4, 5, 8, 5],
    [1, 1, 1, 6, 7, 8, 9, 9, 9, 5, 7, 8, 5, 2, 1],
    [1, 2, 3, 4, 5, 6, 9, 8, 8, 7, 4, 6, 8, 4],
]


def pegar_primeira_duplicata(lista_inteiro):
    numero_checkado = set()
    numero_duplicado = -1

    for numeros in lista_inteiro:
        print(numeros)

    for numeros in lista_inteiro:
        if numeros in numero_checkado:
            numero_duplicado = numeros
            break

        numero_checkado.add(numeros)
    print()

    if numero_duplicado != -1:
        return "Numero duplicado:", numero_duplicado
    else:
        return "Nao existem duplicatas!"


indice_lista = 0
for i, listas in enumerate(lista_de_listas_de_inteiros):
    print("Lista:", i + 1)
    print(pegar_primeira_duplicata(listas))
    print()
    print()
