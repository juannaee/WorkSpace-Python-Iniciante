import os

os.system('cls')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[4] = 14
print(lista)
lista.append(11)
# Recorta o ultimo item da lista
lista.pop()
lista.append(12)
lista.append(13)
print(lista)
lista.pop(3)
print(lista)
lista.insert(0, -1)
print(lista)
