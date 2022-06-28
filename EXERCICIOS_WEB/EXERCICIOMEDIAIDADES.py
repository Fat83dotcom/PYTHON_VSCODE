somaIdadeHomem = somaIdadeMulher = maiorIdade = menorIdade = 0
contadorHomens = contadorMulheres = 0

while True:
    idadeGenerica = int(input('Digite a idade(Número negativo para sair): '))
    if idadeGenerica < 0:
        print('Até mais')
        break
    sexo = input('Digite o sexo(M/F): ').upper()
    if contadorMulheres == 0 and contadorHomens == 0:
        maiorIdade = idadeGenerica
        menorIdade = idadeGenerica
    if sexo == 'M':
        somaIdadeHomem += idadeGenerica
        contadorHomens += 1
    elif sexo == 'F':
        somaIdadeMulher += idadeGenerica
        contadorMulheres += 1
    else:
        print('Digite M ou F somente.')
        continue
    if maiorIdade < idadeGenerica:
        maiorIdade = idadeGenerica
    if menorIdade > idadeGenerica:
        menorIdade = idadeGenerica

if contadorHomens != 0:
    mediaIdadeHomens = somaIdadeHomem / contadorHomens
    print(f'A média da idade dos homens é: {round(mediaIdadeHomens, 2)} anos.')
else:
    print('Não houve homens suficientes para efetuar a media.')

if contadorMulheres != 0:
    mediaIdadeMulheres = somaIdadeMulher / contadorMulheres
    print(f'A média da idade das mulheres é: {round(mediaIdadeMulheres, 2)} anos.')
else:
    print('Não houve mulheres suficientes para efetuar a media.')

print(f'A maior idade foi: {maiorIdade} anos, e a menor foi {menorIdade} anos.')
