#crie uma classe chamada produto com os seguintes atributos: nome, preço e quantidade. 
#e os metodos: calcular valor total, que retorna o preço vezeds a quantidade de produtos
#metodo: nova quantidade de produtos atualiza a quantidade de produtos no atributo quan6tidade
#objtv final crie alguns objts do tipo produto calculeseus valores totais e atualizade a qntd de cada um deles 

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade

    def nova_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

produto1 = Produto("Camiseta", 49.90, 10)
produto2 = Produto("Calça Jeans", 129.90, 5)
produto3 = Produto("Tênis", 199.90, 3)

print(f"Valor total do {produto1.nome}: R${produto1.calcular_valor_total():.2f}")
print(f"Valor total do {produto2.nome}: R${produto2.calcular_valor_total():.2f}")
print(f"Valor total do {produto3.nome}: R${produto3.calcular_valor_total():.2f}")

produto1.nova_quantidade(15)
produto2.nova_quantidade(10)
produto3.nova_quantidade(6)

print("\nApós atualizar as quantidades:")
print(f"Valor total do {produto1.nome}: R${produto1.calcular_valor_total():.2f}")
print(f"Valor total do {produto2.nome}: R${produto2.calcular_valor_total():.2f}")
print(f"Valor total do {produto3.nome}: R${produto3.calcular_valor_total():.2f}")
