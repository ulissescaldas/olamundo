from random import randint

print('-=-' * 50)
print('''Exercício Python 100:
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.''')
print('-=-' * 50)


def sorteia(lst):
    count = 0
    while count != 5:
        num = randint(0, 9)
        if lst.count(num) == 0:
            lst.append(num)
            count += 1
    return lst


def somapar(lst):
    vsoma = 0
    for i in lst:
        if i % 2 == 0:
            vsoma += i
    return vsoma


vNumero = []

print(f'Foram sorteado 5 número para a análise: {sorteia(vNumero)}')
print(f'Somando os valores pares da lista {vNumero} é {somapar(vNumero)}')