import os

os.system('cls')

duplas = [
    ['Juan', 'Julia'],
    ['Bianca', 'Joana']
]

for dupla in duplas:
    for pessoas in dupla:
        print(pessoas)


# Desemcopatando uma lista ou iteravel com chamadas de função

print(*duplas, sep='\n')
