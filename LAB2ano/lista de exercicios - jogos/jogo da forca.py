import random
jogardnv = "S"
palavras = ["girassol", "montanha", "acucar", "relampago", "misterio", "flauta", "esquilo", "vagalume", "espantalho", "ladrilho"]
while jogardnv == "S":
    palavra = random.choice(palavras)
    caracteres = ["_" for _ in palavra]
    chute = []
    chances = 6
    print("jogo da forca! a palavra tem", caracteres)
    while "_" in caracteres:
        chute = input("Digite uma letra:")
        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    caracteres[i] = chute
            print("Letra correta!", caracteres)
        else:
            chances -= 1
            print("Letra incorreta!", chances)
    if "_" not in caracteres:
        print("Parabéns! Você descobriu a palavra:", palavra)
    elif chances == 0:
        print("Suas chances acabaram, voce perdeu! a palavra era:", palavra)
    jogar_dnv = input("Deseja jogar novamente? (S/N): ")