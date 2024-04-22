print('-=-'*50)
print('''Exercício Python 63:
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8''')
print('-=-'*50)
vNumero1 = int(input('Digite um número '))
vNumero2 = 0
vNumero3 = 1
vCont = 3
print('{} -> {}'.format(vNumero2, vNumero3), end='')
while vCont <= vNumero1:
    vNumero4 = vNumero2 + vNumero3
    print(' -> {}'.format(vNumero4), end='')
    vCont += 1
    vNumero2 = vNumero3
    vNumero3 = vNumero4
print(' -> Acabou.')