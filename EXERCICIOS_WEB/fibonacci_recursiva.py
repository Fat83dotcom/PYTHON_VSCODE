def fibo(cont, b=0, a=1, retorno=[]):
    if b == 0:
        cont -= 2
        retorno.append(b)
        print(b)
    retorno.append(a)
    print(a)
    if cont == 0:
        return retorno
    else:
        return fibo(cont-1, b=a, a=a+b)


print(fibo(100))
