pessoa_1 = {}

pessoa_1.update(
    primeiro_nome=input("Digite seu primeiro nome: "),
    segundo_nome=input("Digite seu sobrenome: "),
)

dados_pessoa_1 = {}

dados_pessoa_1.update(cpf=input("Digite seu CPF: "))
pessoa_1.update(dados_pessoa_1)
print(pessoa_1)
