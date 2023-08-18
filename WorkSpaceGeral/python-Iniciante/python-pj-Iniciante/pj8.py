import os
lista = []

while True:

    print('Escolha uma das opções: ')

    try:
        menuOpcao = int(input(
            '1 - Inserir um Item\n2 - Apagar um Item\n3 - Vizualizar Itens\n4 - Sair '))
        print('------------------------------------------------')

        match menuOpcao:
            case 1:
                novo_item = input('Digite um item: ')
                print(f'***Item Digitado*** = {novo_item}')
                print('------------------------------------------------')
                if len(novo_item) == 0:
                    print('------------------------------------------------')
                    print('*****Você deve digitar um item*****')
                    print('------------------------------------------------')
                else:
                    lista.append(novo_item)

            case 2:

                print('Qual item você deseja apagar?\nItens disponiveis: ')
                print('------------------------------------------------')
                for i, item in enumerate(lista):
                    print(i, item)
                print('------------------------------------------------')
                try:
                    indicie_para_apagar = int(
                        input('Digite um dos indicies: '))
                    del lista[indicie_para_apagar]

                except ValueError:
                    os.system('cls')
                    print(
                        'Você deve digitar um numero para escolher um dos indicies!!')
                except IndexError:
                    os.system('cls')
                    print('O indicie escolhido não existe!')
            case 3:
                print('Certo!! Mostrando lista...................')
                if len(lista) == 0:
                    print('A lista é vazia!! Não a nada para mostrar!!')
                else:
                    for item in lista:
                        print(item)
                print('------------------------------------------------')

    except ValueError:
        os.system('cls')
        print('Você deve digitar um numero para escolher uma opção!!')
    except Exception:
        os.system('cls')
        print('Error desconhecido')
