'''
Faça um programa que leia 15 números inteiros e positivos e mostre o maior deles.
'''
maior_Numero_Coletado = 0
for posicao_Numero_Coletado in range(15):
    numero_Coletado = int(input(f'Digite o {posicao_Numero_Coletado + 1}º número :'))
    if posicao_Numero_Coletado == 0:
        maior_Numero_Coletado = numero_Coletado
        continue
    if numero_Coletado > maior_Numero_Coletado:
        maior_Numero_Coletado = numero_Coletado

print(f'\nO maior número digitado foi: {maior_Numero_Coletado}\n')
