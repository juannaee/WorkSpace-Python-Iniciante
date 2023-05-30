import numpy as np


def multiplication(*args):
    return np.prod(args)


print(multiplication(2, 2, 3))


lista = [1, 2, 3, 4, 5]
lista.append(9)
print(lista)
