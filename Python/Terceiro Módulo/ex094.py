print('-=-' * 50)
print('''Exercício Python 094: 
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média''')
print('-=-' * 50)

vCadastro = {}
vLista = []
vSoma = 0

while True:
    vCadastro['nome'] = str(input('\nNome: '))
    while True:
        vCadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if vCadastro['sexo'] in 'MF':
            break
        print('Opção invalida!')
    vCadastro['idade'] = int(input('Idade: '))
    vLista.append(vCadastro.copy())
    vCadastro.clear()
    while True:
        vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if vOpcao in 'SN':
            break
        print('Opção invalida!')
    if vOpcao == 'N':
        break
vTotal = len(vLista)
print(f'A) Ao total temos {vTotal} pessoas cadastradas')
for i in vLista:
    vSoma += i['idade']
vMedia = vSoma/vTotal
print(f'B) A média de idade é de {vMedia:.2f}')
print(f'C) As cadastradas foram ', end='')
for i in vLista:
    if i['sexo'] == 'F':
        print(f'{i['nome']} ', end='')
print('\nD) Lista das Pessoas que estão acima da média:')
for i in vLista:
    if i['idade'] >= vMedia:
        print(f'      Nome = {i['nome']:<15}; Sexo = {i['sexo']:<8}; Idade = {i['idade']:<8}')
print('\nPrograma Finalizado!!!')
