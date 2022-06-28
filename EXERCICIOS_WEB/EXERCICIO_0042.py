'''Leia	do usuário o tempo em segundos e o escreva em horas, minutos e	segundos.
Utilize	cinco métodos:	para a	leitura e escrita de dados e para obtenção de horas,	
minutos	e segundos a partir do tempo em	segundos.	
'''

class FuncoesHorarias:

    def converte_hora(self, segundos):
        return segundos // 3600

    def converte_minutos(self, segundos):
        return segundos // 60


class ConversorHorario(FuncoesHorarias):
    def __init__(self) -> None:
        self.horas = None
        self.minutos = None
        self.segundos = None

    def leitura_segundos(self):
        while True:
            try:
                self.segundos = int(input('Digite o tempo em segundos: '))
                break
            except ValueError as erro:
                print(erro)

    def mostra_resultado(self):
        if self.segundos != None:
            entrada_segundos = self.segundos
            self.horas = self.converte_hora(self.segundos)
            self.segundos = self.segundos - (self.horas * 3600)
            self.minutos = self.converte_minutos(self.segundos)
            self.segundos = self.segundos - (self.minutos * 60)
            print(f'{entrada_segundos} segundos equivalem à: {self.horas} horas, {self.minutos} minutos e {self.segundos} segundos.')
        else:
            print('O método leitura_segundos não foi chamado!')
            self.leitura_segundos()
            self.mostra_resultado()


t1 = ConversorHorario()
# t1.leitura_usuario()
t1.mostra_resultado()
