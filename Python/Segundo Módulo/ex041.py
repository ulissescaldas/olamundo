print('-=-'*50)
print('''Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER''')
print('-=-'*50)

import datetime

vAnoNasc = int(input('Digite o ano de nascimento: '))
vAnoAtual = int(datetime.date.today().year)
vIdade = vAnoAtual - vAnoNasc
if vIdade <= 9:
    print('Você tem {} e é MIRIM'.format(vIdade))
elif vIdade <= 14:
    print('Você tem {} e é INFANTIL'.format(vIdade))
elif vIdade <= 19:
    print('Você tem {} e é JÚNIOR'.format(vIdade))
elif vIdade <= 25:
    print('Você tem {} e é SÊNIOR'.format(vIdade))
else:
    print('Você tem {} e é MASTER'.format(vIdade))