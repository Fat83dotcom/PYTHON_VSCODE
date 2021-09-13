'''
Faça um programa que mostre N números primos
'''
import time
from ConvertSec import ConvertSec

def data():
    data = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
    return data


def gennum():
    cont = 1
    div = 0
    prim = 0
    while 1:
        for i in range(cont):
            if cont > 11 and (cont % 2 == 0 or cont % 3 == 0 or cont % 5 == 0 or cont % 7 == 0 or cont % 11 == 0):
                break    
            if cont % (i + 1) == 0:
                div += 1
        if div == 2:
            prim = cont
            yield prim
        cont += 1
        div = 0


num = input('Digite um número: ')
num = int(num)

n = gennum()

with open(f'/home/fernando/Área de trabalho/{num}--NumerosPrimos--{data()}--.txt', 'a+', encoding='UTF-8')as file:
    file.seek(0)
    zero = str(num)
    qtdZero = len(zero) + 1
    ini = time.perf_counter()
    for i in range(num):
        # print(f'{i + 1}º = {next(n)}'.zfill(qtdZero))
        if (i + 1) % 4 != 0:
            file.writelines(f'{str(i + 1).zfill(qtdZero)}º = {str(next(n)).zfill(qtdZero)}  ---  ')
        else:
            file.writelines(f'{str(i + 1).zfill(qtdZero)}º = {str(next(n)).zfill(qtdZero)}    \n')
    term = time.perf_counter()
    sec = round(term - ini, 2)
    c = ConvertSec(sec)
    file.writelines(f'\n\nTerminado em {sec} segundo(s), {c.convert_sec()}\n\n')
