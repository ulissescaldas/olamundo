print('-=-'*50)
print('''Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120''')
print('-=-'*50)

vNumero = int(input('Digite um número: '))
vCont = vNumero
vFatorial = 1
print('<><><><> Comando WHILE <><><><>')
print('O faturial de {}! = '.format(vNumero), end='')
while vCont > 0:
    print('{}'.format(vCont), end='')
    print(' x ' if vCont > 1 else ' = ', end='')
    vFatorial *= vCont
    vCont -= 1
print('{}'.format(vFatorial))

vCont = vNumero
vFatorial = 1
print('\n<><><><> Comando FOR <><><><>')
print('O faturial de {}! = '.format(vNumero), end='')
for i in range(vCont, 0, -1):
    print('{}'.format(vCont), end='')
    print(' x ' if vCont > 1 else ' = ', end='')
    vFatorial *= vCont
    vCont -= 1
print('{}'.format(vFatorial))