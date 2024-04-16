print('-=-'*50)
print('''Exercício Python 038:
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais''')
print('-=-'*50)

vNumero1 = int(input('Digite o primeiro número: '))
vNumero2 = int(input('Digite o segundo número: '))
if vNumero1 > vNumero2:
    print('O PRIMEIRO número é maior!')
elif  vNumero2 > vNumero1:
    print('O SEGUNDO número é maior!')
else:
    print('Os dois números são IGUAIS!')