print('-=-' * 50)
print('''Exercício Python 097: 
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~''')
print('-=-' * 50)


def titulo(txt):
    vtam = len(txt) + 4
    print('~' * vtam)
    print(f'  {txt}')
    print('~' * vtam)


titulo('Olá, mundo!')
titulo('A copa do mundo é nossa')
titulo('Oi')
titulo('1')
titulo('1000')
