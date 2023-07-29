import sys

lista = [n for n in range(100000)]
gerenator = (n for n in range(100000))


print(sys.getsizeof(lista))
print(sys.getsizeof(gerenator))

while next(gerenator) <= 40:
    print(next(gerenator))
