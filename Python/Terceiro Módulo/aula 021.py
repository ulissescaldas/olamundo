print('Aula 21 – Funções (Parte 2)')

help(print)
help(len)
help(input)


def contador(i, f, p):
    """
    docstrings
    Faz uma contagem e mostra na tel
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por CursoEmVideo.
    Link: https://www.youtube.com/watch?v=etjJ_4Eqrk8&t=948s
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')


contador(0, 100, 10)
help(contador)

#paramentro opcional

somar()
somar(1)
somar(1, 2)
somar(1, 2, 3)


def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('\nDigite um número: '))
print(par(num))
if par(num):
    print('É par!')
else:
    print('Não é par!')

