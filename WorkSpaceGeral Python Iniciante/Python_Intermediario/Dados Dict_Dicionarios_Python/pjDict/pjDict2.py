perguntas = [
    {
        "Pergunta": "Quanto é 2+2 ?",
        "Opcoes": [1, 2, 3, 4],
        "Resposta Certa": 4,
    },
    {
        "Pergunta": "Quanto é 1+1 ?",
        "Opcoes": [1, 2, 3, 4],
        "Resposta Certa": 2,
    },
]

quantidade_acertos = 0
for pergunta in perguntas:
    print()
    print("Pergunta: ", pergunta["Pergunta"])

    opcoes = pergunta["Opcoes"]
    print("Escolha uma opção: ")
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)

    print()
    opcao = input("Digite sua opção: ")
    print()
    try:
        opcao = int(opcao)

    except ValueError:
        print("Você deve digitar um numero para escolhar uma das opções!!")
        print()
    if opcao == pergunta["Resposta Certa"]:
        print("Acertou!!")
        quantidade_acertos += 1
    else:
        print("Você errou")
    print("")
    print(f"Você acertou {quantidade_acertos} de {len(perguntas)} ")
