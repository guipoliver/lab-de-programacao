import random
A = int
X = int 
B = int = 0
X = random.randint(1, 100)
print("Você consegue acertar o numero de 0 a 100 com quantas tentativas?")
while (True):
    A = int = input("qual numero você acha que é? ")
    B += 1
    if str(A) > str(X):
        print("Você digitou um valor muito alto!")
    if str(A) < str(X):
        print("Você digitou um valor muito baixo!")
    if str(A) == str(X):
        print("Parabens voce acertou! Utilizou", B ,"tentativas")
        break