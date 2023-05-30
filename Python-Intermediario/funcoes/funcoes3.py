"""Comportamento de empacotamento e desempacotamento
em funções utilizando listas ou tuplas"""


# a função recebe os argumentos desempacotado, indicado com o caractere *.
def soma_argumentos(*args):
    # Para a função "sum" funcionar ela deve receber argumentos desempacotado,
    # por isso a razão de desempacota o args.
    return sum(args)


# Aqui  criamos uma tupla para servir como argumentos.
valores = 1, 2, 3, 4, 5, 7, 8, 9, 10
# Logo depois desempacotamos essa tupla para jogar na função.
print(soma_argumentos(*valores))
