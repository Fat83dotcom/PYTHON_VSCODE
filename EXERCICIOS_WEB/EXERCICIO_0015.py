'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''


class Quadrado:
    def __init__(self, lado) -> None:
        self.lado = lado

    def mudarValorLado(self, novo_valor):
        self.lado = novo_valor

    def retornaValorLado(self):
        print(f'Novo valor do lado: {self.lado}')

    def area(self):
        return self.lado ** 2


q1 = Quadrado(13)
print(f'A area deste quadrado é {q1.area()} m².')
q1.mudarValorLado(12)
q1.retornaValorLado()
print(f'Area: {q1.area()}')
