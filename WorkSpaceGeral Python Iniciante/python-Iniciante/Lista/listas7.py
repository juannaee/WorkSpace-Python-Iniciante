import os

os.system('cls')
lista = [0, 1, 2, 3]

# Dessa forma os enumerate também não é consumido, "Excluido", porém sempre vai ta criando um novo por conta do for
for item in enumerate(lista):
    print(item)


# Dessa forma o enumerate não vai ser consumido, ou seja guardando os indicieis na memoria
lista_enumerada = list(enumerate(lista))

print('------------------------------------------------------------------------------------------')
for item in lista_enumerada:
    print(item)


print('------------------------------------------------------------------------------------------')
# Outra forma de fazer e muito mais pratica e limpa seria fazer o desempacotamento
# Relembrando a sintaxe:
valor_a, valor_b, valor_c, valor_d, *_ = lista
# print(valor_a)
# Dessa forma podemos usar essa sintaxe pra deixar o codigo mais limpo da seguinte forma
for indice, valor in enumerate(lista):
    print(indice, valor)
