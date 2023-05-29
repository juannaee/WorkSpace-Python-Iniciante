""" Testando comportamento das funções"""

import os

os.system("cls")


# Função de soma
def sum_values(value_1=None, value_2=None, value_3=None):
    """Tratando a possivel exceção para evitar string como argumentos"""
    try:
        value_1 = int(value_1)
        value_2 = int(value_2)
        value_3 = int(value_3)
        # Somando valores e verificando quais argumentos foram colocados
        if value_1 is None and value_2 is None and value_3 is None:
            return "Você não digitou nenhum valor!"
        elif value_1 is None:
            return value_2 + value_3, "Você não digitou o valor 1"
        elif value_2 is None:
            return value_1 + value_3, "Você não digitou o valor 2"
        elif value_3 is None:
            return value_1 + value_2, "Você não digitou o valor 3"
        else:
            return value_1 + value_2 + value_3, "Você digitou todos os valores"
    except ValueError:
        return "Você não digitou numeros"


resultado = sum_values(value_1="a", value_3=80)
print(resultado)
