'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''
temp = ''
while temp == '':
    temp = input('Digite a temperatura em Fahrenheit: ')
    try:
        if temp.isnumeric() or '.' in temp:
            c = 5 * ((float(temp) - 32) / 9)
            print(f'A conversão da temperatura em graus Celsius é {c:.2f}°C')
            break
        else:
            print('Digite somente números.')
            temp = ''
            continue
    except ValueError:
        print('Digite pontos somente com números.')
        temp = ''
        continue
