'''
O número 153 é igual a soma dos cubos dos algarismos que compoe.
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
Entre 100 e 999 também existem outros números que seguem esta propriedade.
Desenvolva um código Python que descobre quais são estes números.
'''


def p3(num):
    num = int(num)
    p_3 = num * num * num
    return p_3


for n1 in range(100, 999):
    nstr = str(n1)
    soma_p3 = p3(int(nstr[0])) + p3(int(nstr[1])) + p3(int(nstr[2]))
    if n1 == soma_p3:
        print(f'{nstr[0]}³ + {nstr[1]}³ + {nstr[2]}³ = {p3(int(nstr[0]))}'
              f' + {p3(int(nstr[1]))} + {p3(int(nstr[2]))} = {soma_p3}')
