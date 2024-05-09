print('Aula 19 – Dicionários')

pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 18}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#deletar coluna
del pessoas['sexo']
#mudar valor
pessoas['nome'] = 'Xico'
#adicionar coluna
pessoas['peso'] = 78.5
pessoas['sexo'] = 'M'

for k in pessoas.keys():
    print(k)
for p in pessoas.values():
    print(p)
for k, p in pessoas.items():
    print(f'{k}: {p}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('\nUnidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

