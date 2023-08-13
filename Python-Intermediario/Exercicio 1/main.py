import pprint
from dados import produtos


def p(x):
    pprint.pprint(
        x,
        sort_dicts=False,
        compact=True,
    )


novos_profutos = [{**p, "Preco": round(p["Preco"] * 1.1, 2)} for p in produtos]


p(novos_profutos)
produtos_ordenados = sorted(novos_profutos, key=lambda x: x["Preco"], reverse=True)


print("================================")
print("Produtos do maior para o menor:")
for p in produtos_ordenados:
    print(p)
