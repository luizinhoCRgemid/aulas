class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: preço não pode ser negativo")


produto = Produto("Notebook", 3500)

print(produto.get_nome())
print(produto.get_preco())

produto.set_preco(-100)
produto.set_preco(3000)

print(produto.get_preco())
