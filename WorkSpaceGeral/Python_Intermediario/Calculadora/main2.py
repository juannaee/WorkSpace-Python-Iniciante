import os

resultado = 0
os.system("cls")


def sum(value_1, value_2):
    return float(value_1) + float(value_2)


def subtrahend(value_1, value_2):
    if float(value_1) < float(value_2):
        return float(value_2) - float(value_1)

    else:
        return float(value_1) - float(value_2)


def multiplicacao(value_1, value_2):
    return float(value_1) * float(value_2)


def divisao(value_1, value_2):
    return float(value_2) / float(value_1)


while True:
    print("Escolha uma opção do menu:")
    print("1 - Entrar na calculadora\n2 - Sair")
    print("")
    opcao_menu = input("Digite uma das opções:")
    print("")
    try:
        opcao_menu = int(opcao_menu)
    except ValueError:
        print("Opção inválida! Você deve digitar um numero para escolher uma opção!!")
        continue

    if opcao_menu == 1:
        while True:
            print("")
            print("Entrar calculadora.....")
            print("")
            print("Escolha uma das opções: ")
            print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
            opcao_calculadora = input("Digite uma das opção:")
            print("")

            try:
                opcao_calculadora = int(opcao_calculadora)
            except ValueError:
                print(
                    "Opção inválida! Você deve digitar um numero para escolher uma opção!!"
                )
                continue

            valor_1 = input("Entrar com o primeiro valor:")
            valor_2 = input("Entrar com o segundo valor:")

            try:
                valor_1 = float(valor_1)
                valor_2 = float(valor_2)
            except ValueError:
                print("Você deve digitar uma numero para realizar a operação!")
                continue

            if opcao_calculadora == 1:
                resultado = sum(valor_1, valor_2)
                print(resultado)

            elif opcao_calculadora == 2:
                resultado = subtrahend(valor_1, valor_2)
                print(resultado)

            elif opcao_calculadora == 3:
                resultado = multiplicacao(valor_1, valor_2)
                print(resultado)

            elif opcao_calculadora == 4:
                resultado = divisao(valor_1, valor_2)
                print(resultado)

            elif opcao_calculadora == 5:
                print("Certo! Saindo......")
                break

            else:
                print("Opção inválida, escolha uma das opções!!!!!!!")
    elif opcao_menu == 2:
        print("Saindo....")
        break
    else:
        print("Opção inválida, escolha uma das opções!!!!!!!")
        continue
