
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = [string[i:i+10] for i in range(0, len(string), 10)]
lista2 = '.'.join(lista)
print(lista)
print(lista2)
lista1 = [int(x) * int(x) for x in string if int(x) > 4]
print(lista1)
lista3 = [x.replace('8', 'oito').zfill(5) for x in string]
print(lista3)
