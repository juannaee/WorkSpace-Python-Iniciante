opcao_menu = input("Você deseja entrar? [Y]es ou [N]o")

senha_digitada = input("Certo! Digite sua senha!!")
senha_verificacao = '2711'

opcao_menu_y = opcao_menu == 'y' or opcao_menu == 'Y'
senha_verificada = senha_digitada == senha_verificacao

if opcao_menu_y and senha_verificada:
    print("Bem vindo ao sistema!!")

elif not opcao_menu_y or not senha_verificada:
    print("OPS! Você tem que escrever um valor valido")
    print(f"Log:  {opcao_menu_y=} ///// {senha_verificada=}   ")


elif not opcao_menu and not senha_digitada:
    print("OPS! Você não digitou nenhuma opção e nenhuma senha")
    print(f"Log:  {opcao_menu=} ///// {senha_digitada=}   ")
