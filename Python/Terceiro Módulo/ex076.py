print('-=-' * 50)
print('''Exercício Python 076: 
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.''')
print('-=-' * 50)

vLista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Mochila', 250)

print(f'{'Lista de Preço':^40}')
print('='*40)
for i in range(0, len(vLista)):
    if i % 2 == 0:
        print(f'{vLista[i]:.<30}', end='')
    else:
        print(f'R$ {vLista[i]:>6.2f}')
print('='*40)
