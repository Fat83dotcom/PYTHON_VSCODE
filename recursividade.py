'''
n! = n*(n-1)*(n-2)*...*1
'''
import sys
sys.setrecursionlimit(1000000)


def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


def fibbonaci(posicaoNumero):
    if posicaoNumero == 0:
        return posicaoNumero
    if posicaoNumero == 1:
        return posicaoNumero
    else:
        return fibbonaci(posicaoNumero - 1) + fibbonaci(posicaoNumero - 2)


print(fatorial(10000))
# print(fibbonaci(2222226))
