peso = float(input('qual é o seu peso: '))
altura = float(input('Qual é sua altura: '))
imc = peso / (altura ** 2)
print('Seu INC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso Normal ')
elif 18.5 <= imc < 25:
    print('Paranéns! você está no PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Vocé está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA')