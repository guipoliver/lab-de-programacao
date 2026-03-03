import random
A = 0
B = 0
jogar_dnv = "S"
lista = ["pedra", "papel", "tesoura"]
print("Bem vindo ao pedra papel e tesoura contra o computador!")
while jogar_dnv == "S":
    esc_comp = random.choices(lista)
    esc_jogador = input("Qual vai ser a sua escolha entre pedra papel e tesoura? ")
    if esc_comp == ["pedra"]:
        print("a maquina escolheu pedra")
        if esc_jogador == "pedra":
            print("empate")
        if esc_jogador == "papel":
            A += 1
            print("Voce ganhou")
        if esc_jogador == "tesoura":
            B += 1
            print("Voce perdeu")
    if esc_comp == ["papel"]:
        print("a maquina escolheu papel")
        if esc_jogador == "pedra":
            B += 1
            print("Voce perdeu")
        if esc_jogador == "papel":
            print("empate")
        if esc_jogador == "tesoura":
            A += 1
            print("Voce ganhou")
    if esc_comp == ["tesoura"]:
        print("a maquina escolheu tesoura")
        if esc_jogador == "pedra":
            A += 1
            print("voce ganhou")
        if esc_jogador == "papel":
            B += 1
            print("Voce perdeu")
        if esc_jogador == "tesoura":
            print("empate")
    print("O jogo acabou, e o placar está", A, "para você e", B, "para a maquina")
    jogar_dnv = input("Deseja jogar denovo? S/N")
    if jogar_dnv == "N":
        break