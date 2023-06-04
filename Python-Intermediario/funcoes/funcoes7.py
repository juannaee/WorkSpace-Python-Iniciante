import os
import random


def gerar_dados():
    def cpf_cliente():
        cpf = ""
        for i in range(9):
            cpf += str(random.randint(0, 9))
        return f"{cpf}"

    return cpf_cliente


s1 = gerar_dados()
print(s1())
print("10488775400")
funcao_teste = s1()

