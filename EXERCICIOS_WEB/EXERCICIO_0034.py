'''
Validar CPF
'''


def valida_pont(cpf):
    entry = cpf
    cpf1 = [x for x in entry]
    cpf2 = []

    if len(entry) == 14:
        if entry[0].isdigit():
            cpf2.append(entry[0])
        if entry[1].isdigit():
            cpf2.append(entry[1])
        if entry[2].isdigit():
            cpf2.append(entry[2])
        if entry[3] == '.':
            cpf2.append(entry[3])
        if entry[4].isdigit():
            cpf2.append(entry[4])
        if entry[5].isdigit():
            cpf2.append(entry[5])
        if entry[6].isdigit():
            cpf2.append(entry[6])
        if entry[7] == '.':
            cpf2.append(entry[7])
        if entry[8].isdigit():
            cpf2.append(entry[8])
        if entry[9].isdigit():
            cpf2.append(entry[9])
        if entry[10].isdigit():
            cpf2.append(entry[10])
        if entry[11] == '-':
            cpf2.append(entry[11])
        if entry[12].isdigit():
            cpf2.append(entry[12])
        if entry[13].isdigit():
            cpf2.append(entry[13])
        if cpf1 == cpf2:
            return cpf1
        else:
            return ''
    else:
        return ''


while True:
    entra = input('Digite um CPF  no formato xxx.xxx.xxx-xx: ')
    cpf = valida_pont(entra)
    if cpf == '':
        print('Voce digitou alguma coisa errada, verifique a digitação.')
        continue

    cpf_raw1 = [n for n in cpf if n != '.' if n != '-']
    cpf_raw2 = cpf_raw1[:-2]

    soma_result = 0
    for i, n in enumerate(cpf_raw2):
        soma_result += int(n) * (10 - i)
    dig1 = 11 - (soma_result % 11)

    if dig1 > 9:
        dig1 = 0

    cpf_raw2.append(str(dig1))
    soma_result = 0
    for i, n in enumerate(cpf_raw2):
        soma_result += int(n) * (11 - i)

    dig2 = 11 - (soma_result % 11)
    cpf_raw2.append(str(dig2))

    if cpf_raw1 == cpf_raw2:
        print('CPF válido.')
    else:
        print('CPF inválido.')
