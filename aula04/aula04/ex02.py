lass Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Erro: nome não pode ser vazio")

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Erro: idade inválida")

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")


pessoa = Pessoa("Ana", 18)

pessoa.apresentar()
pessoa.set_idade(150)
pessoa.set_nome("")
