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