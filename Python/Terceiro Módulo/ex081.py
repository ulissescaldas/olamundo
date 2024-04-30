print('-=-' * 50)
print('''Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.''')
print('-=-' * 50)

vLista = []
while True:
    vOpcao = ' '
    vLista.append(int(input('\nDigite um número: ')))
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if vOpcao in 'N':
        break
vLista.sort(reverse=True)
print(f'\nForam digitado {len(vLista)} números.')
print(f'Os números digitados foram {vLista}')
if 5 in vLista:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 NÃO faz parte da lista')
