print('-=-'*37)
print(' Calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.')
print('-=-'*37)
vSoma = 0
vCont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        vSoma += i
        vCont += 1
        print(i, end=' ')

print('\nTemos {} números. \nO Valor Total é {}.'.format(vCont, vSoma))
