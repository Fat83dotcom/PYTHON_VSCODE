'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
 rodapés necessárias para o local.
 '''


class Retangulo:
    def __init__(self, ladoA, ladoB, ) -> None:
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, A, B):
        self.ladoA = A
        self.ladoB = B

    def retornaLados(self):
        return self.ladoA, self.ladoB

    def area(self):
        return self.ladoA * self.ladoB

    def perimetro(self):
        return (2 * self.ladoA) + (2 * self.ladoB)


chaoA = float(input('Digite a medida de um lado da area a ser ladrilhada: '))
chaoB = float(input('Digite a medida do outro lado da area: '))
pisoA = float(input('Digite a madida de um lado do piso: '))
pisoB = float(input('Digite a outra medida do piso: '))
chao = Retangulo(chaoA, chaoB)
piso = Retangulo(pisoA, pisoB)
qtdPiso = chao.area() / piso.area()
rodaPe = chao.perimetro()
print(f'Seram necessários {round(qtdPiso, 2)} pisos para cobrir a área.')
print(f'Seram necessários {round(rodaPe, 2)} metros de rodapé para ornar a área')
