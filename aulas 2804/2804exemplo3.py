from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.largura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        import math
        return 2 * math.pi * self.raio
        
    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.raio
    
ret = Retangulo(5, 10)
cir = Circulo(7)

print(f"Àrea do Retangulo: {ret.calcular_area()}")
print(f"Perímetro do círculo: {cir.calcular_perimetro()}")