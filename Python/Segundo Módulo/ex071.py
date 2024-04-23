print('-=-'*50)
print('''Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.''')
print('-=-'*50)

from time import sleep
vContNotas= 0
while True:
    print(f'\n{' Caixa Eletrônico ':$^32}')
    vSaque = int(input('Digite o valor do saque: '))
    if vSaque >= 50:
        vContNotas = vSaque // 50
        vSaque = vSaque % 50
        print(f'{vContNotas} cédulas de R$50.00')
    if vSaque >= 20:
        vContNotas = vSaque // 20
        vSaque = vSaque % 20
        print(f'{vContNotas} cédulas de R$20.00')
    if vSaque >= 10:
        vContNotas = vSaque // 10
        vSaque = vSaque % 10
        print(f'{vContNotas} cédulas de R$10.00')
    if vSaque >= 1:
        vContNotas = vSaque // 1
        print(f'{vContNotas} cédulas de R$1.00')
    break
print('Retire as notas...')
sleep(1)
print('Saque finalizado.')
sleep(1)

print('-=-'*50)
print(f'\n{' Caixa Eletrônico CEV ':$^32}')
vSaque = int(input('Digite o valor do saque: '))
vNota = 50
vContNotas = 0
while True:
    if vSaque >= vNota:
        vSaque -= vNota
        vContNotas += 1
    else:
        if vContNotas > 0:
            print(f'{vContNotas} cédulas de R${vNota:.2f}')
        vContNotas = 0
        if vNota == 50:
            vNota = 20
        elif vNota == 20:
            vNota = 10
        elif vNota == 10:
            vNota = 1
        else:
            break
print('Retire as notas...')
sleep(1)
print('Saque finalizado.')