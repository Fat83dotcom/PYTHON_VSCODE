"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
num = []
soma = float()
for n in range(0, 4):
    num.append(float(input('Digite a {0}º nota: '.format(n + 1))))
    soma += num[n]
print(f'A media das notas foi: {soma / 4}')
