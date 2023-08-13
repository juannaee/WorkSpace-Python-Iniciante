from itertools import groupby

lista_qualquer = ["a", "a", "a", "a", "a", "a", "a", "b", "c", "d", "e", "a"]


for i, grupo in groupby(sorted(lista_qualquer)):
    lista = list(grupo)
    print(f"Valor: {i}")
    print(f"Repeticoes: {lista}, \n Numero de repeticoes: {len(lista)}")
