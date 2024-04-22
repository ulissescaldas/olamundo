print('-=-'*50)
print('''Exercício Python 65: 
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.''')
print('-=-'*50)

vSair = ''
vNumeros = []
vSoma = 0
vCont = 0
while vSair in 'Ss':
    vNumero = int(input('Digite um número: '))
    vNumeros.append(vNumero)
    vSoma += vNumero
    vCont += 1
    vSair = input('Quer continuar? [S/N]: ').strip()[0]
vMedia = vSoma / vCont
print('Você digitou {} números e a média foi {:.2f}'.format(vCont, vMedia))
print('O menor número foi {} e o maior foi {}'.format(min(vNumeros), max(vNumeros)))
