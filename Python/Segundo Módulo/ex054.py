print('-=-'*50)
print('''Exercício Python 54:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.''')
print('-=-'*50)

from datetime import date

vContMaior = 0
vContMenor = 0
for i in range(1, 8):
    vAnoNasc = int(input('Digite o {}° ano: '.format(i)))
    if (date.today().year - vAnoNasc) >= 21:
        vContMaior += 1
    else:
        vContMenor += 1
if vContMenor == 1:
    print('\nTem {} menor de 21 anos '.format(vContMenor), end='')
else:
    print('\nTem {} menores de 21 anos '.format(vContMenor), end='')
if vContMaior == 1:
    print('e {} já atigiu a maioridade '.format(vContMaior))
else:
    print('e {} já atigiram a maioridade '.format(vContMaior))
