'''
Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta.
'''
from random import randint
from time import sleep
from itertools import count


def gera_sena(lista):
    for i in lista:
        yield i


n_jogo = int(input('Quantos jogos você quer gerar? '))

sena = []

for i in range(n_jogo):
    jogo = []
    while len(jogo) != 6:
        ran = randint(1, 60)
        if ran not in jogo:
            jogo.append(ran)
        else:
            continue
    sena.append(jogo)

s = gera_sena(sena)
c = count()
d = count()

while next(c) < n_jogo:
    print(f'Jogo {next(d) + 1}: {next(s)}')
    sleep(0.5)

# for n, jogo in enumerate(sena):
#     print(f'Jogo {n + 1}: {jogo}')
#     sleep(0.5)
