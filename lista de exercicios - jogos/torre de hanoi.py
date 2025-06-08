torre1 = [3, 2, 1]
torre2 = []
torre3 = []
lista_vazia = []
disco = []
print("Seja Bem vindo a Torre de Hanoi, aqui possuimos tres torres e tres discos, seu objetivo é passar os 3 discos para outra torre, mas voce nao pode sobrepor um disco menor por um maior")
print(torre1, torre2, torre3)
jogardnv = "S"
while jogardnv == "S":
    mover = int(input("voce deseja mover o disco de qual torre? (1, 2 ou 3)"))
    if mover == 1 and torre1 == lista_vazia:
        print("Essa torre não possui nenhum disco!")
        continue
    if mover == 2 and torre2 == lista_vazia:
        print("Essa torre não possui nenhum disco!")
        continue
    if mover == 3 and torre3 == lista_vazia:
        print("Essa torre não possui nenhum disco!")
        continue
    if mover < 1 or mover > 3:
        print("insira um valor de 1 a 3!")
        continue
    if mover == 1:
        disco = torre1.pop()
    if mover == 2:
        disco = torre2.pop()
    if mover == 3:
        disco = torre3.pop()
    final = int(input("para qual torre? (1, 2 ou 3)"))
    if final == 1 and torre1 and disco > torre1[-1]:
        print("A torre 1 tem um disco menor no topo!")
        continue
    if final == 2 and torre2 and disco > torre2[-1]:
        print("A torre 2 tem um disco menor no topo!")
        continue
    if final == 3 and torre3 and disco > torre3[-1]:
        print("A torre 3 tem um disco menor no topo!")
        continue
    if mover == final:
        print("voce nao pode mover um disco de uma torre para essa mesma torre!")
        continue
    if final == 1:
        disco = torre1.append(disco)
    if final == 2:
        disco = torre2.append(disco)
    if final == 3:
        disco = torre3.append(disco)
    if final < 1 or final > 3:
        print("insira um valor de 1 a 3!")
        continue
    print(torre1, torre2, torre3)
    if torre2 == [3, 2, 1] or torre3 == [3, 2, 1]:
        print("Parabens voce ganhou!!")
        jogardnv = input("Voce deseja jogar denovo? (S/N)")