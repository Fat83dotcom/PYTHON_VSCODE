'''
Faça um Programa que peça 2 números inteiros e um número real.Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
num = ''
num2 = ''
num3 = ''
while num == '' and num2 == '' and num3 == '':
    num = input('Digite um número inteiro: ')
    num2 = input('Digite um número inteiro: ')
    num3 = input('Digite um número real: ')
    try:
        if num.isnumeric() and num2.isnumeric() or '.' in num3:
            mult = (int(num) * 2) * (float(num2) / 2)
            soma = (int(num) * 3) + float(num3)
            quad = pow(float(num3), 3)
            print(
                f'O prod. do dobro do primeiro com metade do segundo: {mult}')
            print(f'A soma do triplo do primeiro com o terceiro: {soma}')
            print(f'O terceiro elevado ao cubo: {quad:.2f}')
            break
        else:
            print('Digite somente números.')
            num = ''
            num2 = ''
            num3 = ''
            continue
    except ValueError:
        print('Digite ponto somente com números.')
        num = ''
        num2 = ''
        num3 = ''
        continue
