'''
Aprimore o exercicio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matrix = []
soma_par = 0
soma_3_col = 0

for i in range(3):
    linha = []
    matrix.append(linha)
    for j in range(3):
        coluna = [int(input(f'Digite um valor para {[i, j]}: '))]
        linha.append(coluna)
        if coluna[0] % 2 == 0:
            soma_par += coluna[0]
        if j == 2:
            soma_3_col += coluna[0]

for linha in matrix:
    print()
    for coluna in linha:
        print(f'{coluna}', end='')

print('\n')
print(f'A soma de todos os valores pares digitados: {soma_par}')
print(f'A soma dos valores da terceira coluna: {soma_3_col}')
print(f'O maior valor da segunda linha: {max(matrix[1])}')
print('\n')
