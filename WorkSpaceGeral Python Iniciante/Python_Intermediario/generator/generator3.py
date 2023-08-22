def sao_todos_numeros(*args):
    return all(isinstance(arg, (int, float)) for arg in args)


def mostrar_excecao(error):
    print(f"{error}")
    print(f"Tipo exceção: {error.__class__.__name__}.")
    return None


def verificar_numeros(*args):
    try:
        if sao_todos_numeros(*args):
            return True
        else:
            raise TypeError("Valores não numéricos.")
    except TypeError as error:
        return mostrar_excecao(error)


def mostrar_mensagem_excutando(func):
    return f"Executando Script /// Função: '{func.__name__}.'"


def mostrar_resultado(total):
    return f"Resultado: {total}."


def soma(*args):
    total = 0
    if verificar_numeros(*args):
        total = sum(args)
        return mostrar_resultado(total)


def mult(*args):
    total = 1
    if verificar_numeros(*args):
        for i in args:
            total *= i
        return mostrar_resultado(total)


def func_generator_():
    yield mostrar_mensagem_excutando(soma)
    result_soma = soma(2, 2, 5, 6, 8, "a")
    if result_soma is not None:
        print(result_soma)

    print("<====================================================>")

    yield mostrar_mensagem_excutando(mult)
    result_mult = mult(2, 10)
    if result_mult is not None:
        print(result_mult)


gen = func_generator_()
for i in gen:
    print(i)
