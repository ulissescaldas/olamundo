print('-=-' * 50)
print('''Exercício Python 078: 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.''')
print('-=-' * 50)

vNumero = []

for i in range(0, 5):
    vNumero.append(int(input(f'Digite o número da posição {i}: ')))
print(f'O valores digitados foram {vNumero}')
min = min(vNumero)
max = max(vNumero)
print(f'\nO menor valor digitado foi {min} e está na posição ', end='')
for i, v in enumerate(vNumero):
    if v == min:
        print(i, end='. ')
print(f'\nO maior valor digitado foi {max} e está na posição ', end='')
for i, v in enumerate(vNumero):
    if v == max:
        print(i, end='. ')
