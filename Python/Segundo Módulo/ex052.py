print('-=-'*50)
print('''Exercício Python 52: 
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.''')
print('-=-'*50)
vCont = 0
vNumero = int(input('Digite um número: '))
for i in range(1, vNumero+1):
    if vNumero % i == 0:
        print('\033[33m{}\033[m'.format(i), end=' ')
        vCont += 1
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
print('\nNúmero {} foi divisível {} vezes'.format(vNumero, vCont))
if vCont == 2:
    print('Número {} É Primo'.format(vNumero))
else:
    print('Número {} NÃO é Primo'.format(vNumero))
