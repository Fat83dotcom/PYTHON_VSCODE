'''
calcule o imc, usando a seguinte fórmula: peso(kg)/altura²(m)
 '''
peso = ''
altura = ''
while not peso and not altura:
    peso = input('Digite seu peso em kg:')
    altura = input('Digite sua altura em metros(use ponto para os decimais)')
    try:
        imc = float(peso) / (float(altura) * float(altura))
    except ValueError:
        print('Digite somente números e ponto decimal.')
        peso = ''
        altura = ''
        continue
    print(f'Seu IMC é : {imc:.2f}')
