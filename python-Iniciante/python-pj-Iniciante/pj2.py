opcao_menu = input("Escolha uma opção: [E]ntrar [S]sair")

senha_digitada = input("Digite sua senha: ")

senha_permitida = "2711"

if opcao_menu == "E" and senha_digitada == senha_permitida:
    print("Certo! entrando............")
else:
    print("saindo............")
