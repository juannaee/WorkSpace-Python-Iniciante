def criar_multiplicadores(multiplicador):
    def valor_a_ser_multiplicado(numero):
        return numero * multiplicador

    return valor_a_ser_multiplicado


duplicar = criar_multiplicadores(2)
triplicar = criar_multiplicadores(3)

print(duplicar(10))
print(triplicar(10))
