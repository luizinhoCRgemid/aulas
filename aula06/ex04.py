class Pagamento:
    def processar(self, valor):
        return valor


class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95  # 5% de desconto


class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02  # 2% de juros


class Pix(Pagamento):
    def processar(self, valor):
        return valor


pagamentos = [Dinheiro(), Cartao(), Pix()]

for pagamento in pagamentos:
    print(f"Valor final: R${pagamento.processar(100):.2f}")
