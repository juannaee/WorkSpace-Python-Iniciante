pessoa = {
    "nome": "Pedro",
    "idade": 25,
    "sexo": "M",
    "peso": 85.5,
    "altura": 1.70,
    "endereco": [
        {
            "Cidade": "Paulista",
            "Municipio": "Maranguape 1",
            "Rua": 84,
            "Bloco": 3,
            "Apartamemento": 306,
        }
    ],
}


for dados in pessoa:
    print(dados, ": ", pessoa[dados])

print(pessoa["nome"])
print(pessoa["sexo"])

