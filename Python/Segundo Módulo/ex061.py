print('-=-'*50)
print('''Exercício Python 61:
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.''')
print('-=-'*50)

print('10 TERMOS DE UMA PA')
vNumero1 = int(input('Digite o Primeiro Termo: '))
vNumero2 = int(input('Digite a Razão: '))
vNumero3 = 0
while vNumero3 != 10:
      print('{} ->'.format(vNumero1), end=' ')
      vNumero1 += vNumero2
      vNumero3 += 1
print('Acabou!!!')