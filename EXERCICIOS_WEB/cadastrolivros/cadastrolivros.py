import os
import csv


def texto_menus(menu=str()):
    menu_principal = '''
            \n
            Menu Pincipal:

            Digite 1 para cadastrar livros.
            Digite 2 para pesquisar.
            Digite 3 para estatísticas.
            Digite 4 para sair do cadasatro.

    '''
    menu_pesquisa = '''
            \n
            Menu de Pesquisa:

            Digite 1 para pesquisar o livro pelo código.
            Digite 2 para pesquisar o livro pelo título.
            Digite 3 para voltar.
    '''

    menu_estatisca = '''
            \n
            Menu estatística:

            Digite 1 para total de livros cadastrados.
            Digite 2 para o ano do livro mais antigo
            Digite 3 para listar os idiomas disponíveis.
            Digite 4 para voltar.
    '''

    if menu == 'P':
        return print(menu_principal)
    elif menu == 'PS':
        return print(menu_pesquisa)
    else:
        return print(menu_estatisca)


def arquivo(livros_cadastrados):
    with open('CADASTROS_REGISTRADOS.csv', 'a+', encoding='utf-8') as file:
        livros = livros_cadastrados
        g = csv.writer(file)
        for i in livros:
            g.writerows([i])


def estrutura_cadastros():

    livros_cadastrados = []
    glob = True
    while glob:
        c = True
        while c:
            livro = []
            cod = input('\nDigite o codigo do livro com 2 letras e 4 números(xx1234): ')
            if len(cod) == 6:
                if cod[:1].isalpha() and cod[2:].isnumeric():
                    livro.append(cod)
                    c = False
                else:
                    print('\nDigite um código no formato 2 letras 4 números(xx1234)!\n')
                    continue
            else:
                print('\nDigite um código no formato 2 letras 4 números(xx1234)!')
                continue
        t = True
        while t:
            titulo = input('\nDigite o título do livro: ').title()
            if titulo == '':
                print('\nCampo obrigatório!!!\n')
                continue
            else:
                livro.append(titulo)
                t = False
        e = True
        while e:
            editora = input('\nDigite o nome da editora: ').title()
            if editora == '':
                print('\nCampo obrigatório!!!\n')
                continue
            else:
                livro.append(editora)
                e = False
        a = True
        while a:
            autor = input('\nDigite o nome do autor: ').title()
            if autor == '':
                print('\nCampo obrigatório!!!\n')
                continue
            else:
                livro.append(autor)
                a = False
        an = True
        while an:
            ano = input('\nDigite o ano de lançamento(AAAA): ')
            if not ano.isdigit() or len(ano) != 4:
                print('\nDigite somente números no formato AAAA\n')
                continue
            else:
                livro.append(ano)
                an = False
        i = True
        while i:
            idioma = input('\nDigite o idioma do livro: ').title()
            if idioma == '':
                print('\nCampo obrigatório!!!\n')
                continue
            else:
                livro.append(idioma)
                i = False
        n = True
        while n:
            n_paginas = input('\nDigite o número de páginas: ')
            try:
                if n_paginas.isdigit() and int(n_paginas) > 0:
                    livro.append(n_paginas)
                    n = False
                else:
                    print('\nDigite somente números inteiros maiores que zero!\n')
                    continue
            except TypeError:
                print('\nDigite somente números inteiros maiores que zero!\n')
                continue
        ss = True
        while ss:
            op = input('\nDeseja guardar esse registro? S/N: ').upper()
            if op[0] == 'S':
                livros_cadastrados.append(livro)
                arquivo(livros_cadastrados)
                livros_cadastrados = []
                print('\nLivro cadastrado e arquivado com sucesso!\n')
                ss = False
            else:
                print('\nRegistro não cadastrado!!!\n')
                ss = False

        saida = input('\nDeseja cadastrar outro livro? S/N: ').upper()
        if saida != '':
            if saida[0] == 'S':
                continue
            else:
                glob = False


def estrutura_pesquisa(opcao):
    with open('CADASTROS_REGISTRADOS.csv', 'r', encoding='utf-8') as file:
        arquivados = [a.split(',') for a in file.readlines()]

        if opcao == 1:
            c = True
            while c:
                codigo = ''
                cod = input('\nDigite o codigo do livro com 2 letras e 4 números(xx1234): ')
                if len(cod) == 6:
                    if cod[:1].isalpha() and cod[2:].isnumeric():
                        codigo = cod
                        c = False
                    else:
                        print('\nDigite um código no formato 2 letras 4 números(xx1234)!\n')
                        continue
                else:
                    print('\nDigite um código no formato 2 letras 4 números(xx1234)!')
                    continue

                codigos_arquivados = []
                for livro in arquivados:
                    if livro[0] == codigo:
                        codigos_arquivados.append(livro[0])
                        print(f'''
                        Código: {livro[0]}
                        Titulo: {livro[1]}
                        Editora: {livro[2]}
                        Autor: {livro[3]}
                        Ano de lançamento: {livro[4]}
                        Idioma: {livro[5]}
                        Número de páginas: {livro[6][:-1]}''')

                if codigo not in codigos_arquivados:
                    print('\nCodigo não cadastrado!\n')
            return True

        if opcao == 2:
            op = True
            while op:
                tit = input('\nDigite o título ou uma palavra chave: ').title()
                if tit == '':
                    print('\nDigite o título ou uma palavra chave:\n ')
                    continue
                else:
                    op = False
            tits = []
            for livro in arquivados:
                if tit in livro[1]:
                    tits.append(livro[1].split(' '))
                    print(f'''
                        Código: {livro[0]}
                        Titulo: {livro[1]}
                        Editora: {livro[2]}
                        Autor: {livro[3]}
                        Ano de lançamento: {livro[4]}
                        Idioma: {livro[5]}
                        Número de páginas: {livro[6][:-1]}''')
            if len(tits) == 0:
                print('\nTítulo ou palavra não encontrada!\n')
            return True


def estrutura_estatistica(opcao):
    with open('CADASTROS_REGISTRADOS.csv', 'r', encoding='utf-8') as file:
        cadastrados = [livros for livros in file.readlines()]
        if opcao == 1:
            n_livros = len(cadastrados)
            print(f'\nExistem {n_livros} livros cadastrados na biblioteca.\n')
            return True
        elif opcao == 2:
            livros = [a.split(',') for a in cadastrados]
            ano = [int(a[4]) for a in livros]
            mais_antigo = min(ano)
            print(f'\nO livro mais antigo da biblioteca foi escrito no ano de {mais_antigo}.\n')
            return True
        else:
            livros = [a.split(',') for a in cadastrados]
            idioma = set()
            for a in livros:
                idioma.add(a[5])
            print(f'\nOs idiomas cadastrasdos são: {idioma} ')
            return True


def main():
    if os.path.isfile("CADASTROS_REGISTRADOS.csv"):
        print('\nA base de dados já existe no arquivo "CADASTROS_REGISTRADOS.csv".\n')
    else:
        with open('CADASTROS_REGISTRADOS.csv', 'w', encoding='utf-8') as file:
            f = csv.writer(file)
            f.writerows([])

    m = True
    while m:
        o = True
        while o:
            texto_menus(menu='P')
            op = input('\nDigite a opção desejada: ')
            if op.isdigit():
                op = int(op)
                if 1 <= op <= 4:
                    if op == 1:
                        estrutura_cadastros()
                        o = False
                    elif op == 2:
                        op1 = True
                        while op1:
                            texto_menus(menu='PS')
                            op2 = input('\nDigite a opção desejada: ')
                            if op2.isdigit():
                                op2 = int(op2)
                                if 1 <= op2 <= 3:
                                    if op2 == 1:
                                        op1 = estrutura_pesquisa(op2)
                                    elif op2 == 2:
                                        op1 = estrutura_pesquisa(op2)
                                    else:
                                        op1 = False
                                        o = True
                                else:
                                    print('\nDigite um número entre 1 e 3.\n')
                                    op1 = True
                                    continue
                    elif op == 3:
                        op3 = True
                        while op3:
                            texto_menus(menu='E')
                            op4 = input('\nDigite a opção desejada: ')
                            if op4.isdigit():
                                op4 = int(op4)
                                if 1 <= op4 <= 4:
                                    if op4 == 1:
                                        op3 = estrutura_estatistica(op4)
                                    elif op4 == 2:
                                        op3 = estrutura_estatistica(op4)
                                    elif op4 == 3:
                                        op3 = estrutura_estatistica(op4)
                                    else:
                                        op3 = False
                                else:
                                    print('\nDigite um número entre 1 e 4.\n')
                                    op3 = True
                                    continue
                    else:
                        o = False
                        m = False
                        print('\nAté a próxima!!!\n')
                else:
                    print('\nDigite um número entre 1 e 4.\n')

            else:
                print('\nDigite um número entre 1 e 4\n')
                continue


main()
