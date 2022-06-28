'''
Sistema de perguntas e respostas
'''
print('Questionario de multipla escolha. Escolha a alternativa correta.\n')

perguntas = {
    '1ª pregunta': {
        'pergunta': 'Qual é o diminutivo de panela ?',
        'resposta': {'a)': 'Janelinha', 'b)': 'Gamelinha', 'c)': 'Panelinha'},
        'resposta_certa': 'c',
    },
    '2ª pregunta': {
        'pergunta': 'Qual é o aumentativo de pau ?',
        'resposta': {'a)': 'Cacetinho', 'b)': 'Pauzinho', 'c)': 'Piruzinho'},
        'resposta_certa': 'b',
    },
    '3ª pregunta': {
        'pergunta': 'Qual é o diminutivo de grelo ?',
        'resposta': {'a)': 'Grelinho', 'b)': 'Dentinho de alho', 'c)': 'Chuveirinho'},
        'resposta_certa': 'a',
    },
    '4ª pregunta': {
        'pergunta': 'Qual é o sucessor de ontem ?',
        'resposta': {'a)': 'Amanhã', 'b)': 'Hoje', 'c)': 'Semana que vem'},
        'resposta_certa': 'b',
    },
    '5ª pregunta': {
        'pergunta': 'Qual é o antecessor de 9 ?',
        'resposta': {'a)': '14', 'b)': '45', 'c)': '8'},
        'resposta_certa': 'c',
    },
}
cont = 0
for kp, vp in perguntas.items():
    print(f'{kp}: {vp["pergunta"]}\n')
    for kr, vr in vp["resposta"].items():
        print(f'{kr} : {vr}')
    
    resposta = input('\nQual a resposta correta? ')

    if resposta == vp['resposta_certa']:
        print('\nVocê acertou.\n')
        cont += 1
    else:
        print('\nResposta incorreta!\n')

percentual = cont * 100 / round(len(perguntas), 2)
print(f'Você acertou {cont} questões, num total de {percentual}%.')