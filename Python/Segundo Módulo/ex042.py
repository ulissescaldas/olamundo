vNumero1 = int(input('Digite o prineiro segmento: '))
vNumero2 = int(input('Digite o segundo segmento: '))
vNumero3 = int(input('Digite o terceiro segmento: '))
if vNumero1 < vNumero2 + vNumero3 and vNumero2 < vNumero1 + vNumero3 and vNumero3 < vNumero1 + vNumero2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if vNumero1 == vNumero2 == vNumero3:
        print('EQUILÁTERO!')
    elif vNumero1 != vNumero2 != vNumero3 != vNumero1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os Segmantos acima NÃO PODEM FORMAR um triângulo')

