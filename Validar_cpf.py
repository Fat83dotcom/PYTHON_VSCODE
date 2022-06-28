entry = input('Digite um CPF no formato xxx.xxx.xxx-xx: ')


cpf1 = [x for x in entry]
cpf2 = list()


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
        print('CPF válido.')
    else:
        print('CPF inválido.')
else:
    print('CPF inválido')
