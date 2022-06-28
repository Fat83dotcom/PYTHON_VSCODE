'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer.
 Obs: Por padrão, a cada ano que nossa pessoa envelhece,
  sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''


class Pessoa:

    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, i):
        self.idade += i
        if self.idade < 21:
            self.altura += i * 0.5
        print(f'{self.nome} envelheceu {i} anos e agora tem { self.idade} anos')

    def engorda(self, g):
        self.peso += g
        print(f'{self.nome} engordou {g} kg e agora pesa {self.peso} kg.')

    def emagrecer(self, m):
        self.peso -= m
        print(f'{self.nome} emagreceu {m} kg e agora pesa {self.peso} kg.')

    def crescer(self, c):
        self.altura += c
        print(f'{self.nome} cresceu {c} cm e a altura atual é {self.altura} cm')


m = Pessoa('Maria', 1, 4, 40)
m.emagrecer(2)
m.crescer(5)
m.envelhecer(1)
m.crescer(0)
m.envelhecer(20)
m.engorda(40)
m.crescer(130)
