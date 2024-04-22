print('-=-'*50)
print('''Exercício Python 62:
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.''')
print('-=-'*50)

print('10 TERMOS DE UMA PA')
vNumero1 = int(input('Digite o Primeiro Termo: '))
vNumero2 = int(input('Digite a Razão: '))
vNumero3 = 10
vNumero4 = vNumero3
while vNumero3 != 0:
      print('{} ->'.format(vNumero1), end=' ')
      vNumero1 += vNumero2
      if vNumero3 == 1:
          vNumero3 = int(input('PAUSA \nQuantos temos vocês quer mostrar a mais? '))
          vNumero4 += vNumero3
      else:
          vNumero3 -= 1
print('Acabou!!!')
print('Total de {} termos mostrados.'.format(vNumero4))