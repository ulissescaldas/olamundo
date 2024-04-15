n1 = int(input('Digite o prineiro segmento: '))
n2 = int(input('Digite o segundo segmento: '))
n3 = int(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os Segmantos acima NÃO PODEM FORMAR um triângulo')

