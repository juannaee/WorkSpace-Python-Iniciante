import pprint
from itertools import combinations, permutations, product


def p(iter):
    return pprint.pprint(list(iter), sort_dicts=False)


lista_pessoas = ["Luanar", "Juan"]
lista_camisas = [
    ["preta", "branca"],
    ["p", "g", "m"],
]

print("Combinations")
p(combinations(lista_pessoas, 2))
print("--------------------------------")
print("Permutations")
p(permutations(lista_pessoas, 2))
print("--------------------------------")
p(product(*lista_camisas))
