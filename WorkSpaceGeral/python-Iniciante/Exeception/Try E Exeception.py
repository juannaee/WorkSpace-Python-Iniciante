'''

numero = input('Digite um numero para dobrar: ')


try:
    numero_int = float(numero)
    print(f'Seu numero: {numero_int} dobrado é: {numero_int * 2}')

except:
    print('ERRO: Digite um numero!!')

    
'''
