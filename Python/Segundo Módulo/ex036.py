print('-=-'*50)
print('''Exercício Python 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.''')
print('-=-'*50)

vCasa = float(input('Digite o valor da casa: '))
vSalario = float(input('Digite o valor do salário: '))
vAnoFin = int(input('Quantos anos de financiamento: '))
vPrestacao = vCasa / (vAnoFin * 12)
print('Valor da casa: R${} \nQuantidade de Prestação: {:.0f} meses \nValor da prestação por mês: R${:.2f}'.format(vCasa,vAnoFin * 12, vPrestacao))
if vPrestacao < vSalario * 30 / 100:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')