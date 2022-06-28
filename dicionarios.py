d1 = {'chave': 'valor'}
print(d1)

d2 = {
    'str': 12,
    123: 'ddd',
    (1, 2): 23
}
# print(d1['naoexiste'])
d1['naoexiste'] = 'existe'
print(d1['naoexiste'])  # verifica se a chave existe
print(d1.get('chave3'))  # verifica se a chave existe

d1.update({'novachave': 'novovalor', 'novachave2': 'novovalor2'})  # Cria nova chave e novo valor
print(d1)

del d2['str']
print(d2)

print('valor' in d1.values())  # verifica se o valor existe

for k, v in d2.items():
    print(k, v)

for k in d2.items():
    print(k[0], k[1])
d4 = {}


def gera(id):
    d4.update({f'cliente{id}': {
            'nome': '',
            'endereço': 'None',
            'conta': 'None'
        },
    })


def cadastro():
    for i in range(3):
        gera(i)
    for cliente_k, valores_v in d4.items():  # Desempacota a chave cliente{id}, cujo valor é outro dicionario
        print(cliente_k)  # Mostra a chave.
        for k_v, v_v in valores_v.items():  # Desempacota o valor que é um dicionario onde estão os dados.
            print(f'Digite o {k_v} do cliente: ')  # Mostra a chave que guardará o dado correspondente
            valores_v[k_v] = 'teste'  # input()  Entra com o valor correspondente a chave.
    print(d4)


cadastro()

d5 = {}
d5['chave1'] = 'valor'
d5.update({'chave1': 'valor3'})
print(d5)
print(d4.get('cliente2'))
