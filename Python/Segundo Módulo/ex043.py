vPeso = float(input('qual é o seu peso: '))
vAltura = float(input('Qual é sua altura: '))
vImc = vPeso / (vAltura ** 2)
print('Seu INC é {:.1f}'.format(vImc))
if vImc < 18.5:
    print('Você está ABAIXO do peso Normal ')
elif 18.5 <= vImc < 25:
    print('Paranéns! você está no PESO NORMAL')
elif 25 <= vImc < 30:
    print('Você está em SOBREPESO')
elif 30 <= vImc < 40:
    print('Vocé está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA')