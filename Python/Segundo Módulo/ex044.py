print('=' * 10, 'LOJAS UCS', '=' * 10)
print('{:=^31}'.format(' LOJAS UCS '))
vCompra = float(input('Digite o valor da compra: '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro\cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
vOpcao = int(input('Qual é a opção: '))

if vOpcao == 1:
    vDesconto = vCompra * 10/100
    vValor = vCompra - vDesconto
    print('Valor da compra: R${:.2f} \nValor do Desconto: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(vCompra, vDesconto, vValor))

elif vOpcao == 2:
    vDesconto = vCompra * 5 / 100
    vValor = vCompra - vDesconto
    print('Valor da compra: R${:.2f} \nValor do Desconto: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(vCompra, vDesconto, vValor))

elif vOpcao == 3:
    parcela = vCompra / 2
    print('Valor da compra: R${:.2f} \nValor do parcela em 2 vezes: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(vCompra, parcela, vCompra))

elif vOpcao == 4:
    vNumeroParcela = int(input('Em quantas parcelas vai dividir? '))
    vJuros = vCompra * 20 / 100
    vValor = vCompra + vJuros
    vParcela = vValor / vNumeroParcela
    print('Valor da compra: R${:.2f} \nQuantidades de parcelas: {} \nValor das Parcelas: R${:.2f} \nValor do Juros: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(vCompra, vNumeroParcela, vParcela, vJuros, vValor))
else:
    print('Opção invalida! tente novamento.')
