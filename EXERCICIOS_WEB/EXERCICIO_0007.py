"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o
dobro desta área para o usuário.
"""
lado = ''
while not lado.isnumeric():
    lado = input("Digite o lado do quadrado em cm: ")
    if '.' in lado:
        try:
            float(lado)
            break
        except ValueError:
            print('Digite somente números e pontos.')
            continue
    if not lado.isnumeric():
        print('Digite um número.')
area = float(lado) * float(lado)
double_area = area * 2
print(
    f'A área do quadrado é{area:.2f}cm² e seu dobro é {double_area:.2f} cm².')
