'''
Implemente uma função chamada mostrar_unicos, que recebe uma lista de valores como entrada
e retorna outra lista com os elementos da entrada sem repeti-los.Não é necessario que a lista com
os valores n saída esteja ordenada.
'''


def mostrar_unicos(lista):
    uni = []
    cont = 0
    for n in range(len(lista)):
        for i in lista:
            if i == lista[n]:
                cont += 1
        if cont == 1:
            uni.append(lista[n])
            cont = 0
        else:
            cont = 0
    return uni


print(mostrar_unicos([3, 1, 2, 1, 5, 6, 7, 4, 5]))
