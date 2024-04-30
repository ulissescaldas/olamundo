print('-=-' * 50)
print('''Exercício Python 079: 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente.''')
print('-=-' * 50)
vNumero = 0
vLista = []
vOpcao = ' '

while True:
    vNumero = int(input('Digite um número: '))
    if vNumero not in vLista:
        vLista.append(vNumero)
        print('Valor adicionado...')
    else:
        print('Esse valor é repetido e não vai ser adicionado.')
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if vOpcao in 'N':
        break
    else:
        vOpcao = ' '
vLista.sort()
print(f'\nOs valores adicionado foram {vLista}')
