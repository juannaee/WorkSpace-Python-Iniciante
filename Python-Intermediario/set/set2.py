s1 = {1, 2, 3}
s2 = {3, 4, 5}
# Junta os 2 Sets
s3 = s1.union(s2)
print(s3)
# Pega os valores iguais nos dois sets
s3 = s1.intersection(s2)
print(s3)
# Pegando a diferença do set da esquerda comparado ao da direita
s3 = s1.difference(s2)
print(s3)
s3 = s2.difference(s1)
print(s3)
# Pegando itens que não estão repetidos nos 2
s3 = s1.symmetric_difference(s2)
print(s3)
