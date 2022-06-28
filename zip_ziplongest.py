cidade = ['são paulo', 'rio de janeiro', 'salvador']
estados = ['sao paulo', 'rio de janeiro', 'bahia']

juntando = zip(cidade, estados)

print(next(juntando))
print(next(juntando))
print(next(juntando))

juntando = zip(cidade, estados)

for i in juntando:
    print(i)
