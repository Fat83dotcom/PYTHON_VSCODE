'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''


altura = ''
while not altura:
    altura = input('Digite sua altura(m): ')
    try:
        if float(altura):
            sexo = ''
            while not sexo:
                sexo = input('Qual seu sexo(M/F): ').upper()
                if 'M' in sexo[0]:
                    pM = (72.7 * float(altura)) - 58
                    print(f'Seu peso ideal é: {pM:.2f} kg.')
                    break
                elif 'F' in sexo[0]:
                    pF = (62.1 * float(altura)) - 44.7
                    print(f'Seu peso ideal é: {pF:.2f} kg.')
                    break
                else:
                    print('Digite M ou F somente.')
                    sexo = ''
                    continue
    except ValueError:
        print('Digite um número valido.')
        altura = ''
        continue
