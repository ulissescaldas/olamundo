print('Aula 20 – Funções (Parte 1)')


def linha():
    print('-=-' * 20)


def lin(txt):
    print('-=-' * 20)
    print(txt)
    print('-=-' * 20)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} = {s}')


def somavalores(* valor):
    s = 0
    for i in valor:
        s += i
    print(f'A soma dos valores {valor} = {s}')


def somalista(lst):
    s = 0
    for i in lst:
        s += i
    print(f'A soma dos valores {lst} = {s}')


def contador(* num):
    print(num, end=' -> ')
    print(len(num))


def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont += 1


lin('Olá! mundo.')
soma(1, 5)
soma(2, 10)
linha()
contador(1, 2, 3, 4, 5)
contador(9, 8, 7)
contador(6)
linha()
valores = [1, 2, 3, 4, 5]
print(valores)
linha()
dobra(valores)
print(valores)
linha()
somavalores(1, 2, 3, 4, 5)
linha()
somalista(valores)
