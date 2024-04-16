print('-=-'*50)
print('Exercício Python 49: \nTabuada v.2.0')
print('-=-'*50)
vNumero = int(input('Digite um número: '))
for i in range(1, 11):
    print('{} x {} = {}'.format(vNumero, i, vNumero * i))