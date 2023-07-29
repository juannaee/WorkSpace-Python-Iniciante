import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=60)


usuarios = [
    {"id": 1, "nome": "Jose", "sobrenome": "Silva", "ativo": False},
    {"id": 2, "nome": "Maria", "sobrenome": "Silva", "ativo": True},
    {"id": 3, "nome": "Joao", "sobrenome": "Lemos", "ativo": True},
]


usuarios_inativos = [{**usuario} for usuario in usuarios if usuario["ativo"] != True]

p(usuarios_inativos)
