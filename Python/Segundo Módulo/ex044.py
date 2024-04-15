print('=' * 10, 'LOJAS UCS', '=' * 10)
print('{:=^31}'.format(' LOJAS UCS '))
compra = float(input('Digite o valor da compra: '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro\cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção: '))

if opcao == 1:
    desconto = compra * 10/100
    valor = compra - desconto
    print('Valor da compra: R${:.2f} \nValor do Desconto: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(compra, desconto, valor))

elif opcao == 2:
    desconto = compra * 5 / 100
    valor = compra - desconto
    print('Valor da compra: R${:.2f} \nValor do Desconto: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(compra, desconto, valor))

elif opcao == 3:
    parcela = compra / 2
    print('Valor da compra: R${:.2f} \nValor do parcela em 2 vezes: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(compra, parcela, compra))

elif opcao == 4:
    numeroparcela = int(input('Em quantas parcelas vai dividir? '))
    juros = compra * 20 / 100
    valor = compra + juros
    parcela = valor / numeroparcela
    print('Valor da compra: R${:.2f} \nQuantidades de parcelas: {} \nValor das Parcelas: R${:.2f} \nValor do Juros: R${:.2f} \nValor a PAGAR: R${:.2f}'.format(compra, numeroparcela, parcela, juros, valor))
else:
    print('Opção invalida! tente novamento.')
