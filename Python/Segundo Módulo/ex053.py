print('-=-'*50)
print('''Exercício Python 53:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
desconsiderando os espaços. Exemplos de palíndromos:''')
print('-=-'*50)

vFrase = str(input('Digite uma frase: ')).strip().upper()
vFraseSemEspaco = ''.join(vFrase.split())
vFraseInversa = vFraseSemEspaco[::-1]
print('Frase digitada: {}'.format(vFrase))
print('Frase sem espaço: {}'.format(vFraseSemEspaco))
print('Frase inversa: {}'.format(vFraseInversa))
if vFraseSemEspaco == vFraseInversa:
    print('A frase é PALÍNDROMO')
else:
    print('A frase NÃO é palíndromo')
