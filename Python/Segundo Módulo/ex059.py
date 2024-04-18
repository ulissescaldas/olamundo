print('-=-'*50)
print('''Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.''')
print('-=-'*50)

from time import sleep

vOpcao = 0
vNumero1 = int(input('Digite o primero número: '))
vNumero2 = int(input('Digite o segundo número: '))
while vOpcao != 5:
    print('''\n<><><><> O que gostaria de fazer? <><><><> 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa
    ''')
    vOpcao = int(input('Digite sua Opção: '))
    if vOpcao == 1:
        print('A soma de {} e {} = {}'.format(vNumero1, vNumero2, vNumero1 + vNumero2))
    elif vOpcao == 2:
        print('A multiplicação de {} e {} = {}'.format(vNumero1, vNumero2, vNumero1 * vNumero2))
    elif vOpcao == 3:
        print('O maior número entre {} e {} = {}'.format(vNumero1, vNumero2, max(vNumero1,vNumero2)))
    elif vOpcao == 4:
        print('\nDigite os números novamente!')
        vNumero1 = int(input('Digite o primero número: '))
        vNumero2 = int(input('Digite o segundo número: '))
    elif vOpcao == 5:
        print('\nFinalizando...')
    else:
        print('Opção inválida! tente novamente.')
    sleep(2)
print('\n<><><><> Fim do Programa! <><><><>')