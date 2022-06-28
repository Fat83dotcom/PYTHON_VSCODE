'''
Considerando duas listas de inteiros ou floats(lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

se uma lista fo menor que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
listaa = [1, 2, 3, 4, 5]
listab = [3, 4, 5, 6, 7, 8, 9]

soma = [4, 6, 8, 10, 12]
'''
from random import randint
from itertools import zip_longest
nl1 = randint(1, 10)
nl2 = randint(1, 10)

l1 = [randint(1, 100) for i in range(nl1)]
l2 = [randint(1, 100) for i in range(nl2)]

uni1 = zip(l1, l2)
uni2 = zip_longest(l1, l2, fillvalue=0)
soma1 = [(a + b) for a, b in uni1]
soma2 = [(a + b) for a, b in uni2]

print(f'Lista 1 = {l1}')
print(f'Lista 2 = {l2}')
print(f'Soma 1 = {soma1}')
print(f'Soma 2 = {soma2}')
