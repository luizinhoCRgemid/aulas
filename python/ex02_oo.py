
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco * (1 - percentual / 100)

produto = Produto("Notebook", 100.0)

print(produto.desconto(10))

