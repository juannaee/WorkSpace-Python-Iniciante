def mostrar_resultado(v):
    return f"Resultado da operação: {v}"


def flag_str(f):
    return f"Executando Script /// Função: {f.__name__}"


def sao_todos_numeros(*args):
    return all(isinstance(arg, (float, int)) for arg in args)


def mostrar_excecao(error):
    print(f"Error: {error}")
    print(f"Tipo de error: {error.__class__.__name__}")
    return None


def verificar_numeros(*args):
    try:
        if sao_todos_numeros(*args) == True:
            return True
        else:
            raise TypeError("Existem valores não numericod")

    except TypeError as error:
        return mostrar_excecao(error)


def soma(*args):
    total = 0
    if verificar_numeros(*args) == True:
        total = sum(args)
        return mostrar_resultado(total)


def generator_func():
    flag_str(soma())
