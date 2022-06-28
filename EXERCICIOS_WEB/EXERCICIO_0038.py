'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar
em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar
esta informação por que ela pode ser calculada a qualquer momento.
'''
from time import sleep
from itertools import count


class Tamagushi():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def set_nome(self):
        self.nome = input('Qual o novo nome do seu bichinho? ')

    def set_fome(self, fome):
        self.fome += fome

    def set_saude(self, saude):
        self.saude += saude

    def set_idade(self, idade):
        self.idade += idade

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def alimentar(self):
        if self.get_fome() == 0:
            print(f'Seu Tamaguishi {self.nome} está morto. Fim de Jogo.')
            return False
        if self.get_fome() < 20:
            print(f'Seu Tamagushi {self.nome} está com fome.')
            self.set_fome(int(input('Dar alimento: ')))
        if 21 < self.get_fome() < 50:
            print(f'Seu Tamagushi {self.nome} pode comer.')
            self.set_fome(int(input('Dar alimeto: ')))
        if 51 < self.get_fome() <= 100:
            print(f'Seu Tamagushi {self.nome} não precisa comer.')
            self.set_fome(int(input('Dar alimento: ')))
        if self.get_fome() > 100:
            print(f'Seu Tamagushi {self.nome} não precisa comer.')
            self.set_fome(int(input('Dar alimento: ')))
        return True

    def humor(self):
        pass


t1 = Tamagushi('zezinho', 100, 100, 0)
flag = True
c = count(-1)
contador = next(c)
while flag:
    if contador == 59:
        print('passou aqui')
        c = count(0)
    contador = next(c)
    print(contador)
    sleep(1)
