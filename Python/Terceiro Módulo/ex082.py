print('-=-' * 50)
print('''Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.''')
print('-=-' * 50)

vLista = []
vPares = []
vImpar = []
vOpcao = ' '

while True:
    vOpcao = ' '
    vLista.append(int(input('\nDigite um número: ')))
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if vOpcao in 'N':
        break
for i in vLista:
    if i % 2 == 0:
        vPares.append(i)
    else:
        vImpar.append(i)
print(f'\nOs números digitados foram {vLista}.')
print(f'Os números pares foram {vPares}.')
print(f'Os números ímpares foram {vImpar}.')
