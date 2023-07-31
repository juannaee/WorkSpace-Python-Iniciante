import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=50)


lista = [
    (x, y) if x != 2 else (x * 1000, y * 1000)
    for x in range(1, 6)
    for y in range(1, 4)
    if x != 2
]

p(lista)
