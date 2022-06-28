'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada
seja invertida.
'''

nome = input('Digite seu nome: ').upper()
cont = len(nome)
while cont > 0:
    print(nome[:cont])
    cont -= 1
