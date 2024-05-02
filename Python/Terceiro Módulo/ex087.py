print('-=-' * 50)
print('''Exercício Python 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.''')
print('-=-' * 50)

vlista = [[], [], []]
vSomaPar = vSomaColuna = 0

for i in range(0, 3):
    for j in range(0, 3):
        vlista[i].append(int(input(f'Digite o valor para [{i}, {j}]: ')))
for i in vlista:
    print(f'[{i[0]:^5}][{i[1]:^5}][{i[2]:^5}]')
    vSomaColuna += i[2]
    for s in i:
        if s % 2 == 0:
            vSomaPar += s
print(f'A soma dos valores pares é {vSomaPar}')
print(f'A soma dos valores da coluna 3 é {vSomaColuna}')
print(f'O maior valor da linha 2 é {max(vlista[1])}')
