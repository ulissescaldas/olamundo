import time
from random import randint

itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('''SUAS OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua opção? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print('-<>-'*7)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('-<>-'*7)
if computador == 0: #computador jogou Pedra
    if jogador ==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('Joganda Invalida!')
elif computador == 1: #computador jogou Papel
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCE')
    else:
        print('Joganda Invalida!')
elif computador ==2: #computador jogou Tesoura
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('Joganda Invalida!')
else:
    print('Opção Invalida')