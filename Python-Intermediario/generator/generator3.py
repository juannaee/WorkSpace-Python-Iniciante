def soma(v1, v2):
    try:
        v1 = int(v1)
        v2 = int(v2)
        return True, v1 + v2

    except ValueError:
        print("Valores nao numericos!")


def subtracao(v1, v2):
    try:
        v1 = int(v1)
        v2 = int(v2)
        return True, v1 - v2
    except ValueError:
        print("Valores nao numericos!")


def flag_generator(v=0):
    yield f"RODANDO EXECUTAVEL #{v}: SOMA"
    resultado = soma(4, 5)
    if resultado is not None:
        print(f"Resultado soma:{resultado[1]}")
        print("!!PASSOU!!")
    else:
        print("ERROR!")

    yield f"RODANDO EXECUTAVEL #{v+1}: SUBTRACAO"
    resultado = subtracao(10, 2)
    if resultado is not None:
        print(f"Resultado subtracao:{resultado[1]}")
        print("!!PASSOU!!")
    else:
        print("ERROR!")

    return "FINALIZADO"


gen = flag_generator(1)

for i in gen:
    print(i)
