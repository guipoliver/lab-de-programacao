class Calculadora:
    def somar(self, a, b ,c=None):
        if c is None:
            return a + b
        else:
            return a + b + c 

calc = Calculadora()
print(calc.somar(2, 3))     #saída: 5
print(calc.somar(2, 3, 4))  #saída: 4