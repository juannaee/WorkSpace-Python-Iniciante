numeros_iter = iter(range(0, 5))
print(numeros_iter)

print(next(numeros_iter))
print(next(numeros_iter))
print(next(numeros_iter))
print(next(numeros_iter))
print(next(numeros_iter))
# Chegando aqui estoura uma exceção que o proprio for trata - print(next(numeros_iter))

print('---------------------------------------------------------------------------------------------')
numeros_iter_2 = range(0, 5)
iteratador = iter(numeros_iter_2)


while True:
    try:

        print(next(iteratador))

    except StopIteration:
        print('Fim dos valores possiveis')
        break
