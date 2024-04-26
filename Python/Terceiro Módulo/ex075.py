print('-=-' * 50)
print('''Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.''')
print('-=-' * 50)

vNumero = (int(input('Digite um númeno: ')), int(input('Digite um númeno: ')),
           int(input('Digite um númeno: ')), int(input('Digite um númeno: ')))
print(vNumero)
print(f'O número 9 foi digitado {vNumero.count(9)} vezes')
if 3 in vNumero:
    print(f'O primeiro 3 está na posição {vNumero.index(3)+1}')
else:
    print(f'O primeiro 3 não foi digitado!')
print('Os valores pares foram ', end='')
for i in vNumero:
    if i % 2 == 0:
        print(i, end=' ')
