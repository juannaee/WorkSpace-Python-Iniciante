def parametros_decorador(ordem):
    def decorador(func):
        def funcao_decorada(*args, **kwargs):
            print(f"Decorador:{ordem}")
            print(f"DECORANDO A FUNCAO: {func.__name__}")

            return f"Decorada com sucesso", func(*args, **kwargs)

        return funcao_decorada

    return decorador


@parametros_decorador(ordem="Teste Soma")
def soma(x, y):
    return x + y


multiplicacao = parametros_decorador("Teste Multiplicacao")(lambda x, y: x * y)
multiplicacao_qualquer = multiplicacao(8, 5)
print(multiplicacao_qualquer)
soma_qualquer = soma(5, 5)
print(soma_qualquer)
