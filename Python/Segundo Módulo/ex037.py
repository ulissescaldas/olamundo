vNumero1 = int(input('Digite um número: '))
print('''Escola a base de conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
vOpcao = int(input('Digite a sua OPÇÃO: '))

if vOpcao == 1:
    print('O valor {} em BINÁRIO é {}'.format(vNumero1, bin(vNumero1)[2:]))
elif vOpcao == 2:
    print('O valor {} em OCTAL é {}'.format(vNumero1, oct(vNumero1)[2:]))
elif vOpcao == 3:
    print('O valor {} em HEXADECIMAL é {}'.format(vNumero1, hex(vNumero1)[2:]))
else:
    print('Opção INVALIDA!')
