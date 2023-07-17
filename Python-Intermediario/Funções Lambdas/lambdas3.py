def execute(funcao, *args):
    return funcao(*args)


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


print(execute(criar_multiplicador(2), 3))
duplica = execute(lambda x: lambda y: x * y, 3)
print(duplica(6))


def soma_total(*args):
    return sum(args)


print(execute(soma_total, 10, 10, 10, 40, 40))

print(execute(lambda *args: sum(args), 10, 10, 10, 40, 40))
