'''
Leia	 do	 usuário	 o	 tempo	 em	 segundos	 e	 o	 escreva	 em	 horas,	 minutos
e	 segundos.
Utilize	 cinco	 métodos: para	 a	 leitura	 e	 escrita	 de	 dados e para	 obtenção
de	 horas,
minutos	e	segundos	a	partir	do	tempo	em	segundos.
'''
usu_sec = ''
hora = minuto = segundo = 0
while not usu_sec.isnumeric():
    usu_sec = input("Digite o tempo em segundos ou sair: ")
    if usu_sec.isnumeric():
        usu_sec = int(usu_sec)
        if usu_sec >= 3600:
            hora = usu_sec // 3600
            usu_sec = usu_sec - (3600 * hora)
            minuto = usu_sec // 60
            usu_sec = usu_sec - (60 * minuto)
            segundo = usu_sec
            print(f'{hora}:{minuto}:{segundo}')
            usu_sec = ''
            hora = minuto = segundo = 0
        elif 60 <= usu_sec < 3600:
            minuto = usu_sec // 60
            usu_sec = usu_sec - (60 * minuto)
            segundo = usu_sec
            print(f'{hora}:{minuto}:{segundo}')
            usu_sec = ''
            hora = minuto = segundo = 0
        else:
            segundo = usu_sec
            print(f'{hora}:{minuto}:{segundo}')
            usu_sec = ''
            hora = minuto = segundo = 0
    elif usu_sec[0].upper() == "S":
        break
