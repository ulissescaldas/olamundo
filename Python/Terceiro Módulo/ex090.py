print('-=-' * 50)
print('''Exercício Python 090: 
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.''')
print('-=-' * 50)

vAluno = dict()
vAluno['nome'] = str(input('Digite o nome: '))
vAluno['media'] = float(input('Média: '))
if vAluno['media'] < 4:
    vAluno['situacao'] = 'Rerovado'
elif vAluno['media'] < 6:
    vAluno['situacao'] = 'Recuperação'
else:
    vAluno['situacao'] = 'Aprovado'
print('='*20)
for k, v in vAluno.items():
    print(f'- {k} é igual {v}')
