dict_1 = {"Valor_1": 50, "Valor_2": 100, "Valor_3": 150, "Valor_4": 200}


dict_1.update(
    {"Valor_5": 250},
)

print(dict_1)

lista_valores = [["Valor_6", 300], ["Valor_7", 350]]
dict_1.update(lista_valores)

print(dict_1)


Total_soma_values = 0.0
for valores in dict_1.values():
    Total_soma_values = valores + valores

print(Total_soma_values)




