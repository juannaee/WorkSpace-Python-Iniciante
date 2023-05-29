condicao = False

passou_no_if = None


if condicao:
    passou_no_if = True
else:
    passou_no_if = None


if passou_no_if is None:
    print('o teste não passou,caiu no else')

if passou_no_if is not None:
    print('O teste passou , foi true')
