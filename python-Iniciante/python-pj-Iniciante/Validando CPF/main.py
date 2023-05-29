import os
import random

os.system('cls')

cpf_enviado = ''

for i in range(9):
    cpf_enviado += str(random.randint(0, 9))


digitos_9_cpf = cpf_enviado[:9]
contador_primeiro_digito = 10

resultado_digito_1 = 0

for digito in digitos_9_cpf:
    resultado_digito_1 += int(digito) * contador_primeiro_digito
    contador_primeiro_digito -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


digitos_10_cpf = digitos_9_cpf + str(digito_1)
contador_segundo_digito = 11

resultado_digito_2 = 0

for digito in digitos_10_cpf:
    resultado_digito_2 += int(digito) * contador_segundo_digito
    contador_segundo_digito -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f"{digitos_9_cpf}{digito_1}{digito_2}"
print(f'{cpf_gerado}')
