def sao_todos_numeros(*args):
    return all(isinstance(arg, (int, float)) for arg in args)


def soma(*args):
    total = 0
    try:
        if sao_todos_numeros(*args):
            total = sum(args)
            return True, total
        else:
            raise TypeError
    except TypeError:
        print("VALORES NAO NUMERICOS")
        return None


def flag_generator_():
    v = 0
    yield f"EXECUTANDO SCRIPT #{v + 1} FUNCAO: {soma.__name__}"
    resultado = soma(5, 5, 5, 5, 5, 5, 5, "S")

    if resultado is not None:
        print(f"Resultado:{resultado[1]}")
    else:
        print(f"ERRO SCRIPT {soma.__name__}")


gen = flag_generator_()
for i in gen:
    print(i)
