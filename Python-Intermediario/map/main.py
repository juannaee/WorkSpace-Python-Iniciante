from functools import partial
import pprint


def p(x):
    pprint.pprint(list(x))


def aumentar_preco(valor, porcentagem):
    return round(valor * porcentagem, 2)


def mudar_preco_produtos(produto):
    return {**produto, "Preco": aumentar_preco_10_por_cento(produto["Preco"])}


aumentar_preco_10_por_cento = partial(aumentar_preco, 1.1)

lista_de_produtos = [
    {"Nome": "TV", "Preco": 2500},
    {"Nome": "Celular", "Preco": 5200},
]

lista_de_produtos_atualizada = map(mudar_preco_produtos, lista_de_produtos)
p(lista_de_produtos_atualizada)
