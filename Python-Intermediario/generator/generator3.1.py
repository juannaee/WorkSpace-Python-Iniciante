def sao_todos_numeros(*args):
    return all(isinstance(arg, (int, float)) for arg in args)


def soma(*args):
    total = 0
    try:
        if sao_todos_numeros(*args):
            total = sum(args)
            return True, total
        else:
            raise TypeError("Existem valores nao numericos")
    except TypeError as error:
        print(f"ERROR: {error}")
        print(f"Tipo excecao: {error.__class__.__name__}")
        return None


def mult(*args):
    total = 0
    try:
        if total == 0:
            total = +1
        if sao_todos_numeros(*args):
            for i in args:
                total = total * i
            return True, total
        else:
            raise TypeError("Existem valores nao numericos")
    except TypeError as error:
        print(f"{error}")
        print(f"Tipo excecao: {error.__class__.__name__}")
        return None


def func_generator_():
    v = 0
    yield f"EXECUTANDO SCRIPT #{v + 1} FUNCAO: '{soma.__name__}'"
    resultado = soma("a", 2)

    if resultado is not None:
        print(f"Resultado:{resultado[1]}")
    print("<====================================================>")
    yield f"EXECUTANDO SCRIPT #{v + 2} FUNCAO: '{mult.__name__}'"
    resultado = mult(2, 10)

    if resultado is not None:
        print(f"RESULTADO: {resultado[1]}")


gen = func_generator_()
for i in gen:
    print(i)
