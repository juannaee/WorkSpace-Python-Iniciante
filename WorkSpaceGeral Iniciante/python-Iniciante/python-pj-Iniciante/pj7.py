import os

letras_acertadas = ''
palavra_secreta = 'perfume'
numero_tentativas = 0
numero_max_tentaivas = 2 * len(palavra_secreta)

while True:

    numero_tentativas += 1

    if numero_tentativas <= numero_max_tentaivas:
        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Você pode apenas digitar apenas uma letra, tente novamente')
            continue
        if letra in palavra_secreta:
            letras_acertadas += letra

        palavra_formada = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print(palavra_formada)
        print(
            f'Numero de tentativas restantes: {numero_max_tentaivas - numero_tentativas} ')

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print(
                f'Parabens!!! Você ganhou, {palavra_secreta = }\n{numero_tentativas =}  ')
            letras_acertadas = ''
            numero_tentativas = 0
    else:
        print('Numero de tentativas esgotado, tente novamente')
        numero_tentativas = 0
        continue
