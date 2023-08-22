import os

os.system('cls')
while True:
    nome_aluno_str = input('Digite seu nome: ')
    if len(nome_aluno_str) == 0:
        print('Você deve digitar um nome!!!')
        continue
    idade_aluno_str = input('Digite sua idade: ')

    try:
        idade_aluno_int = int(idade_aluno_str)
        print(f'Bem vindo {nome_aluno_str}')
    except ValueError:
        print('Você deve digitar um numero inteiro para sua idade!')
        continue

    print(
        f'Confirme sua idade! Você tem: {idade_aluno_int} anos ?\n1 - Sim\n2 - Não ')
    opcao_menu_str = input()

    try:
        opcao_menu_int = int(opcao_menu_str)

        match opcao_menu_int:
            case 1:
                print('Certo! Continuando...............................\n')
            case 2:
                print('Certo digite novamente os dados!')
                continue
            case _:
                print('Você deve escolher uma das opções!!!')

    except ValueError:
        print('Você digitar um numero inteiro para escolher uma opção!')

    

