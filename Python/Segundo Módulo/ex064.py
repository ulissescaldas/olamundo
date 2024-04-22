print('-=-'*50)
print('''Exercício Python 64:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).''')
print('-=-'*50)
vSair = 0
vSoma = 0
vCont = -1
while vSair != 999:
    vSoma += vSair
    vCont += 1
    vSair = int(input('Digite um número para somar ou 999 para sair: '))
print('Você digitou {} números e a soma é {}'.format(vCont,vSoma))
