'''
-> Uma classe pode se relacionar com outras classes.
-> As classes são independentes, elas não dependem uma da outra.
'''
from classes import Escritor, Caneta, MaquinaEscrever

escritor = Escritor('mané')
caneta = Caneta('Bic')
maquina = MaquinaEscrever('Garret')

caneta.escreve()

escritor.ferramenta = caneta
escritor.ferramenta.escreve()
caneta.marca = 'Pilot'
escritor.ferramenta.escreve()
escritor.ferramenta = maquina
escritor.ferramenta.escreve()
maquina.marca = 'Singer'
escritor.ferramenta.escreve()
