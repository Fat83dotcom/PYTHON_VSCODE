#!/usr/bin/env python
# coding: utf-8
# # TRABALHO PRÁTICO A
# ### MANCHAS SOLARES
# ##### PROGRAMAÇÃO DE COMPUTADORES - PROFESSOR JOSÉ DE SIQUEIRA
# ### APRESENTAÇÃO
#   * A princípio, foi realizada uma função para ler os dados a partir dos arquivos anexados na
# proposta "Dados de entrada", com os números de observações diárias e mensais das manchas solares.
# Em seguida, armazenei-os em dicionários, para cada ano, de acordo com a sua categoria
# (diária ou mensal). Para facilitar, foi importado o módulo "sys" que fornece funções e variáveis
# usadas para manipular diferentes partes do ambiente de tempo de execução em Python.
#   * A fim de retornar as funções de teste deste trabalho é importante ressaltar que foi usado um
# número total de manchas solares diárias. O valor de -1 indica que nenhum número está disponível
# para esse dia (valor faltante), por isso, os dias em que foram computados como -1 não estão
# apresentados, nem como "sem manchas solares" e nem como "com manchas solares", ou seja, não foi
# usado para a finalidade das questões propostas. Foi empregado especificamente os valores >0 e 0.
# Sendo que, o indicador exclusivo = '0', foi utilizado para concluir os dias em que não foram
# observadas manchas solares naquele dia.
# * A seguir, explicito as funções usadas em meu script:
# * Para poder percorrer o índice/posição dos elementos da minha lista, usei a função enumerate().
# * Para ordenar as informações da minha lista empreguei a função sorted() acompanhada de um parâmetro,
# parâmetro key(chave). Isso permitiu criar a minha própria ordem de classificação, uma função
# de linha única.

# import sys


# isso aqui organiza os dados dos arquivos anexados na proposta(diário)


def format_file_1():
    with open("SN_d_tot_V2.0.txt", "r") as file:
        arr = []
        for row in file.readlines():
            data = row.split()
            arr.append(
                {
                    "year": int(data[0]),
                    "month": int(data[1]),
                    "day": int(data[2]),
                    "sunspot_daily": data[4],
                    "observations": int(data[6]),
                }
            )
        return arr


# isso aqui organiza os dados dos arquivos anexados na proposta(mensal)


def format_file_2():
    with open("SN_m_tot_V2.0.txt", "r") as file:
        arr = []
        for row in file.readlines():
            data = row.split()
            arr.append(
                {
                    "year": int(data[0]),
                    "month": int(data[1]),
                    "sunspot_monthly": data[3],
                    "observations": int(data[5]),
                }
            )

    return arr


extracaoDadosDiarios()


# isso aqui conta os dias em que nãa foram observadas manchas solares em cada mês, para um dado ano. Retornando apenas o (0).


def find_not_observed_days(year):
    df = format_file_1()
    filtered_by_year = []

    for row in df:
        if (row['year'] == year):
            filtered_by_year.append(row)

    not_observed_days = []
    for data in filtered_by_year:
        for k, v in data.items():
            if k == "month":
                not_observed_days.append(v)
            if k == "sunspot_daily":
                not_observed_days.append(v)

    mouth = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for acctualy_mouth in range(1, 13):
        sumy = 0
        for acctualy_sunspot_daily in range(len(not_observed_days)):
            if acctualy_sunspot_daily % 2 == 0 and not_observed_days[acctualy_sunspot_daily] == acctualy_mouth:
                if int(not_observed_days[acctualy_sunspot_daily + 1]) == 0:
                    sumy += 1
        print(f'{mouth[acctualy_mouth - 1]}: {sumy} dias.')


# isso aqui retorna o ano e o mês que tiveram mais dias SEM manchas solares e o else(outro) retorna o ano e o mês que tiveram mais manchas solares


def most_not_observed_by_month_and_year():
    # df = format_file_2()

    # observations_by_month = sorted(df, key=lambda d: d['observations'])

    # by_year = []
    # for i, row in enumerate(df):
    #     if (df[i - 1]['year'] != row['year']):
    #         data = {
    #             'year': row['year'],
    #             'observations': int(row['observations'])
    #         }
    #         by_year.append(data)
    #     else:
    #         by_year[-1]['observations'] = data['observations'] + int(row['observations'])

    # observations_by_year = sorted(by_year, key=lambda d: d['observations'])

    # return {
    #     'by_month': {
    #         'month': observations_by_month[-1]['month'],
    #         'year': observations_by_month[-1]['year'],
    #         'observations': observations_by_month[-1]['observations']
    #     },
    #     'by_year': {
    #         'year': observations_by_year[-1]['year'],
    #         'observations': observations_by_year[-1]['observations']
    #     }
    # }
    dados = format_file_1()
    dados_filtrados = []
    for cada_um in dados:
        for k, v in cada_um.items():
            dados_filtrados.append(v)

    anos = set()
    for ano in dados_filtrados[::5]:
        anos.add(ano)

    print(anos)

    meses = set()
    for mes in dados_filtrados[1::5]:
        meses.add(mes)
    print(meses)


# isso aqui me retorna o máximo e o mínimo de manchas solares em um período dado.


def observations_filtered_by_range(year_gt, month_gt, year_lt, month_lt):

    df = format_file_2()

    index_gt = next((index for (index, d) in enumerate(
        df) if d["year"] == year_gt and d["month"] == month_gt), None)

    filtered_gt = df[index_gt:]

    index_lt = next((index for (index, d) in enumerate(
        filtered_gt) if d["year"] == year_lt and d["month"] == month_lt), None)

    filtered_array = filtered_gt[:index_lt]

    bigger = sorted(filtered_array, key=lambda d: d['observations'])[-1]
    smaller = sorted(filtered_array, key=lambda d: d['observations'])[0]

    return {
        'bigger': maximo,
        'smaller': minimo
    }

# isso aqui me retorna a média mensal de cada mês, para um dado ano


def average_by_year(year):

    df = format_file_1()
    filtered_by_year = []

    for row in df:
        if (row['year'] == year):
            filtered_by_year.append(row)

    average = []
    for i in range(13):
        if i != 0:
            data = {
                'month': i,
                'average': 0,
            }
            for row in filtered_by_year:
                if row['month'] == i:
                    data['average'] = data['average'] + row['observations']

            data['average'] = data['average'] / 12
            average.append(data)

    return average


# print(find_not_observed_days(1953))
# observations_filtered_by_range(1889, 8, year_lt, month_lt)
# print(average_by_year(1818))
# print(most_not_observed_by_month_and_year())



