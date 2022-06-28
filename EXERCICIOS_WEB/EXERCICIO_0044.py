animais = ['gato', 'cachorro', 'rato', 'cavalo', 'elefante', 'girafa', 'tatu']
# excluidos = []

# for animal in animais:
#     if len(animal) > 4:
#         excluidos.append(animal)

# for excluido in excluidos:
#     animais.remove(excluido)

# del excluidos 

# print(animais)
# animais = ['gato', 'cachorro', 'rato', 'cavalo', 'elefante', 'girafa', 'tatu']
# excluidos = [animal for animal in animais if len(animal) > 4]
# resultado = [animais.remove(excluido) for excluido in excluidos]
# del excluidos
# del resultado

# print(animais)

lista = ['gato', 'cachorro', 'papagaio', 'canguru', 'rato', 'tatu', 'tamanduá', 'tucano']

def animal(nome):
    return len(nome) < 5

print(list(filter (animal, lista)))