'''
-> Agrupando valores em um dicionario
'''
from itertools import groupby

alunos = [{'nome': 'Nome Aluno1', 'nota': 'A'},
          {'nome': 'Nome Aluno2', 'nota': 'B'},
          {'nome': 'Nome Aluno3', 'nota': 'B'},
          {'nome': 'Nome Aluno4', 'nota': 'E'},
          {'nome': 'Nome Aluno5', 'nota': 'D'},
          {'nome': 'Nome Aluno6', 'nota': 'A'},
          {'nome': 'Nome Aluno7', 'nota': 'A'},
          {'nome': 'Nome Aluno8', 'nota': 'E'},
          {'nome': 'Nome Aluno9', 'nota': 'D'},
          {'nome': 'Nome Aluno10', 'nota': 'A'},
          {'nome': 'Nome Aluno11', 'nota': 'B'}, ]


def ordena(item):
    return item['nota']


alunos.sort(key=ordena)
print(alunos)
alunosAgrupados = groupby(alunos, ordena)

for agrupamento, agrupados in alunosAgrupados:
    quantidade = len(list(agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
