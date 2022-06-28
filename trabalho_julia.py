def extracaoDados(diario=str(), mensal=str()):
    if diario:
        with open(diario, 'r') as file:
            dadosDiarios = []
            dadosPorLinha = [linha.split() for linha in file.readlines()]
            for linha in dadosPorLinha:
                dadosDiarios.append({'ano': int(linha[0]),
                                     'mes': int(linha[1]),
                                     'dia': int(linha[2]),
                                     'dataFracao': float(linha[3]),
                                     'nManchas': int(linha[4]),
                                     'dvPadra': float(linha[5]),
                                     'nObserv': int(linha[6])}
                                    )

            return dadosDiarios
    else:
        with open(mensal, 'r') as file:
            dadosMensais = []
            dadosPorLinha = [linha.split() for linha in file.readlines()]
            for linha in dadosPorLinha:
                dadosMensais.append({'ano': int(linha[0]),
                                     'mes': int(linha[1]),
                                     'dataFracao': float(linha[2]),
                                     'mediaMensalManchas': float(linha[3]),
                                     'dvPadraMensal': float(linha[4]),
                                     'nObserv': int(linha[5])}
                                    )

            return dadosMensais


def geradorDeMeses(numeroDoMes):
    if numeroDoMes == 1:
        return 'Janeiro'
    elif numeroDoMes == 2:
        return 'Fevereiro'

    elif numeroDoMes == 3:
        return 'Março'

    elif numeroDoMes == 4:
        return 'Abril'

    elif numeroDoMes == 5:
        return 'Maio'

    elif numeroDoMes == 6:
        return 'Junho'

    elif numeroDoMes == 7:
        return 'Julho'

    elif numeroDoMes == 8:
        return 'Agosto'

    elif numeroDoMes == 9:
        return 'Setembro'

    elif numeroDoMes == 10:
        return 'Outubro'

    elif numeroDoMes == 11:
        return 'Novembro'

    elif numeroDoMes == 12:
        return 'Dezembro'


def diasManchasNaoObservadas(ano, diario):
    extrato = extracaoDados(diario=diario)
    filtradoPorAno = [extratAno for extratAno in extrato if extratAno['ano'] == ano]

    resultado = []
    for dados in filtradoPorAno:
        for k, v in dados.items():
            if k == 'mes':
                resultado.append(v)
            if k == 'nManchas':
                resultado.append(v)
    print('\n')
    for mesAtual in range(1, 13):
        soma = 0
        for nManchasAtual in range(len(resultado)):
            if nManchasAtual % 2 == 0 and resultado[nManchasAtual] == mesAtual:
                if int(resultado[nManchasAtual + 1]) == 0:
                    soma += 1
        print(f'{geradorDeMeses(mesAtual)}: {soma} dias.')


def mesAnoMaisDiasSemManchas(diario):
    extrato = extracaoDados(diario=diario)
    dadosFiltrado = []
    for n, dado in enumerate(extrato):
        dadoTemporario = []
        for k, v in dado.items():
            if k == 'ano':
                dadoTemporario.append(v)
            if k == 'mes':
                dadoTemporario.append(v)
            if k == 'nManchas':
                dadoTemporario.append(v)
        dadosFiltrado.append(dadoTemporario)
    anoAtual = dadosFiltrado[0][0]
    soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maior = 0
    anoMesEMaiorValor1 = []
    anoMesEMaiorValor2 = []

    for dadosAnalizados in dadosFiltrado:
        # print(somatorioMensal)
        # print(soma)
        if anoAtual == dadosAnalizados[0]:
            if dadosAnalizados[1] == 1:
                if dadosAnalizados[2] == 0:
                    soma[0] += 1
                else:
                    soma[0] += 0
            elif dadosAnalizados[1] == 2:
                if dadosAnalizados[2] == 0:
                    soma[1] += 1
                else:
                    soma[1] += 0
            elif dadosAnalizados[1] == 3:
                if dadosAnalizados[2] == 0:
                    soma[2] += 1
                else:
                    soma[2] += 0
            elif dadosAnalizados[1] == 4:
                if dadosAnalizados[2] == 0:
                    soma[3] += 1
                else:
                    soma[3] += 0
            elif dadosAnalizados[1] == 5:
                if dadosAnalizados[2] == 0:
                    soma[4] += 1
                else:
                    soma[4] += 0
            elif dadosAnalizados[1] == 6:
                if dadosAnalizados[2] == 0:
                    soma[5] += 1
                else:
                    soma[5] += 0
            elif dadosAnalizados[1] == 7:
                if dadosAnalizados[2] == 0:
                    soma[6] += 1
                else:
                    soma[6] += 0
            elif dadosAnalizados[1] == 8:
                if dadosAnalizados[2] == 0:
                    soma[7] += 1
                else:
                    soma[7] += 0
            elif dadosAnalizados[1] == 9:
                if dadosAnalizados[2] == 0:
                    soma[8] += 1
                else:
                    soma[8] += 0
            elif dadosAnalizados[1] == 10:
                if dadosAnalizados[2] == 0:
                    soma[9] += 1
                else:
                    soma[9] += 0
            elif dadosAnalizados[1] == 11:
                if dadosAnalizados[2] == 0:
                    soma[10] += 1
                else:
                    soma[10] += 0
            elif dadosAnalizados[1] == 12:
                if dadosAnalizados[2] == 0:
                    soma[11] += 1
                else:
                    soma[11] += 0
        else:
            valorMaximo = None
            mesMaior = None
            for indice, numero in enumerate(soma):
                if (valorMaximo is None or numero > valorMaximo):
                    valorMaximo = numero
                    mesMaior = indice

            if valorMaximo >= maior:
                anoMesEMaiorValor1 = []
                maior = valorMaximo
                anoMesEMaiorValor1.append(dadosAnalizados[0] - 1)
                anoMesEMaiorValor1.append(mesMaior + 1)
                anoMesEMaiorValor1.append(maior)
                anoMesEMaiorValor2.append(anoMesEMaiorValor1)
                tamanho = len(anoMesEMaiorValor2)
                if tamanho > 1:
                    if anoMesEMaiorValor2[tamanho - 1][2] > anoMesEMaiorValor2[tamanho - 2][2]:
                        anoMesEMaiorValor2.pop(tamanho - 2)

            soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if dadosAnalizados[1] == 1:
                if dadosAnalizados[2] == 0:
                    soma[0] += 1
                else:
                    soma[0] += 0
            anoAtual += 1
    for datas in anoMesEMaiorValor2:
        print(f'{geradorDeMeses(datas[1])} de {datas[0]}, '
              f'com {datas[2]} dia(s) sem manchas solares.')


def mesAnoMaisManchas(diario):
    extrato = extracaoDados(diario=diario)
    dadosFiltrado = []
    for n, dado in enumerate(extrato):
        dadoTemporario = []
        for k, v in dado.items():
            if k == 'ano':
                dadoTemporario.append(v)
            if k == 'mes':
                dadoTemporario.append(v)
            if k == 'nManchas':
                dadoTemporario.append(v)
        dadosFiltrado.append(dadoTemporario)
    anoAtual = dadosFiltrado[0][0]
    soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    maior = 0
    anoMesEMaiorValor1 = []
    anoMesEMaiorValor2 = []

    for dadosAnalizados in dadosFiltrado:
        # print(somatorioMensal)
        # print(soma)
        if anoAtual == dadosAnalizados[0]:
            if dadosAnalizados[1] == 1:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[0] += dadosAnalizados[2]
                else:
                    soma[0] += 0
            elif dadosAnalizados[1] == 2:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[1] += dadosAnalizados[2]
                else:
                    soma[1] += 0
            elif dadosAnalizados[1] == 3:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[2] += dadosAnalizados[2]
                else:
                    soma[2] += 0
            elif dadosAnalizados[1] == 4:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[3] += dadosAnalizados[2]
                else:
                    soma[3] += 0
            elif dadosAnalizados[1] == 5:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[4] += dadosAnalizados[2]
                else:
                    soma[4] += 0
            elif dadosAnalizados[1] == 6:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[5] += dadosAnalizados[2]
                else:
                    soma[5] += 0
            elif dadosAnalizados[1] == 7:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[6] += dadosAnalizados[2]
                else:
                    soma[6] += 0
            elif dadosAnalizados[1] == 8:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[7] += dadosAnalizados[2]
                else:
                    soma[7] += 0
            elif dadosAnalizados[1] == 9:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[8] += dadosAnalizados[2]
                else:
                    soma[8] += 0
            elif dadosAnalizados[1] == 10:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[9] += dadosAnalizados[2]
                else:
                    soma[9] += 0
            elif dadosAnalizados[1] == 11:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[10] += dadosAnalizados[2]
                else:
                    soma[10] += 0
            elif dadosAnalizados[1] == 12:
                if dadosAnalizados[2] != 0 and dadosAnalizados[2] != -1:
                    soma[11] += dadosAnalizados[2]
                else:
                    soma[11] += 0
        else:
            valorMaximo = None
            mesMaior = None
            for indice, numero in enumerate(soma):
                if (valorMaximo is None or numero > valorMaximo):
                    valorMaximo = numero
                    mesMaior = indice

            if valorMaximo >= maior:
                anoMesEMaiorValor1 = []
                maior = valorMaximo
                anoMesEMaiorValor1.append(dadosAnalizados[0] - 1)
                anoMesEMaiorValor1.append(mesMaior + 1)
                anoMesEMaiorValor1.append(maior)
                anoMesEMaiorValor2.append(anoMesEMaiorValor1)
                tamanho = len(anoMesEMaiorValor2)
                if tamanho > 1:
                    if anoMesEMaiorValor2[tamanho - 1][2] > anoMesEMaiorValor2[tamanho - 2][2]:
                        anoMesEMaiorValor2.pop(tamanho - 2)

            soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if dadosAnalizados[1] == 1:
                if dadosAnalizados[2] == 0:
                    soma[0] += 1
                else:
                    soma[0] += 0
            anoAtual += 1
    for datas in anoMesEMaiorValor2:
        print(f'{geradorDeMeses(datas[1])} de {datas[0]}, '
              f'com {datas[2]} manchas solares.')


def maximoEMinimoDeManchas(anoInicio, mesInicio, anoTermino, mesTermino, diario):
    extrato = extracaoDados(diario=diario)
    dadosFiltrado = []
    for n, dado in enumerate(extrato):
        dadoTemporario = []
        anoTemporario = 0
        mesTemporario = 0
        for k, v in dado.items():
            if k == 'ano':
                if anoInicio == anoTermino:
                    if v == anoInicio and v < (anoTermino + 1):
                        anoTemporario = v
                if anoInicio < anoTermino:
                    if v >= anoInicio and v < (anoTermino + 1):
                        anoTemporario = v
            if k == 'mes':
                mesAtual = dado['mes']
                anoAtual = dado['ano']
                if anoInicio == anoTermino:
                    if v >= mesInicio and v < (mesTermino + 1):
                        mesTemporario = v
                if anoInicio < anoTermino:
                    if anoInicio == anoAtual:
                        if mesInicio <= v:
                            mesTemporario = v
                    if anoTermino > anoAtual and anoInicio != anoAtual:
                        mesTemporario = v
                    if anoTermino == anoAtual:
                        if mesAtual < (mesTermino + 1):
                            mesTemporario = v
            if k == 'nManchas':
                if anoTemporario != 0 and mesTemporario != 0:
                    dadoTemporario.append(anoTemporario)
                    dadoTemporario.append(mesTemporario)
                    dadoTemporario.append(v)
                if anoTemporario == (anoTermino) and mesTemporario == (mesTermino + 1):
                    break
        if anoTemporario == (anoTermino) and mesTemporario == (mesTermino + 1):
            break
        else:
            if len(dadoTemporario) != 0:
                dadosFiltrado.append(dadoTemporario)

    # print(dadosFiltrado)
    contadorDiasSemManchas = 0
    contadorDiasComManchas = 0
    maiorPeriodoComManchas = 0
    maiorPeriodoSemManchas = 0

    incicioPeriodoComMaiorNumeroDeManchas = []
    terminoPeriodoComMaiorNumeroDeManchas = []
    incicioPeriodoComMenorNumeroDeManchas = []
    terminoPeriodoComMenorNumeroDeManchas = []

    incicioPeriodoComMaiorNumeroDeManchasTemporario = []
    terminoPeriodoComMaiorNumeroDeManchasTemporario = []
    incicioPeriodoComMenorNumeroDeManchasTemporario = []
    terminoPeriodoComMenorNumeroDeManchasTemporario = []

    valoresColetadosNoMaiorPeriodo = []
    valoresColetadosNoMaiorPeriodoTemporario = []

    for dados in dadosFiltrado:
        if dados[2] != -1:
            if dados[2] > 0:
                if contadorDiasComManchas == 0:
                    if len(incicioPeriodoComMaiorNumeroDeManchasTemporario) > 0:
                        incicioPeriodoComMaiorNumeroDeManchasTemporario.clear()
                    if len(valoresColetadosNoMaiorPeriodoTemporario) > 0:
                        valoresColetadosNoMaiorPeriodoTemporario.clear()
                    contadorDiasComManchas += 1
                    incicioPeriodoComMaiorNumeroDeManchasTemporario.append([dados[0], dados[1]])
                    valoresColetadosNoMaiorPeriodoTemporario.append(dados[2])
                else:
                    contadorDiasComManchas += 1
                    valoresColetadosNoMaiorPeriodoTemporario.append(dados[2])
                    terminoPeriodoComMaiorNumeroDeManchasTemporario.clear()
                    terminoPeriodoComMaiorNumeroDeManchasTemporario.append([dados[0], dados[1], contadorDiasComManchas])
            else:
                if maiorPeriodoComManchas < contadorDiasComManchas:
                    maiorPeriodoComManchas = contadorDiasComManchas
                    incicioPeriodoComMaiorNumeroDeManchas = incicioPeriodoComMaiorNumeroDeManchasTemporario.copy()
                    terminoPeriodoComMaiorNumeroDeManchas = terminoPeriodoComMaiorNumeroDeManchasTemporario.copy()
                    valoresColetadosNoMaiorPeriodo = valoresColetadosNoMaiorPeriodoTemporario.copy()
                contadorDiasComManchas = 0

    for dados in dadosFiltrado:
        if dados[2] != -1:
            if dados[2] == 0:
                if contadorDiasSemManchas == 0:
                    if len(incicioPeriodoComMenorNumeroDeManchasTemporario) > 0:
                        incicioPeriodoComMenorNumeroDeManchasTemporario.clear()
                    contadorDiasSemManchas += 1
                    incicioPeriodoComMenorNumeroDeManchasTemporario.append([dados[0], dados[1]])

                else:
                    contadorDiasSemManchas += 1
                    terminoPeriodoComMenorNumeroDeManchasTemporario.clear()
                    terminoPeriodoComMenorNumeroDeManchasTemporario.append([dados[0], dados[1], contadorDiasSemManchas])
            else:
                if maiorPeriodoSemManchas < contadorDiasSemManchas:
                    maiorPeriodoSemManchas = contadorDiasSemManchas
                    incicioPeriodoComMenorNumeroDeManchas = incicioPeriodoComMenorNumeroDeManchasTemporario.copy()
                    terminoPeriodoComMenorNumeroDeManchas = terminoPeriodoComMenorNumeroDeManchasTemporario.copy()
                contadorDiasSemManchas = 0

    valorMaximo = None
    for numero in valoresColetadosNoMaiorPeriodo:
        if (valorMaximo is None or numero > valorMaximo):
            valorMaximo = numero

    print(f'\nDe {geradorDeMeses(incicioPeriodoComMaiorNumeroDeManchas[0][1])} '
          f'de {incicioPeriodoComMaiorNumeroDeManchas[0][0]} até {geradorDeMeses(terminoPeriodoComMaiorNumeroDeManchas[0][1] )} '
          f'de {terminoPeriodoComMaiorNumeroDeManchas[0][0]}, com {terminoPeriodoComMaiorNumeroDeManchas[0][2]} dias de observações '
          f'de manchas solares, sem interrupções, e uma máxima observação de {valorMaximo} manchas em um único dia.')
    print(f'\nDe {geradorDeMeses(incicioPeriodoComMenorNumeroDeManchas[0][1])} de {incicioPeriodoComMenorNumeroDeManchas[0][0]} '
          f'até {geradorDeMeses(terminoPeriodoComMenorNumeroDeManchas[0][1])} de {terminoPeriodoComMenorNumeroDeManchas[0][0]}, '
          f'com {terminoPeriodoComMenorNumeroDeManchas[0][2]} dias sem observações de manchas solares.')


def mediaMensalParaUmAno(ano, diario):
    extrato = extracaoDados(diario=diario)
    filtradoPorAno = [extratoAno for extratoAno in extrato if extratoAno['ano'] == ano]

    soma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for dados in filtradoPorAno:
        for k, v in dados.items():
            if k == 'mes':
                if v == 1:
                    soma[0] += dados['nManchas']
                    soma[1] += 1
            if k == 'mes':
                if v == 2:
                    soma[2] += dados['nManchas']
                    soma[3] += 1
            if k == 'mes':
                if v == 3:
                    soma[4] += dados['nManchas']
                    soma[5] += 1
            if k == 'mes':
                if v == 4:
                    soma[6] += dados['nManchas']
                    soma[7] += 1
            if k == 'mes':
                if v == 5:
                    soma[8] += dados['nManchas']
                    soma[9] += 1
            if k == 'mes':
                if v == 6:
                    soma[10] += dados['nManchas']
                    soma[11] += 1
            if k == 'mes':
                if v == 7:
                    soma[12] += dados['nManchas']
                    soma[13] += 1
            if k == 'mes':
                if v == 8:
                    soma[14] += dados['nManchas']
                    soma[15] += 1
            if k == 'mes':
                if v == 9:
                    soma[16] += dados['nManchas']
                    soma[17] += 1
            if k == 'mes':
                if v == 10:
                    soma[18] += dados['nManchas']
                    soma[19] += 1
            if k == 'mes':
                if v == 11:
                    soma[20] += dados['nManchas']
                    soma[21] += 1
            if k == 'mes':
                if v == 12:
                    soma[22] += dados['nManchas']
                    soma[23] += 1
    contadorDeMeses = 0
    for numero in range(0, 24):
        media = 0
        if numero % 2 == 0 and (soma[numero + 1]) != 0:
            media = soma[numero] / soma[numero + 1]
            print(f'A média para o mês de {geradorDeMeses(contadorDeMeses + 1)} foi de {round(media, 2)} manchas.')
            contadorDeMeses += 1


def main():
    menu = '''
    \n
            Escolha uma entre as opções abaixo:

    1 -> Contar os dias em que nao foram observadas manchas solares em cada mês, para um dado ano.
    2 -> Determinar os anos e meses que tiveram mais dias sem manchas solares.
    3 -> Determinar o ano e o mes que tiveram mais manchas solares.
    4 -> Determinar o maximo e o minimo de manchas solares em um período dado.
    5 -> Calcular a media mensal de cada mes, para um dado ano.
             Saída -> Digite um número maior que 5.
    \n
    '''
    while 1:
        arquivoDiario = 'SN_d_tot_V2.0.txt'
        # arquivoMensal = 'SN_m_tot_V2.0.txt'
        print(menu)
        marca = input('Digite um das opções acima: ')
        if marca.isnumeric():
            marca = int(marca)
            if marca == 1:
                print('\n1 -> Contar os dias em que nao foram observadas manchas solares em cada mês,'
                      'para um dado ano:\n')
                while 1:
                    ano = input('Digite o ano(entre 1818 e 2018): ')
                    if ano.isnumeric():
                        if (1818 <= int(ano) <= 2018):
                            diasManchasNaoObservadas(ano, arquivoDiario)
                            break
                        else:
                            print('\nDigite um número entre 1818 e 2018.\n')
                    else:
                        print('\nDigite um número entre 1818 e 2018.\n')
                marca = ''
            elif marca == 2:
                print('\n2 -> Determinar o ano e o mes que tiveram mais dias sem manchas solares.\n')
                mesAnoMaisDiasSemManchas(arquivoDiario)
                marca = ''
            elif marca == 3:
                print('\n3 -> Determinar o ano e o mes que tiveram mais manchas solares.\n')
                mesAnoMaisManchas(arquivoDiario)
                marca = ''
            elif marca == 4:
                print('\n4 -> Determinar o maximo e o minimo de manchas solares em um período dado.\n')
                while 1:
                    anoInicio = input('Entre com o ano inicial (entre 1818 e 2018): ')
                    mesInicio = input('Entre com o mês inicial (entre 1 e 12): ')
                    anoTermino = input('Entre com o ano final (entre o primeiro digitado e 2018): ')
                    mesTermino = input('Entre com o mês final (entre 1 e 12): ')
                    if anoInicio.isnumeric() and mesInicio.isnumeric() and anoTermino.isnumeric() and mesTermino.isnumeric():
                        if (1818 <= int(anoInicio) <= 2018) and (int(anoInicio) < int(anoTermino)):
                            if (1 <= int(mesInicio) <= 12) and (1 <= int(mesTermino) <= 12):
                                maximoEMinimoDeManchas(int(anoInicio), int(mesInicio), int(anoTermino),
                                                       int(mesTermino), arquivoDiario)
                                break
                            else:
                                print('\nDigite os meses entre 1 e 12.\n')
                        else:
                            print('\nDigite um número entre 1818 e 2018 e o inicio menor que o termino.\n')
                    else:
                        print('\nDigite somente números.\n')
                marca = ''
            elif marca == 5:
                print('\n5 -> Calcular a media mensal de cada mes, para um dado ano.\n')
                while 1:
                    ano = input('Digite o ano(entre 1818 e 2018): ')
                    if ano.isnumeric():
                        if (1818 <= int(ano) <= 2018):
                            mediaMensalParaUmAno(int(ano), arquivoDiario)
                            break
                        else:
                            print('\nDigite um número entre 1818 e 2018.\n')
                    else:
                        print('\nDigite um número entre 1818 e 2018.\n')
            else:
                break
        else:
            print('\nDigite um número entre 1 e 5.\n')


main()
