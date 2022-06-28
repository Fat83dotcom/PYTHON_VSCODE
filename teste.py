idade = idades_homem = idades_mulher = maior = menor = 0
homens = mulheres = 1
while idade >= 0:
    idade = int(input("Idade [ou um valor negativo para encerrar]: "))
    if idade < 0:
        break
    else:
        sexo = input("Informe o sexo do habitante [M/F]: ")
        if maior == 0 or idade > maior:
            maior = idade
        elif menor == 0 or idade < menor:
            menor = idade
        elif sexo in 'Mm':
            idades_homem += idade
            if idades_homem == 0:
                homens = 1
            else:
                homens += 1
        elif sexo in 'Ff':
            idades_mulher += idade
            if idades_mulher == 0:
                mulheres = 1
            else:
                mulheres += 1
media_homens = idades_homem / homens
media_mulheres = idades_mulher / mulheres
print(f"""A média de idade dos homens é de {media_homens:.1f} anos.
A média de idade das mulheres é de {media_mulheres:.1f} anos.
A maior idade do grupo é {maior} anos.
E a menor idade do grupo é {menor} anos.""")
