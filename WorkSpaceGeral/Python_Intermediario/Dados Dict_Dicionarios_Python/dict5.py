import os


"""Exemplo de como funciona um "Shallow Copy (Copia Rasa) """
os.system("cls")

c1 = {"v1": 1, "v2": 2}

# Nesse caso não estamos copiando o c1 para o c2 , estamos so apontando.
c2 = c1
# Por isso que se você mudar o c2, tambem muda o c1.
c2["v1"] = 100
print(c1)

c3 = {"v1": 1, "v2": 2}
# Ja nesse caso estamos copiando o c3 para o c4
c4 = c3.copy()

# Logo com isso podemos ver que alterando c4 não se altera no c3
c4["v1"] = 300
print(c3)
print(c4)

"""Esse tipo de copia so funciona para valores imutaveis!!
Se você tentar com valores mutaveis como lista tera o seguinte comportamento:"""


c5 = {"v1": 1, "v2": 2, "l1": [0, 1, 2]}

c6 = c5.copy()

# Percebemos que a lista é modificada nos dois dicionarios, pois é uma copia rasa.
c6["l1"][0] = 2
print(c5)
print(c6)


"""Porém para cotornamos isso podemos utilizar a importanção copy,
com isso podemos utilizando a função/metodo deepcopy, onde até valores mutaveis
como listas, podera ser manipulado, porque com o deepcopy 
todos os subsniveis do dicionario vai conseguir ser acessado!!"""

import copy

c7 = {"v1": 1, "v2": 2, "l1": [0, 1, 2]}
c8 = copy.deepcopy(c7)

c8["l1"][0] = 5
print(c7)
print(c8)
