print('-=-'*50)
print('''Exercício Python 43: 
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida''')
print('-=-'*50)

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