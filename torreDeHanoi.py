
def hanoiRecursiva(disco, t_Origem, t_Destino, t_Auxiliar):
    if disco == 1:
        print(f'Mova o disco {disco} da torre {t_Origem} para a torre {t_Destino}')
        return
    hanoiRecursiva(disco - 1, t_Origem, t_Auxiliar, t_Destino)
    print(f'Mova o disco {disco} da torre {t_Origem} para a torre {t_Destino}')
    hanoiRecursiva(disco - 1, t_Auxiliar, t_Destino, t_Origem)


def defineDisco(qtdMovimento) -> int():
    discoDaVez = 0
    qtdMovimentoInterna = qtdMovimento
    if qtdMovimento:
        while (qtdMovimentoInterna & 1) == 0:
            qtdMovimentoInterna = qtdMovimentoInterna >> 1
            discoDaVez += 1
    return discoDaVez


def movimentoDeDisco(qtdMovimento, origem, destino, disco) -> None:
    if disco & 1:
        torre = ['A', 'B', 'C']
    else:
        torre = ['A', 'C', 'B']

    print(f'Mova o disco {defineDisco(qtdMovimento) + 1} da torre'
          f' {torre[origem]} para a torre {torre[destino]}')


def hanoiIterativa(disco) -> None:
    qtdMovimento = 1
    while qtdMovimento < (1 << disco):
        torre_O = (qtdMovimento & (qtdMovimento - 1)) % 3
        torre_D = ((qtdMovimento | (qtdMovimento - 1)) + 1) % 3
        movimentoDeDisco(qtdMovimento, torre_O, torre_D, disco)
        qtdMovimento += 1


def main() -> None:
    nDiscos = int(input('Quantos discos deseja empilhar? '))
    print('\nRecursiva')
    hanoiRecursiva(nDiscos, 'A', 'C', 'B')
    print('\nIterativa')
    hanoiIterativa(nDiscos)


main()
