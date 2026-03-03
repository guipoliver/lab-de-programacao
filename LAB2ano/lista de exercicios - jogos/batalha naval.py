import random
tabuleiro = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]
jogardnv = "S"
while jogardnv == "S":
    linha1 = random.choice(tabuleiro) 
    linha2 = random.choice(tabuleiro) 
    linha3 = random.choice(tabuleiro) 
    navio1 = random.choice(linha1)
    navio2 = random.choice(linha2)
    navio3 = random.choice(linha3)
    navio1 = [navio1, navio1 + 1, navio1 + 2, navio1 + 3]
    navio2 = [navio2, navio2 + 1, navio2 + 2]
    navio3 = [navio3, navio3 + 1]
    print (navio1, navio2, navio3)
    print("Bem vindo ao batalha naval contra o computador! em um tabuleiro 10x10 estão 3 navios escondidos, advinhe onde eles estão dando numero da linha e coluna")
    mar = 0
    while mar < 10:
        print("~ " * 10)
        mar += 1
    comeca = "S"
    navios = 9
    while comeca == "S":
        linha = int(input("Onde voce acha que estao os navios? digite um valor para a linha"))
        coluna = int(input("Agora digite um valor para a coluna"))
        chute = tabuleiro[linha - 1][coluna - 1]
        print(chute)
        if chute in navio1 or chute in navio2 or chute in navio3:
            print("voce acertou um navio!")
            navios -= 1
        else:
            print("voce acertou o mar!")
        if navios == 0:
            print("Voce ganhou!!!")
            jogardnv = input("deseja jogar dnv? (S/N)")
            if jogardnv == "N":
                    break   