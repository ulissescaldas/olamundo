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