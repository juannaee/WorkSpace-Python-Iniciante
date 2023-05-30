"""Testando Função com a bibliotecca numpy, com valores recebidos pelo input"""
import numpy as np
import os

os.system("cls")


def multiplication(*args):
    # np.prod tem a ação de multiplicar todos os argumentos
    return np.prod(args)


numero_de_interacoes = int(input("Digite quantos valores serão inseridos: "))
lista_valores = []

"""Criando For para controlar o numero de entrada de valores"""
for i in range(numero_de_interacoes):
    valor = int(input("Digite um valor: "))
    # Adicionando valores na lista
    lista_valores.append(valor)

resultado = multiplication(*lista_valores)
print(f"{resultado= }")
