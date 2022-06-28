"""
Faça um Programa que pergunte quanto você ganha por hora e
o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""

hora = ''
qtd_hora = ''

while not hora.isnumeric() and not qtd_hora.isnumeric():

    hora = input('Quanto você ganha por hora? R$')
    qtd_hora = input('Qunatas horas você trabalhou este mês? ')

    if not hora.isnumeric() and not qtd_hora.isnumeric():
        print('Digite somente números.')
        continue
    else:
        float(hora)
        float(qtd_hora)
        break

salario = float(hora) * float(qtd_hora)
print(f'O seu salario este mês é de R${salario:.2f}')
