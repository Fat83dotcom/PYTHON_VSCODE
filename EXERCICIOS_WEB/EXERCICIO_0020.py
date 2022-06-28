'''
Crie um dicionário que é uma agenda e
coloque nele os seguintes dados: chave (cpf),
nome, idade, telefone. O programa deve ler
um número indeterminado de dados, criar a
agenda e imprimir todos os itens do
dicionário no formato chave: nome-idade-fone.
'''
d1 = {}  # type: dict
cont = 0
while 1:
    id1 = input('Digite o CPF do cadastro ou 0(Zero) para sair: ')
    if id1 == '0':
        break
    else:
        if id1 not in d1.keys():
            d1.update({f'{id1}': {
                'nome': input('Digite o nome: '),
                'idade': input('digite a idade: '),
                'telefone': input('Digite o telefone: ')
                },
            },)
        else:
            print('CPF já cadastrado.')
            continue

try:
    for k, v in d1.items():
        with open('exercicio20.txt', 'a+', encoding='utf-8') as file:
            file.write(f'{k}\t{v}\n')
            print(f'{k}\t{v}')
except NameError:
    print('Fim')
