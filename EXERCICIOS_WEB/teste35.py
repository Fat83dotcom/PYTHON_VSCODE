# def gera_palavra(palavras):
#     for p in palavras:
#         yield p


# palavras = ['buceta', 'pica', 'bunda']
# p = gera_palavra(palavras)

# print(next(p))
# print(next(p))
# print(next(p))

from itertools import count

cont = count()

for i in range(10):
    print(next(cont))
