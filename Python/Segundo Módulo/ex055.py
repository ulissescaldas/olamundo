print('-=-'*50)
print('''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.''')
print('-=-'*50)

vPeso = []
for i in range(1, 6):
    vPeso.append(float(input('Digite o {}º peso: '.format(i))))
print('O menor peso é {} \nO maior peso é {}'.format(min(vPeso),max(vPeso)))