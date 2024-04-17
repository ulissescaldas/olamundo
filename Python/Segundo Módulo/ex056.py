print('-=-'*50)
print('''Exercício Python 56:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: 
- a média de idade do grupo;
- qual é o nome do homem mais velho;
- quantas mulheres têm menos de 20 anos.''')
print('-=-'*50)

vMedia = 0
vSomaIdade = 0
vCont = 0
vMaior = 0
vContMulher = 0
vNomeMaior = ''

for i in range(1, 5):
    print('\n{}ª Pessoa'.format(i))
    vNome = str(input('Digite o nome: ').strip())
    vIdade = int(input('Digite a idade: '))
    vSexo = str(input('Digite o sexo [M/F]: ').strip().upper())
    vSomaIdade += vIdade
    vCont += 1
    if vSexo == 'M' and i == 1:
        vMaior = vIdade
        vNomeMaior = vNome
    if vSexo == 'M' and vMaior < vIdade:
         vMaior = vIdade
         vNomeMaior = vNome
    if vSexo == 'F' and vIdade <= 35:
        vContMulher += 1

vMedia = vSomaIdade/vCont
print('A média de idade do grupo é {:.1f}'.format(vMedia))
print('O nome do homem mais velho é {} e tem {} anos'.format(vNomeMaior, vMaior))
print('{} mulheres têm menos de 35 anos'.format(vContMulher))