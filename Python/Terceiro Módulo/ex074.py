print('-=-' * 50)
print('''Exercício Python 074:
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.''')
print('-=-' * 50)

from random import randint

vNumero = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Números: {vNumero}')
print(f'Maior: {max(vNumero)}')
print(f'Menor: {min(vNumero)}')
