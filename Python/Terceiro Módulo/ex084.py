print('-=-' * 50)
print('''Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.''')
print('-=-' * 50)

vPessoa = []
vLista = []
vMaior = vMenor = 0
while True:
    vOpcao = ' '
    vPessoa.append(str(input('\nDigite o Nome: ')).strip())
    vPessoa.append(float(input('Digite o peso: ')))
    if len(vLista) == 0:
        vMenor = vMaior = vPessoa[1]
    else:
        if vPessoa[1] < vMenor:
            vMenor = vPessoa[1]
        if vPessoa[1] > vMaior:
            vMaior = vPessoa[1]
    vLista.append(vPessoa[:])
    vPessoa.clear()
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if vOpcao in 'N':
        break
print(f'Pessoas cadastradas: {vLista}')
print(f'Total de pessoas cadastradas {len(vLista)}')
print(f'O maior pessoa foi {vMaior}kg com a pessoa: ', end='')
for i in vLista:
    if i[1] == vMaior:
        print(i[0], end=', ')
print(f'\nO menor pessoa foi {vMenor}kg com a pessoa: ', end='')
for i in vLista:
    if i[1] == vMenor:
        print(i[0], end=', ')
