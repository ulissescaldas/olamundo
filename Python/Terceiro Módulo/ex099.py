from random import randint
from time import sleep

print('-=-' * 50)
print('''Exercício Python 099: 
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.''')
print('-=-' * 50)


def maior(lst):
    if len(lst) == 0:
        vmaior = 0
    else:
        vmaior = max(lst)
    print('\nAnalisando os valores...')
    sleep(1)
    print(f'Foram informados {len(lst)} valores: ', end='')
    for v in lst:
        sleep(0.5)
        print(v, end=' ')
    sleep(1)
    print(f'\nO maior valor foi {vmaior}')


vLista = []
vOpcao = int(input('Quantos números deseja analisar (0 a 9)? '))
if vOpcao > 9:
    vOpcao = 9
for i in range(0, vOpcao):
    vLista.append(randint(0, 9))
maior(vLista)
