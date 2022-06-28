'''
Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos
são obrigatórios.
'''


class ContaCorrente:
    def __init__(self, n_conta, nome, saldo=0):
        self.n_conta = n_conta
        self.nome = nome
        self.saldo = saldo

    def altera_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O nome do titular da conta {self.n_conta} foi alterado para {self.nome}')

    def deposito(self, valor):
        saldo_anterior = self.saldo
        print(f'Saldo anterior: R${saldo_anterior}')
        self.saldo = float(valor) + float(self.saldo)
        print(f'O valor depositado foi de R${valor} saldo atual é {self.saldo}')

    def saque(self, valor):
        if float(valor) > float(self.saldo):
            print(f'Saldo insuficiente.Seu saldo é {self.saldo}')
        else:
            self.saldo = float(self.saldo) - float(valor)
            print(f'{self.nome} sacou R${valor} e seu novo saldo é R${self.saldo}')


f = ContaCorrente(304, 'Fernando')
f.deposito(100)
f.saque(50)
f.deposito(400)
f.saque(450)
f.deposito(10999)
