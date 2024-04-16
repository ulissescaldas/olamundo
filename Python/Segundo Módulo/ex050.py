print('-=-'*50)
print('''Exercício Python 50: 
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.''')
print('-=-'*50)
vSoma = 0
vAcumulador = []
for i in range(1, 7):
    vNumero = int(input('Digite o número {}: '.format(i)))
    if vNumero % 2 == 0:
        vSoma += vNumero
        vAcumulador.append(vNumero)
if vSoma == 0:
    print('Nenhum número par foi digitado')
else:
    print('Números pares: {} '.format(vAcumulador))
    print('A soma dos números pares é {}'.format(vSoma))

