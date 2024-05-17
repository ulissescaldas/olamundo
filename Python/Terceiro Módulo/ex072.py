print('-=-'*50)
print('''Exercício Python 72:
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.''')
print('-=-'*50)

vTupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('-=-'*10)
    while True:
        vNumero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= vNumero <= 20:
            break
        print('Número Inválido. ')
    print(f'Você digitou o número {vTupla[vNumero].upper()}.')
    vOpcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if vOpcao in 'N':
        break
print('\nPrograma finalizado.')
