'''
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome
e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''
nome = input('Digite seu nome: ').upper()
contra = [i for i in nome[len(nome)-1::-1]]
nome = ''.join(contra)
print(nome)
