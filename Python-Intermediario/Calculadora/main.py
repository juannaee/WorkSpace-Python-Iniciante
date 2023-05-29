import os
resultado = 0
os.system('cls')


def sum(value_1, value_2):
    valor_1 = float(value_1)
    valor_2 = float(value_2)
    return valor_1 + valor_2


def subtrahend(value_1, value_2):
    valor_1 = float(value_1)
    valor_2 = float(value_2)
    resultado = 0

    if valor_1 < valor_2:
        resultado = valor_2 - valor_1
    else:
        resultado = valor_1 - valor_2

    return resultado


def multiplicacao(value_1, value_2):
    valor_1 = float(value_1)
    valor_2 = float(value_2)
    return valor_1 * valor_2


def divisao(value_1, value_2):
    valor_1 = float(value_1)
    valor_2 = float(value_2)
    return valor_1 / valor_2


while True:
    print('Escolha uma opção do menu:')
    print('1 - Entrar na calculadora\n2 - Sair')
    print('')
    opcao_menu = input('Digite uma das opções:')
    print('')
    try:
        opcao_menu = int(opcao_menu)
    except ValueError:
        print('Opção inválida! Você deve digitar um numero para escolher uma opção!!')
        continue
    match opcao_menu:
        case 1:
            while True:
                print('')
                print('Entrar calculadora.....')
                print('')
                print('Escolha uma das opções: ')
                print(
                    '1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair')
                opcao_calculadora = input('Digite uma das opção:')
                print('')
                try:
                    opcao_calculadora = int(opcao_calculadora)
                except ValueError:
                    print(
                        'Opção inválida! Você deve digitar um numero para escolher uma opção!!')
                    continue
                valor_1 = input('Entrar com o primeiro valor:')
                valor_2 = input('Entrar com o segundo valor:')
                try:
                    valor_1 = float(valor_1)
                    valor_2 = float(valor_2)
                except ValueError:
                    print('Você deve digitar uma numero para realizar a operação!')
                    continue
                match opcao_calculadora:
                    case 1:
                        resultado = sum(valor_1, valor_2)
                        print(resultado)
                    case 2:
                        resultado = subtrahend(valor_1, valor_2)
                        print(resultado)
                    case 3:
                        resultado = multiplicacao(valor_1, valor_2)
                        print(resultado)
                    case 4:
                        resultado = divisao(valor_1, valor_2)
                        print(resultado)
                    case 5:
                        print('Certo!, saindo......')
                        break
                    case _:
                        print('Opção Invalida, escolha uma das opções!!!!!!!')
        case 2:
            print('Sair....')
            break
        case _:
            print('Opção Invalida, escolha uma das opções!!!!!!!')
            continue
