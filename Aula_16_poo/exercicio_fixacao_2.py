#2) Crie uma classe chamada Conta para simular as operações de
# uma conta corrente. Sua classe deverá ter os atributos Titular e
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
# Conta e teste os atributos e métodos implementados.

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self, quantidade_sacar):
        self.quantidade_sacar = quantidade_sacar
        if self.saldo < quantidade_sacar:
            return f"Não é possível sacar R${self.quantidade_sacar} pois o saldo é {self.saldo}"
        else:
            self.saldo -= self.quantidade_sacar
            return f"Saque de R${self.quantidade_sacar} foi sacado com sucesso!\nTotal: {self.saldo}\n"
    
    def depositar(self, quantidade_deposito):
        self.quantidade_deposito = quantidade_deposito
        self.saldo += self.quantidade_deposito
        return f"Depositou R${self.quantidade_deposito} reais!\nSaldo atual: {self.saldo}"


titular_conta = Conta("João", 1500.0)

print(titular_conta.sacar(100))
print(titular_conta.depositar(500))