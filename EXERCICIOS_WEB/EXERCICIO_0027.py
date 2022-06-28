'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''
num = input("Digite um número: ")
num = int(num)
div = 0

for i in range(num):
    if num % (i+1) == 0:
        div += 1
if div == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
    