import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False)


lista_usuarios = [
    {"Nome": "JUAN", "STATUS": "Ativo", "teste": 1},
    {"Nome": "BRENNO", "STATUS": "Ativo", "teste": 0},
    {"Nome": "SAMUEL", "STATUS": "Ativo", "teste": 0},
    {"Nome": "JAIRO", "STATUS": "Ativo", "teste": 1},
    {"Nome": "Roberta", "STATUS": "Inativo", "teste": 1},
    {"Nome": "Bella", "STATUS": "Inativo", "teste": 1},
]

lista_usuarios_inativo = [
    {"Nome": "JUAN", "STATUS": "Inativo"},
    {"Nome": "BRENNO", "STATUS": "Inativo"},
]

lista_usuarios_att = [
    {**usuario} if usuario["teste"] == 0 else {**usuario} for usuario in lista_usuarios
]

lista_usuarios_att.append(lista_usuarios_inativo)

p(lista_usuarios_att)
