'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.'''


def numerador():
    n = 1
    while 1:
        yield n
        n += 1


def denominador():
    m = 1
    while 1:
        if m % 2 != 0:
            yield m
        m += 1


while 1:
    qtd = input('Digite a quantidade de frações que seram somadas: ')
    n = numerador()
    m = denominador()
    soma = 0
    for i in range(int(qtd)):
        numera = next(n)
        denomina = next(m)
        if i == 0:
            print(f'S = {numera}/{denomina}', end='')
        else:
            print(f' + {numera}/{denomina}', end='')
        
        soma += (numera / denomina)

    print()
    print(f'A soma dos termos foi: {soma}')
    
    saida = input('Deseja sair, S/N: ').upper()
    if saida == "S":
        break
    else:
        continue
