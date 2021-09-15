'''
Classe para converter segundos no formato h:m:s
'''


class ConvertSec():
    def __init__(self, sec):
        self.sec = sec

    def convert_sec(self):
        hora = minuto = segundo = 0
        self.sec = int(self.sec)
        if self.sec >= 3600:
            hora = self.sec // 3600
            self.sec = self.sec - (3600 * hora)
            minuto = self.sec // 60
            self.sec = self.sec - (60 * minuto)
            segundo = self.sec
        elif 60 <= self.sec < 3600:
            minuto = self.sec // 60
            self.sec = self.sec - (60 * minuto)
            segundo = self.sec
        else:
            segundo = self.sec
        return str(f'{str(hora).zfill(2)}hs : {str(minuto).zfill(2)}min : {str(segundo).zfill(2)}seg')


if __name__ == "__main__":
    pass
