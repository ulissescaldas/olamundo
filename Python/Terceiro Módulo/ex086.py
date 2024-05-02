print('-=-' * 50)
print('''Exercício Python 086: 
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.''')
print('-=-' * 50)

vlista = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        vlista[i].append(int(input(f'Digite o valor para [{i}, {j}]: ')))
for i in vlista:
    print(f'[{i[0]:^5}][{i[1]:^5}][{i[2]:^5}]')
