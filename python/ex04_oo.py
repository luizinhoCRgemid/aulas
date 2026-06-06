lass ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")

conta = ContaBancaria("Luiz Gustavo", 1000)

conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)

conta.extrato()

