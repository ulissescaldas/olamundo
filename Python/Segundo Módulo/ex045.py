print('-=-'*50)
print('-=-'*50)

import time
from random import randint

vItens = ('PEDRA','PAPEL','TESOURA')
vComputador = randint(0,2)
print('''SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
vJogador = int(input('Qual é a sua opção? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print('-<>-'*7)
print('O computador escolheu {}'.format(vItens[vComputador]))
print('Você escolheu {}'.format(vItens[vJogador]))
print('-<>-'*7)
if vComputador == 0: #computador jogou Pedra
    if vJogador ==0:
        print('EMPATE')
    elif vJogador ==1:
        print('JOGADOR VENCE')
    elif vJogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('Joganda Invalida!')
elif vComputador == 1: #computador jogou Papel
    if vJogador ==0:
        print('COMPUTADOR VENCE')
    elif vJogador ==1:
        print('EMPATE')
    elif vJogador ==2:
        print('JOGADOR VENCE')
    else:
        print('Joganda Invalida!')
elif vComputador ==2: #computador jogou Tesoura
    if vJogador ==0:
        print('JOGADOR VENCE')
    elif vJogador ==1:
        print('COMPUTADOR VENCE')
    elif vJogador ==2:
        print('EMPATE')
    else:
        print('Joganda Invalida!')
else:
    print('Opção Invalida')