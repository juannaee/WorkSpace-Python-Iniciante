def soma(x, y):
    return x + y


def multiply(x, y):
    return x * y


def executa(f, x):
    def interna(y):
        return f(x, y)

    return interna


soma_por_cinco = executa(soma, 5)
multiply_por_cinco = executa(multiply, 5)

print(multiply_por_cinco(10))
print(soma_por_cinco(2))
