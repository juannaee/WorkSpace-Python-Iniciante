import os
import re
import sys
os.system('cls')

# 94062615029
# cpf_enviado = '134.632.450-60'.replace('.', '').replace('-', '')
# print(cpf_enviado)

entrada_cpf = input("CPF: ")
cpf_enviado = re.sub(r'[^0-9]', '', entrada_cpf)

# string_qualquer = 'A'
# string_repetida = string_qualquer * 10
# print(string_repetida)

cpf_e_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
if cpf_e_sequencial:
    print('Você digitou valores repetidos!!')
    sys.exit()

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

if cpf_gerado == cpf_enviado:
    print('CPF VALIDO!')
    print(f'CPF ENVIADO:  {cpf_enviado} \nCPF GERADO: {cpf_gerado}')

else:
    print('CPF INVALIDO!!')
    print(f'CPF ENVIADO:  {cpf_enviado} \nCPF GERADO: {cpf_gerado}')
