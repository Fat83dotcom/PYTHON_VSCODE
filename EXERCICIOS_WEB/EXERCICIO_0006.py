"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
raio = ''
while not raio.isnumeric():
    raio = input('Digite o tamanho do raio em cm: ')
    if '.' in raio():
        break
    if not raio.isdigit():
        print('Digite um número.')
        continue
area = (float(raio) * float(raio)) * 3.1415
print(f'A área do circulo de raio {raio} é igual a: {area:.2f} cm')
