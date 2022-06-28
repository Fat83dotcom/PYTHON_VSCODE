from itertools import count
# from random import randint
# gra_de = []
# linhas = []

# for li in range(2):
#     for col in range(8):
#         linhas.append(randint(0, 1))
#     gra_de.append(linhas[:])
#     linhas.clear()

# for lis in gra_de:
#     print(lis)


class Leituras:
    def __init__(self, grade):
        self.grade = grade

    @staticmethod
    def gera_palavra(palavras):
        for p in palavras:
            yield p

    def verfica_horizontal(self, palavra):
        for linha in self.grade:
            for letra in linha:
                for letra_l in palavra:
                    pass


linhas = 0
while linhas <= 2:
    linhas = int(input('L = '))
colunas = 100
while colunas >= 100 or colunas <= 0:
    colunas = int(input('C = '))

rec_linha = ''
grade = []
linha = []
cont = count()

while next(cont) < linhas:
    rec_linha = input('').strip()
    if len(rec_linha) == colunas + (colunas - 1):
        for letra in rec_linha:
            if letra != ' ':
                linha.append(letra)
        grade.append(linha[:])
        linha.clear()
    else:
        print('A quantidade de letras digitadas não corresponde ao',
            'número digitado de colunas, por favor, insira novamente.')
        rec_linha = ''
        continue

n_palavras = 10
while n_palavras >= 10 or n_palavras == 0:
    n_palavras = int(input('P = '))

palavras = [input(f'P.{i + 1} = ') for i in range(n_palavras)]

leitu = Leituras(grade)
leitu.verfica_horizontal(palavras)

# print(grade, palavras)
