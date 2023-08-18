def execute(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def multi(x, y):
    return x * y


print(execute(soma, 10, 10))
print(execute(multi, 10, 10))

print(execute(lambda x, y: x + y, 10, 10))
print(execute(lambda x, y: x * y, 10, 10))
