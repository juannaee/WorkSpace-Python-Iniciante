quantidade_de_linhas = 5
quantidade_de_colunas = 5
quantidade_de_testes = 5


linha = 0
while linha <= quantidade_de_linhas:
    coluna = 0
    while coluna <= quantidade_de_colunas:
        coluna += 1
        teste = 0
        while teste <= quantidade_de_testes:
            teste += 1
            print(f'{linha=},{coluna=},{teste=}')
    linha += 1
