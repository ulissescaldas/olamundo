print('-=-'*50)
print('''Exercício Python 69: 
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.''')
print('-=-'*50)

from time import sleep

vCont = vMaior18 = vHomem = vMulher = 0

while True:
    vOpcao = ' '
    vSexo = ' '
    vCont += 1
    print(f'\n{' Cadastre uma pessoa ':+^30}')
    vIdade = int(input('Idade: '))
    while vSexo not in 'MF':
        vSexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    print(f'{vIdade}{vSexo}')
    while vOpcao not in 'SN':
        vOpcao = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    if vIdade >= 18:
        vMaior18 += 1
    if vSexo == 'M':
        vHomem += 1
    if vSexo == 'F' and vIdade < 20:
        vMulher += 1
    if vOpcao == 'N':
        print('Gravando Cadastro...')
        sleep(1)
        print('Analizando os dados...')
        sleep(1)
        break
print(f'Foram cadastrados {vCont} pessoas \n{vMaior18} é maior de 18 anos \n{vHomem} homens foram cadastrados \n{vMulher} mulheres tem menos de 20 anos.')