import os


os.system("cls")


pessoa_1 = {
    "primeiro_nome": "Juan",
    "Segundo_nome": "Guilherme",
    "Idade": 21,
}


# get tras o valor de acordo com o nome da chave
print(pessoa_1.get("Idade"))
print(pessoa_1.get("primeiro_nome"))
print(pessoa_1.get("Segundo_nome"))


# o pop também tras, porém ele exclui do dicionario
chave_excluida_1 = pessoa_1.pop("Segundo_nome")
print(chave_excluida_1)
print(pessoa_1)


# o pop item exclui do dicionario a ultima chave dele
ultima_chave = pessoa_1.popitem()
print(pessoa_1)

# com o update podemos fazer varias coisas ao mesmo tempo tanto atualizar quanto, adicionar

pessoa_1.update({"sobrenome": "Guilherme", "Idade": 21})
print(pessoa_1)
pessoa_1.update(id=271114)
tuple = (("Aniversario", "27/11/2001"),)
pessoa_1.update(tuple)
print(pessoa_1)
lista = [["cpf", 10488775400], ["cep", 441300]]

pessoa_1.update(lista)
print(pessoa_1)
