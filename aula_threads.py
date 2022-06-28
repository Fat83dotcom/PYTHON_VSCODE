from threading import Thread
import csv
from time import sleep


class TesteThread(Thread):
    def __init__(self, laco, condicao=True):
        self.cond = condicao
        self.n_v_laco = laco
        super().__init__()

    def run(self):
        with open('teste.csv', 'a+', newline='', encoding='utf-8') as file:
            w = csv.writer(file)
            for i in range(self.n_v_laco):
                if self.cond:
                    w.writerow([f'Esse número:{i}', f'elevado ao quadrado é igual a : {i ** 2}'])
                    sleep(1)
                else:
                    print('Laço terminou')
                    break
        print('terminou thread')


flag = False
cont = 60
cond = True
while not flag:
    t = TesteThread(cont, cond)
    t.start()

    flag2 = input('Deseja encerrar o programa? (S/N): ').upper()
    if flag2[0] == 'S':
        cont = 0
        cond = False
        flag = True
        break
print('terminou')
