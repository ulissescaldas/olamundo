from time import sleep

print('-=-' * 50)
print('''Exercício Python 098: 
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada''')
print('-=-' * 50)


def contador(inicio, fim, passo):
    if inicio <= fim:
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            sleep(0.3)
        print()
    else:
        for i in range(fim, inicio, passo):
            print(i, end=' ')
            sleep(0.3)
        print()


print('\nA) de 1 até 10, de 1 em 1')
contador(1, 11, 1)
print('\nB) de 10 até 0, de 2 em 2 ')
contador(0, 11, 2)
print('\nC) uma contagem personalizada')
ci = int(input('Digite o Início: '))
cf = int(input('Digite o Fim:    '))
cp = int(input('Digite o Passo:  '))
if ci <= cf:
    cf += 1
else:
    ci += 1
if cp < 0:
    cp *= -1
if cp == 0:
    cp = 1
contador(ci, cf, cp)
