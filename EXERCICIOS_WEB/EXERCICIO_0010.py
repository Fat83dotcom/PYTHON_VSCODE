'''
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
'''
temp = ''
while temp == '':
    temp = input('Digite a temperatura em graus Celsius: ')
    try:
        if temp.isnumeric() or '.' in temp:
            f = ((9 * float(temp)) / 5) + 32
            print(f'A convesão de graus Celsius para Fahrenheit é {f:.2f}F.')
            break
        else:
            print('Digite somente números.')
            temp = ''
            continue
    except ValueError:
        print('Digite ponto somente com números.')
        temp = ''
        continue
