import pprint


def print_p(v):
    pprint.pprint(v, sort_dicts=False)


produtos_1 = [
    {"name": "Computador", "Price": 2500},
    {"name": "PS4", "Price": 3500},
    {"name": "PS5", "Price": 4500},
    {"name": "teste3", "Price": 45000},
    {"name": "teste4", "Price": 8500},
    {"name": "teste5", "Price": 35000},
    {"name": "teste6", "Price": 2890},
]
produtos_2 = [
    {**produto, "Price": produto["Price"] * 2}
    if produto["Price"] > 2500
    else {**produto}
    for produto in produtos_1
    if produto["Price"] < 3000
]


print_p(produtos_2)
