print('-=-'*50)
print('''Exercício Python 67:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.''')
print('-=-'*50)
print(f'{' Tabuada de Multiplicação ':=^40}')
while True:
    vNumero = int(input('\nDigite um número positivo ver a sua tabuada ou um número negativo para sair do programa: '))
    if vNumero < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{vNumero} x {i:2} = {vNumero * i}')
print('\nPrograma encerrado!')