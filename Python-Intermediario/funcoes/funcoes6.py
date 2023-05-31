def executar(funcao, *args):
    return funcao(*args)


def mensagem(nome, sobrenome):
    return f"{nome} {sobrenome}"


print(executar(mensagem, "Juan", "Guilherme"))


