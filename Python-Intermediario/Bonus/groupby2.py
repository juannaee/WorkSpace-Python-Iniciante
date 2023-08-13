from itertools import groupby
import pprint

alunos = [
    {"Nome": "Juan", "Nota": "A"},
    {"Nome": "Paula", "Nota": "B"},
    {"Nome": "Joao", "Nota": "C"},
    {"Nome": "Jonas", "Nota": "A"},
    {"Nome": "Julia", "Nota": "A"},
    {"Nome": "Ben", "Nota": "A"},
    {"Nome": "Savio", "Nota": "B"},
    {"Nome": "Bianca", "Nota": "B"},
    {"Nome": "Xico", "Nota": "C"},
    {"Nome": "Lucas", "Nota": "C"},
]


def p(x):
    return pprint.pprint(list(x))


def ordena_por_notas(aluno):
    return aluno["Nota"]


grupo_alunos_ordenados = sorted(alunos, key=ordena_por_notas)
grupos_de_alunos = groupby(grupo_alunos_ordenados, key=ordena_por_notas)

for i, grupo in grupos_de_alunos:
    print(f"Alunos com a nota: {i}")
    p(grupo)
