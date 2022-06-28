'''
Crie um progama que leia nome e duas notas de varios alunos e guarde em uma lista composta.
No final, mostre um boletim contendo a média de cada um permita que o usuario possa mostrar as notas
de cadasa aluno individualmente.
'''
from itertools import count

c = count()

dados = []
while True:
    aluno = []
    soma = 0
    aluno.append(input('Digite o nome: '))
    aluno.append(float(input('Digite a 1ª nota: ')))
    aluno.append(float(input('Digite a 2ª nota: ')))
    soma = aluno[1] + aluno[2]
    media = soma / 2
    aluno.append(media)
    dados.append(aluno[:])
    saida = input('Deseja sair? [S/N]: ').upper()

    if saida[0] == 'S':
        print('Nº    Nome          Media')
        for aluno in dados:
            print(f'{next(c)}', end='')
            print(f'     {aluno[0]}', end='')
            print(f'           {round(aluno[3], 2)}')

        info = input('\nDeseja saber as notas dos alunos? [S/N]').upper()
        if info[0] == 'S':
            flag = 0
            while flag != 999:
                flag = int(input('Digite o número do aluno, 999 para sair: '))
                if flag != 999 and flag < len(dados):
                    print(f'\nO aluno {dados[flag][0]} tem as notas {dados[flag][1]}, {dados[flag][2]}\n')
                elif flag == 999:
                    print('Até mais...')
                    break
                else:
                    print('Digite um número válido.')
                    continue
            break
        else:
            break
    else:
        continue
