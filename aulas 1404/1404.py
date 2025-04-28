class animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("Som generico de animal")

class Cachorro(animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(animal):
    def emitir_som(self):
        print("Miau!")
        
meu_cachorro = Cachorro("Rex", 3)
meu_gato = Gato("Fushi", 2)
meu_cachorro.emitir_som()
meu_gato.emitir_som()