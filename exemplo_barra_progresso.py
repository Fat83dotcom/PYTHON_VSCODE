# from tqdm import tqdm
# from time import sleep
import os

# for i in tqdm(range(200)):
#     sleep(0.5)

# with tqdm(total=60) as barra:
#     cont = 0
#     while cont < 60:
#         sleep(1)
#         barra.update(1)
#         cont += 1
print(os.path.dirname(os.path.realpath(__file__)))  # obter o caminho da pasta
