''' Crie uma função que exiba uma saudação com os parametros saudação e nome.
'''


# def saud(nome, saudacao):
#     frase = f'{saudacao}, {nome}'
#     print(frase)


# saud('Fernando', 'Olá')

'''
com expressões lambda
'''
# frase = lambda nome, saudacao: print(f'{saudacao}, {nome}!!!')
# frase('Fernando', 'Bom dia')

'''
Crie uma função que recebe 2 números. O primeiro é um valor e o segundo um
percentual(ex: 10%).Retorne o valor do primeiro número somado do aumeneto
do percentual do mesmo.
'''


# def percent(numero, perc):
#     return float(numero) + (float(numero) * float(perc)) / 100


# num = input('Digite um número: ')
# perc = input('Digite a porcentagem: ')

# print(f'O valor somado ao percental é: {percent(float(num), float(perc))}')


'''
Fizz Buzz - Se o parametro da função for divsivel por 3, retorne fizz,
se o parametro da funçao for divivel por 5, retorne buzz. Sei o parametro
da função for divisivel por 5 e 3, retorne fizzbuzz, caso contrario retorne
o numero enviado.
'''


def FizzBuzz(numero):
    numero = float(numero)
    if float(numero) % 3 == 0 and not float(numero) % 5 == 0:
        return 'Fizz'
    elif float(numero) % 5 == 0 and not float(numero) % 3 == 0:
        return 'Buzz'
    elif float(numero) % 3 == 0 and float(numero) % 5 == 0:
        return'FizzBuzz'
    else:
        return numero


num = input('Digite um numero: ')
print(FizzBuzz(num))
