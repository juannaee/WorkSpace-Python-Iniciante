import os
os.system('cls')
frase = '               Olá mundo como vocês estão?, bem ?, ou mal ?                    '
lista_crua = frase.split(',')
print(lista_crua)

lista_consertada = []

for i, valor in enumerate(lista_crua):
    lista_consertada.append(lista_crua[i].strip())

print(lista_consertada)
lista_unida = '-'.join(lista_consertada)
print(lista_unida)
