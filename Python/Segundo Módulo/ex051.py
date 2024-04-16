print('-=-'*50)
print('''Exercício Python 51: 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.''')
print('-=-'*50)

print('10 TERMOS DE UMA PA')
vNumero1 = int(input('Digite o Primeiro Termo: '))
vNumero2 = int(input('Digite a Razão: '))
vNumero3 = vNumero1 + 10 * vNumero2
for i in range(vNumero1, vNumero3, vNumero2):
      print('{} ->'.format(i), end=' ')
print('Acabou!!!')