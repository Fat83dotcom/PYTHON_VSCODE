'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo
'''

def fibona():
    a = 0
    b = 1
    while 1:
        c = a + b
        a = b
        b = c
        yield c


while 1:
    f = fibona()
    num = input('Digite a quantidade de termos da sequência fibonacci: ')
    
    for i in range(int(num)):
        print(f'O {i + 1}º termo da sequencia é: {next(f)}')
    
    saida = input('Deseja outra rodada? S/N: ').upper()
    if saida == 'S':
        continue
    else:
        break
