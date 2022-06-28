'''
Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista
única que mantenha separados os valores pares e ipares. No fina,  mostre os valores pares e impares
em ordem crescente.
'''

cadastro = [[], []]

for i in range(7):
    num = float(input(f'Digite o {i + 1}º número:'))
    if num % 2 == 0:
        cadastro[0].append(num)
    else:
        cadastro[1].append(num)
print(f'Os valores pares são: {sorted(cadastro[0])}')
print(f'Os valores impares são: {sorted(cadastro[1])}')
