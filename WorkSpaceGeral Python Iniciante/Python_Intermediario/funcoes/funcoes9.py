"""Exemplo de como adiar e controlar o uso de argumentos"""


def criar_multiplicadores(multiplicador):
    def valor_a_ser_multiplicado(numero):
        return numero * multiplicador

    return valor_a_ser_multiplicado


# Aqui enviamos primeiramente o argumento da primeira função.
duplicar = criar_multiplicadores(2)
triplicar = criar_multiplicadores(3)

# Aqui enviamos o segundo argumento.
print(duplicar(10))
print(triplicar(10))
