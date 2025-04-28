#crie uma superclasse chamada funcionario com os atributos nome, salario base e metodo calcular salario

#crie uma subclasse chamada gerente com o atributo bonus

#crie uma subclasse chamada vendedor com atributo comissao e vendas

#crie uma subclasse chamada desenvolvedor com atributos nivel e experiencia

#IMPLEMENTE O METODO CALCULAR SALARIO DE FORM diferente em cada subclasse considerando seus atributos especificos

class funcionarios:
    def __init__(self, nome, salariobase):
        self.nome = nome
        self.salariobase = salariobase

    def calcsalario(self):
        print("teste")

class gerente(funcionarios):
    def __init__(self, nome, salariobase, bonus):
        self.nome = nome
        self.salariobase = salariobase
        self.bonus = bonus
    def calcsalario(self):
        print("gerente", self.salariobase + self.bonus)
        
class vendedor(funcionarios):
    def __init__(self, nome, salariobase, comissao, vendas):
        self.nome = nome
        self.salariobase = salariobase
        self.comissao = comissao
        self.vendas = vendas
    def calcsalario(self):
        print("vendedor", self.salariobase + self.comissao + self.vendas)

class desenvolvedor(funcionarios):
    def __init__(self, nome, salariobase, nivel, experiencia):
        self.nome = nome
        self.salariobase = salariobase
        self.nivel = nivel
        self.experiencia = experiencia
    def calcsalario(self):
        print("desenvolvedor", self.salariobase * self.nivel * self.experiencia)
    
gerente = gerente("Jorge", 1000, 500)
vendedor = vendedor("Robson", 1000, 1000, 1000)
desenvolvedor = desenvolvedor("Mario",1000, 10, 8)

gerente.calcsalario()
vendedor.calcsalario()
desenvolvedor.calcsalario()