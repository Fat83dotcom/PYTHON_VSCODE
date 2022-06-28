'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos do teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

matrix = []

for i in range(3):
    linha = []
    matrix.append(linha)
    for j in range(3):
        coluna = [int(input(f'Digite um valor para {[i, j]}: '))]
        linha.append(coluna[:])

for linha in matrix:
    print()
    for coluna in linha:
        print(f'{coluna}', end='')
print('\n')
