
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 80.00)

print(produto1.nome, "-", produto1.preco)
print(produto2.nome, "-", produto2.preco)

