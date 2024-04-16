print('-=-'*50)
print('''Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO''')
print('-=-'*50)

vNota1 = float(input('Digite o valor da primeira nota: '))
vNota2 = float(input('Digite o valor da segunda nota: '))
vMedia = (vNota1 + vNota2) / 2
print('A média entre {:.1f} e {:.1f} = {:.1f}'.format(vNota1, vNota2, vMedia))
if 7 > vMedia >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif vMedia < 5:
    print('O aluno está REPROVADO!')
elif vMedia >= 7:
    print('O aluno está APROVADO!')