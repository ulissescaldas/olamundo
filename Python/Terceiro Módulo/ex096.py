print('-=-' * 50)
print('''Exercício Python 096: 
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
 (largura e comprimento) e mostre a área do terreno.''')
print('-=-' * 50)


def area(lar, com):
    a = lar * com
    print(f'A área de {lar}x{com} é de {a}m².')


print('  Contorle de Terreno')
print('-'*23)
vLargura = float(input('Digite a largura (m): '))
vComprimento = float(input('Digite o comprimento (m): '))
area(vLargura, vComprimento)
