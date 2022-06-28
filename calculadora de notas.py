numeroDeNotas = int(input('Digite a quantidade de notas a serem computadas: '))

while 1:

    numeroDaMedia = float(input('Digite a media desejada: '))

    somatorio = 0
    for i in range(numeroDeNotas - 1):
        nota = float(input(f'Digite {i + 1}º a nota: '))
        somatorio += nota

    diferenca = numeroDaMedia * numeroDeNotas
    passo1 = (diferenca - somatorio)
    media = (passo1 + somatorio) / numeroDeNotas

    print(f'Nota a ser colocada {passo1}')
    print(media)

    saida = input('Deseja outro calculo?[S/N]').upper()
    if saida == 'S':
        continue
    else:
        break
