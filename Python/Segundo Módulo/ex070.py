print('-=-'*50)
print('''Exercício Python 70: 
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.''')
print('-=-'*50)

from time import sleep

vCont = vTotal = vMenor = vCaro = 0
vProdutoMenor = ''

while True:
    print(f'\n{' Cadastro de compra ':$^28}')
    vProduto = str(input('Digite no nome do produto: ')).strip()
    vValor = float(input('Digite o valor do produto: '))
    vCont += 1
    vTotal += vValor
    if vValor > 1000:
        vCaro += 1
    if vCont == 1:
        vMenor = vValor
        vProdutoMenor = vProduto
    elif vMenor > vValor:
         vMenor = vValor
         vProdutoMenor = vProduto
    vOpcao = ' '
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja cadastrar mais um produto? [S/N] ')).upper().strip()[0]

    if vOpcao == 'N':
        print('\nFechando a venda...')
        sleep(1)
        print('Analisando...')
        sleep(1)
        break
print(f'\nForam vendidos {vCont} produtos.')
print(f'O total gasto na compra foi  R${vTotal:.2f}.')
print(f'{vCaro} produtos custam mais de R$1000.')
print(f'{vProdutoMenor} foi o produto mais barato.')