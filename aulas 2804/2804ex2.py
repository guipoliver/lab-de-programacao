class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial #convenção para atributo "protegido"

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Deposito de {valor} Realizado. Saldo atual: {self._saldo}")
        else:
            print(f"Valor de depósito inválido")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self._saldo}")
        else:
            print(f"Saldo insuficiente ou valor de saque inválido.")

    def get_saldo(self):
        return self._saldo

minha_conta = ContaBancaria(1000)

print(f"Saldo inicial: {minha_conta.get_saldo()}")

minha_conta.depositar(500)
minha_conta.sacar(200)