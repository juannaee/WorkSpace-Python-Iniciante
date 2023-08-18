import decimal
import os

os.system('cls')
# Mostrando como funciona a imprecisão
valor_1 = 0.1
valor_2 = 0.7
valor_total = valor_1 + valor_2
print(valor_total)

# ******************************************************************#
# ******************************************************************#

# Resolvendo imprecisão com formatação de string
valor_1 = 0.1
valor_2 = 0.7
valor_total = valor_1 + valor_2
print(f'{valor_total:.2f}')

# ******************************************************************#
# ******************************************************************#

# Resolvendo imprecisão com função que retorna um valor float
valor_1 = 0.1
valor_2 = 0.7
valor_total = valor_1 + valor_2
print(round(valor_total, 2))


# ******************************************************************#
# ******************************************************************#

# Resolvendo imprecisão com classe/objeto que faz converção de string para float
valor_1 = decimal.Decimal('0.1')
valor_2 = decimal.Decimal('0.7')
valor_total = valor_1 + valor_2
print(type(valor_total))
print(valor_total)
