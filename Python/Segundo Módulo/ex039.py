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