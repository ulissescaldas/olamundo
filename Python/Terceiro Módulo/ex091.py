print('-=-' * 50)
print('''Exercício Python 091: 
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.''')
print('-=-' * 50)

from random import randint
from time import sleep
from operator import itemgetter

vJogador = dict()
vLista = list
for i in range(0, 4):
    vJogador[f'jogador{i+1}'] = randint(1, 6)
vLista = sorted(vJogador.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(vLista):
    print(f'{k+1}º lugar foi o {v[0]} tirou {v[1]} no dado')
    sleep(1)
