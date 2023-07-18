dict_1 = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# Empacotamento
(a1, a2), (a3, a4), (a5, a6), *_ = dict_1.items()
print(a1, "=", a2, a3, "=", a4, a5, "=", a6)

# Desempacotamento
dict_2 = {
    "d": 4,
    "e": 5,
    "f": 6,
}

dict_tudo_junto = {**dict_1, **dict_2}
print(dict_tudo_junto)


print("#===============================================#")


def exibir_dict(*args, **kargs):
    print("NÃO NOMEADOS: ", args)
    print("NOMEADOS:", kargs)


exibir_dict(2, 3, 4, 5, 6, nome="Juan", sobrenome="Guilherme")

print("#===============================================#")


def exibir_dict_tudo_junto(*args, **kwargs):
    for i, valor in kwargs.items():
        print(i, "=", valor)


exibir_dict_tudo_junto(**dict_tudo_junto)
