# var = [1, 2, 3, 4, 5, 6, 7, 8]
# n1, n2, n3, *resto = var  # Os 3 primeiros itens da lista serão gurdados nas
# # variaveis n1, n2 n3 e o restante em resto

# print(n1, n2, n3, resto)

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)


# print(fibo(30))

from math import gcd


def func(a, b, c):
    a = a + b
    b = b + c
    c = a + b + c
    return a, b, c


var = func(24, 48, 96)
n1, n2, n3 = var

resto = gcd(n1, n2, n3)  # MDC, maior divisor comum

print(var, n1, resto)
