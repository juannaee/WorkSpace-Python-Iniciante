def criar_func(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado

    return interna


def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Os valores devem ser string")


@criar_func
def inverte_string(string_qualquer):
    return string_qualquer[::-1]


c = inverte_string("teste")

print(c)
