print('-=-' * 50)
print('''Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.''')
print('-=-' * 50)

vPalavra = ('Ulisses',
            'Joao',
            'Paralelepipedo',
            'Conceicao',
            'Borogodo',
            'Brasilia',
            'Taguatinga Norte')
print(vPalavra)
for i in vPalavra:
    print(f'\nNa palavra {i} tem as vogais: ', end='')
    for v in i:
        if v.lower() in 'aeiou':
            print(v.lower(), end=' ')