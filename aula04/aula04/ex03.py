class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo: R${self.__saldo:.2f}")


conta = ContaBancaria("Luiz Gustavo")

conta.depositar(1000)
conta.sacar(300)

print(conta.get_saldo())
conta.extrato()
