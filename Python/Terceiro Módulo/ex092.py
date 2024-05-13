print('-=-' * 50)
print('''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.''')
print('-=-' * 50)

from datetime import datetime

vCadastro = {}
vAnoAtual = datetime.now().year

vCadastro['nome'] = str(input('Digite o nome: '))
vAnoNasc = int(input('Digite o ano de nascimento: '))
vCadastro['idade'] = vAnoAtual - vAnoNasc
vCadastro['ctps'] = int(input('Cateira de Trabalho (0 não tem: '))
if vCadastro['ctps'] != 0:
    vCadastro['ano'] = int(input('Ano de contratação: '))
    vCadastro['salario'] = float(input('Salário: R$'))
    vCadastro['tempo'] = vAnoAtual - vCadastro['ano']
    vCadastro['aposentar'] = vCadastro['idade'] + ((vCadastro['ano'] + 35) - vAnoAtual)
print('  ==> Cadastro Funcionário <==')
for k, v in vCadastro.items():
    print(f'  --> {k} = {v}')
