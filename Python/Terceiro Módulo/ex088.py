print('-=-' * 50)
print('''Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.''')
print('-=-' * 50)

from random import randint
from time import sleep

vJogos = []
vLista = []
vNumero = vCont = 0
print('-=-'*11)
print(f'{'JOGOS DA MEGA SENA':^30}')
print('-=-'*11)
vVezes = int(input('Quantos jogos deseja criar? '))
print(f'-=-=-=- Sorteando {vVezes} Jogos -=--=-')
for i in range(0, vVezes):
    while vCont != 6:
        vNumero = randint(1, 60)
        if vNumero not in vJogos:
            vJogos.append(vNumero)
            vCont += 1
    vJogos.sort()
    vLista.append(vJogos[:])
    vJogos.clear()
    vCont = 0
for i, v in enumerate(vLista):
    print(f'Jogo {i+1:2}: {v}')
    sleep(0.5)
print('-=-'*11)
