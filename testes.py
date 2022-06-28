# num1 = eval(input('Digite o primeiro número:'))
# num2 = eval(input('Digite o segundo número: '))

# if num1 > num2:
#     print(f'{num1} é maior que {num2}')
# elif num1 == num2:
#     print(f'{num1} é igual {num2}')
# else:
#     print(f'{num1} é menor que {num2}')

# for n in range(9, 8):
#     print(n)

# print(list(range(2, 9, 4)))

# nome = []
# for letra in 'Fernando':
#     nome.append(letra)
#     print(''.join(nome))
# nome = []
# for letra in 'Fernando'[::-1]:
#     nome.append(letra)
#     print(''.join(nome))


# numero = input('Digite um número: ')
# n_decomposto = []
# for i, n in enumerate(numero[::-1]):
#     n_decomposto.append((10**i)*int(n))

# print('O número é composto por: ', end=' ')

# for i, n in enumerate(n_decomposto[::-1]):
#     if i != (len(n_decomposto) - 1):
#         print(f'{n}', end=' + ')
#     else:
#         print(n)

# def func1(x):
#   x = 10
#   print(f'Função func1 - x = {x}')
 
 
# def func2(x):
#     x = 20
#     print(f'Função func2 - x = {x}')
 

# x = 45
# func1(x)
# func2(x)
# print(f'Programa principal: x = {x}')

# def fatorial(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * fatorial(x-1)

# print(fatorial(3))

# a = 0
# b = 1
# for n in range(200000):
#     c = a + b
#     a = b
#     b = c
#     print(n, c)


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
    

print(fibo(10))