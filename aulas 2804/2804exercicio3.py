#criar ujm carrinho de comprtas com a classe: carrinho de compras produto
#add produtos no carrinho, retirar, mostrar o valor total do produto

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                break

    def mostrar_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco:.2f}")

p1 = Produto("Livro", 45.90)
p2 = Produto("Caneta", 3.50)
p3 = Produto("Mochila", 120.00)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

print("Produtos no carrinho:")
carrinho.listar_produtos()

print("\nTotal: R$", carrinho.mostrar_total())

carrinho.remover_produto("Caneta")

print("\nProdutos no carrinho após remover 'Caneta':")
carrinho.listar_produtos()

print("\nTotal atualizado: R$", carrinho.mostrar_total())
