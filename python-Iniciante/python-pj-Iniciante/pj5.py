nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é muito pequeno!')
    elif tamanho_nome == 6:
        print('Seu nome tem um tamanho adquado!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Você deve digitar um nome com mais de uma letra!')
