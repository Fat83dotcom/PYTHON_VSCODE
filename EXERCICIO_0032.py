'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras
lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.
'''
from random import randint

with open('exercicio_0032.txt', 'r') as arquivo:
    palavras = [palavra for palavra in arquivo.readlines()]
    n = randint(0, len(palavras))
    palavra_chave = palavras[n].upper()[:-1]
    cont = 6
    armazena_letra = []
    while cont > 0:
        letra = input('Digite uma letra: ').upper()
        if letra in palavra_chave:
            armazena_letra.append(letra)
            n = 0
            for le in palavra_chave:
                if le in armazena_letra:
                    print(le, end='')
                    n += 1
                    if n == len(palavra_chave):
                        print('\n')
                        print('Parabéns você ganhou!!')
                        break
                else:
                    print('_', end='')
            if n == len(palavra_chave):
                break
            n = 0
            print('\n')
        else:
            cont -= 1
            print(f'Você errou, ainda tem {cont} tentativas.')
            if cont == 0:
                print('Você perdeu !!!')
                break
