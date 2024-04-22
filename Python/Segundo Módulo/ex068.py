print('-=-'*50)
print('''Exercício Python 68: 
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.''')
print('-=-'*50)

from random import randint

vCont = 0

while True:
    vNumero = int(input('\nJoga seu número: '))
    vComputador = randint(0, 10)
    vSoma = vNumero + vComputador
    vOpcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {vNumero} e o computador jogou {vComputador} a soma dos números é {vSoma} e o resultado é ',end='')
    if vSoma % 2 == 0:
        print('Par')
        if vOpcao == 'P':
            print('Você GANHOU!')
        else:
            print('Você Perdeu!')
            break
    else:
        print('Ímpar')
        if vOpcao == 'I':
            print('Você GANHOU!')
        else:
            print('Você Perdeu!')
            break
    vCont += 1
if vCont == 1:
    print(f'\nVocê ganhou {vCont} vez')
else:
    print(f'\nVocê ganhou {vCont} vezes')