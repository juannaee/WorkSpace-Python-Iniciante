pessoa = {}


chave_nome = "Nome"
chave_sobrenome = "Sobrenome"
chave_idade = "Idade"


pessoa[chave_nome] = "João"
pessoa[chave_sobrenome] = "Silva"
pessoa[chave_idade] = 35

del pessoa[chave_nome]

if pessoa.get("Nome") is not None:
    print(pessoa.get("Nome"), "Existe!!")
else:
    print("Chave Inexistente!")
