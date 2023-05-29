""" Testando  comportamentos das funções com tuplas"""
import os


def sum_args(*args):
    """Função de soma de argumentos"""
    # Criando um acumlador
    total = 0
    # correndo por todos os valores dos argumentos
    for arg in args:
        total += arg
    print(args)
    return total


resultado_soma = sum_args(5, 5)
print(resultado_soma)

teste_numero = 1
