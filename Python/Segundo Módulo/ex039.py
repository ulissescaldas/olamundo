print('-=-'*50)
print('''Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.''')
print('-=-'*50)

import datetime

vAnoNasc = int(input('Digite o ANO de nascimento: '))
vAnoAtual = datetime.date.today().year
vIdade = vAnoAtual - vAnoNasc
print('Quem nasceu em {} tem {} anos em {}'.format(vAnoNasc, vIdade, vAnoAtual))
if vIdade < 18:
    print('Ainda faltam {} para se alistamento.'.format(18-vIdade))
    print('Seu alistamento será em {}'.format(vAnoNasc + 18))
elif vIdade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(vIdade-18))
    print('Seu alisamento foi em {}'.format(vAnoNasc + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')