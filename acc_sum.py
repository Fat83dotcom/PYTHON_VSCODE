def acc_sum(lista):
    soma = list()
    for i in range(len(lista)):
        if i == 0:
            soma.append(lista[0] + 0)
        else:
            soma.append(soma[i - 1] + lista[i])
    print(lista)
    print(soma)


acc_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
