import sys

# lista = [1, 2, 3, 4, 5, 6, 7]
# print(sys.getsizeof(lista))

# numlist = len(lista)
# lista = iter(lista)

# cont = 0
# while cont < numlist:
#     print(next(lista), end=', ')
#     cont += 1

# print(sys.getsizeof(lista))
'''
A função fib gera, a cada iteração um expoente na base 2

1 -> 2¹
2 -> 2²
3 -> 2³
...

'''
fator = 100

def fib():
    a = 0
    b = 1
    while 1: 
        a = b
        b = a + b
        yield b

def fib2(tam):
    a = 0
    b = 1
    l = []
    cont = 0
    while cont < tam:
        a = b
        b = a + b
        l.append(b)
        cont += 1
    
    return l


f = fib()

for i in range(fator): 
    print(next(f))

l = fib2(fator)

for i in l:
    print(i)


print(sys.getsizeof(f))
print(sys.getsizeof(l))