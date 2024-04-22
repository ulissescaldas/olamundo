print('-=-'*50)
print('''Exercício Python 66: 
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).''')
print('-=-'*50)

vNumero = vSoma = vCont = 0
while True:
    vNumero = int(input('Digite um número para somar ou 999 para sair: '))
    if vNumero == 999:
        break
    vSoma += vNumero
    vCont += 1
print(f'Você digitou {vCont} números e a soma é {vSoma}')
