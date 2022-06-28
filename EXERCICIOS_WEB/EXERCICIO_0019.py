'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir
o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
'''


class Tv:
    def __init__(self):
        self.volume = 0
        self.canal = {
            0: 'Grobo',
            1: 'Sbt',
            2: 'Recor',
            3: 'Band',
            4: 'CNN',
            5: 'BBC',
            6: 'FOX',
            7: '',
            8: '',
            9: '',
            10: ''
        }

    def lista_canais(self):
        print(self.canal)

    def define_canal(self, num_canal):
        if 0 <= int(num_canal) <= 10:
            a = self.canal.get(num_canal)
            if a == '':
                self.canal[num_canal] = str(input(f'Digite o nome do canal {num_canal}: '))
            else:
                flag = input(f'Canal {num_canal} ja foi definido, deseja substituir?(S/N): ').upper()
                if 'S' in flag[0]:
                    self.canal[num_canal] = str(input(f'Digite o nome do canal {num_canal}: '))
                else:
                    return
        else:
            print('Digite um canal válido, entre 0 e 10')

    def selecionar_canal(self, num_canal):
        if 0 <= int(num_canal) <= 10:
            print(f'Voce está assistido o canal : {num_canal} : {self.canal.get(num_canal)}.')
            if self.volume == 10:
                print('O volume da tv está no maximo.')
        else:
            print("Canal não correspondente.")

    def aumenta_volume(self, n_volume):
        if (int(n_volume) + self.volume) > 10:
            print('O volume está no máximo.')
            self.volume = 10
            return
        else:
            self.volume += int(n_volume)
            print(f'O volue foi definido em {self.volume}.')

    def diminuir_volume(self, n_volume):
        if (self.volume - int(n_volume)) < 0:
            print('Mute')
            self.volume = 0
            return
        else:
            self.volume -= int(n_volume)
            print(f'O volue foi definido em {self.volume}.')


f = Tv()
print()
f.lista_canais()
f.selecionar_canal(3)
f.aumenta_volume(7)
f.diminuir_volume(4)
