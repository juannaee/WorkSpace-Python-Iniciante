import os
os.system('cls')
lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_1, *_ = lista_a
print(valor_1)
_, valor_2, *_ = lista_a
print(valor_2)
_, _, valor_3, *_ = lista_a
print(valor_3)

# como boas praticas devemos renomear a variavel que recebe o resto da listapara _ *_
# caso não vamos utilizar de alguma forma.
