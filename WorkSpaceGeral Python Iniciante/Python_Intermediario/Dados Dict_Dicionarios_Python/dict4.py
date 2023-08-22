import os

os.system("cls")

pessoa = {"nome": "Pedro", "idade": 25, "sexo": "M"}

print("Pegando o tamanho do dicionario aparti da quantidade de chaves:")
print(len(pessoa))

print("Pegando suas chaves:")
print(pessoa.keys())

print(
    "Transformando o dicicionario em uma lista para pegar uma chave parti do seu numero de indices: "
)
print(list(pessoa.keys())[0])

print("Dando loop para trazer suas chaves de forma iteravel:")
for chaves in pessoa.keys():
    print(chaves)

print("Dando loop para pegar os valores da chave de forma iteravel:")
for valores in pessoa.values():
    print(valores)


print("Dando loop para pegar as chaves e o valores: ")
for chave, valor in pessoa.items():
    print(chave, ":", valor)


print(
    "Criando um valor padrão para uma chave que talvez naõ exista no meu dicionario: "
)

pessoa.setdefault("peso", 75.5)
print(pessoa.get("peso"))
