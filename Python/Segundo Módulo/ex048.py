print('-=-'*50)
print('''Exercício Python 48:
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.''')
print('-=-'*50)
vSoma = 0
vCont = 0
print('Números múltiplos de três de 1 até 500: ', end='')
for i in range(1, 501, 2):
    if i % 3 == 0:
        vSoma += i
        vCont += 1
        print(i, end=' ')

print('\nTemos {} números. \nO Valor Total é {}.'.format(vCont, vSoma))
