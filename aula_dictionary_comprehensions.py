lista = [
    ('chave', 'valor'),
    ('chave1', 'valor1')
]
d1 = {x: y for x, y in lista}
print(d1)
d2 = {f'op{x}': x*9 for x in range(100)}
print(d2)
e = 'string'
letra = [x for x in e if x == 't']
print(letra)
