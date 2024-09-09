print('-=-' * 50)
print('''Exercício Python 102:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.''')
print('-=-' * 50)


def fatoral(n=0, show=False):
    """
    docstrings
    => Calcular o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: True para Mostrar o calculo, False para não mostrar o calculo.
    :return: valor do fatural de um número
    """

    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(f'{i}', end='')
            if i == 1:
                print(' = ', end='')
                break
            else:
                print(' x ', end='')
    return f


help(fatoral)
n = int(input('Digite um número: '))
while True:
    s = False
    opcao = str(input('Deseja mostrar o calculo (S/N)')).upper().strip()[0]
    if opcao in 'SN':
        if opcao in 'S':
            s = True
        break
    else:
        print('Opção invalida')
print(fatoral(n, s))
