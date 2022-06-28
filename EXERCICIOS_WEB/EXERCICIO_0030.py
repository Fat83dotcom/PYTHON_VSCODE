'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome
em formato de escada.
'''

nome = input('Digite seu nome: ').upper()
cont = 0
while cont <= len(nome):
    print(nome[:cont])
    cont += 1
