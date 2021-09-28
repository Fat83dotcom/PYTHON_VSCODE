def primos(ini, fim):
    div = 0
    primos = list()
    for i in range(ini, fim):
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div == 2:
            primos.append(i)
            div = 0
        else:
            div = 0
    print(primos)


primos(100, 300)
