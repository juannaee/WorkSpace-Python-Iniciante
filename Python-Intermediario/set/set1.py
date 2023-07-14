lista_1 = [1, 2, 3]

set_1 = set(lista_1)

print(set_1)

set_1.add(89595)
set_1.update({98785, "Teste 1"})

print(set_1)

valores_alternativos = {
    "valor_1": 123,
    "Valor_2": 321,
}

novo_valor = 0
for valores in valores_alternativos.values():
    novo_valor = valores
    set_1.add(novo_valor)

print(set_1)
set_1.discard(321)
print(set_1)
