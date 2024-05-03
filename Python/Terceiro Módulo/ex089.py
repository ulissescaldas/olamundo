print('-=-' * 50)
print('''Exercício Python 089: 
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.''')
print('-=-' * 50)

vAluno = []
vLista = []
vMedia = 0
while True:
    vOpcao = ' '
    vAluno.append(str(input('\nDigite o Nome: ')).strip())
    vAluno.append(float(input('Digite a nota 1: ')))
    vAluno.append(float(input('Digite a nota 2: ')))
    vLista.append(vAluno[:])
    vAluno.clear()
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if vOpcao in 'N':
        break
print('='*27)
print('No.  Nome             Média')
print('-'*27)
for i, v in enumerate(vLista):
    vMedia = (vLista[i][1] + vLista[i][2])/2
    print(f'{i:<5}{vLista[i][0]:<17}{vMedia:>5}')
print('-' * 27)
while True:
    vOpcao = int(input('\nDeseja ver as notas de qual aluno ou 999 para sair: '))
    if vOpcao == 999:
        print('\nSistema Finalizado!')
        break
    vMedia = (vLista[vOpcao][1] + vLista[vOpcao][2])/2
    print(f'As notas de {vLista[vOpcao][0]} foram [{vLista[vOpcao][1]} e {vLista[vOpcao][2]}] e a média foi {vMedia}')


