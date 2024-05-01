print('-=-' * 50)
print('''Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.''')
print('-=-' * 50)

vLista = [[], []]
vNumero = 0
for i in range(0, 7):
    vNumero = int(input(f'Digite o {i+1}º número: '))
    if vNumero % 2 == 0:
        vLista[0].append(vNumero)
    else:
        vLista[1].append(vNumero)
vLista[0].sort()
vLista[1].sort()
print(f'Os números pares são: {vLista[0]}')
print(f'Os números ímpares são: {vLista[1]}')
