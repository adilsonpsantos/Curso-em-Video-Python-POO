class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True

c1 = ContaBancaria(112, "Gustavo", 3000)
c1.depositar(500)
valor = 510

if not c1.sacar(valor):
    print(f"Saque de R$ {valor:,.2f} não autorizado. Saldo atual é de R$ {c1.saldo:,.2f}")
else:
    print(f"Saque de R$ {valor:,.2f} autorizado")
print(c1)
