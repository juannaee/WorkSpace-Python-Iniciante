

print("Escolha uma opção:\n1 - Entrar portal\n2 - Sair portal\n3 - Ajuda")
entrada = input('Digite um numero!')


try:
    numero = int(entrada)

    if numero == 1:
        print('Certo entrando no portal...............')
    elif numero == 2:
        print('Certo saindo do portal...............')
    elif numero == 3:
        print('Entrando na sessão ajuda.............')
    else:
        print('Você deve digitar uma das opções!!!!')


except:
    print('Você não digitou um numero!!!')
