

while True:

    numero_1 = input('Digite o primeiro valor: ')
    numero_2 = input('Digite o segundo valor:  ')
    resultado = 0
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0


### Conversão dos valores str para float ###
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

        operador = int(
            input('Escolha um operador:\n1 = +\n2 = x\n3 = /\n4 = -\n'))

        match operador:
            case 1:
                resultado = numero_1_float + numero_2_float
                print(f'{numero_1_float} + {numero_2_float} = {resultado}')
            case 2:
                resultado = numero_1_float * numero_2_float
                print(f'{numero_1_float} x {numero_2_float} = {resultado}')
            case 3:
                resultado = numero_1_float / numero_2_float
                print(f'{numero_1_float} / {numero_2_float} = {resultado}')
            case 4:
                resultado = numero_1_float - numero_2_float
                print(f'{numero_1_float} - {numero_2_float} = {resultado}')

### Caso default ###
            case _:
                print('Você deve digitar uma das opções!!!')
                continue

### Tratamente de execeção ###

    except:
        numeros_validos = None

        if numeros_validos is None:
            print('Um dos numeros ou ambos digitados são invalidos, digite novamante!! ')
            continue


### Opção de sair ###
    sair = input('Você quer sair [s]: ').lower().startswith('s')
    if sair is True:
        break
    else:
        continue
