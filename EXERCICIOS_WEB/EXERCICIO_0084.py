'''
Faça um programa que leia o nome e peso de varios usuarios, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''


def p_pesos(lista):
    p_leve = []
    p_pesada = []
    for i in lista:
        if i[1].isnumeric():
            if i == 0:
                ref_min = int(i[1])
                ref_max = int(i[1])
        else:
            print('Você digitou algum número invalido, tente novamente')
            return None
    for i in range(len(lista)):
        if i == 0:
            p_leve.append(lista[i][0])
            ref_min = lista[i][1]
            p_pesada.append(lista[i][0])
            ref_max = lista[i][1]
        else:
            if lista[i][1] == ref_min:
                p_leve.append(lista[i][0])
            elif lista[i][1] < ref_min:
                p_leve.clear()
                p_leve.append(lista[i][0])
                ref_min = lista[i][1]
            if lista[i][1] == ref_max:
                p_pesada.append(lista[i][0])
            elif lista[i][1] > ref_max:
                p_pesada.clear()
                p_pesada.append(lista[i][0])
                ref_max = lista[i][1]
    print(f'O maior peso foi de {ref_max}Kg. Peso de {p_pesada}')
    print(f'O menor peso foi de {ref_min}Kg. Peso de {p_leve}')
    return 1


cadastro = []
item = []
n_pessoas = 0

while True:
    item.append(input('Nome: ').upper())
    item.append(input('Peso Kg: '))
    cadastro.append(item[:])
    item.clear()
    n_pessoas += 1
    saida = input('Deseja continuar? [S/N]: ').upper()
    if saida[0] == 'N':
        print(f'{n_pessoas} pessoas foram cadastradas.')
        c = p_pesos(cadastro)
        break
    else:
        continue
