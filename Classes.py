'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        return self.cor

    def mostraCor(self):
        print(self.cor)

    def mostraBola(self):
        print(f'Sua bola é {self.cor}, de {self.circunferencia} cm de circunferência e feita de {self.material}.')


b = Bola('azul', 30, 'couro')
c = Bola('amarela', 23, 'plastico')
b.mostraBola()
b.trocaCor('branca')
b.mostraCor()
b.mostraBola()
c.mostraCor()
c.mostraBola()
