vCasa = float(input('Digite o valor da casa: '))
vSalario = float(input('Digite o valor do Salário: '))
vAnoFin = int(input('Quantos anos de financiamento: '))
vPrestacao = vCasa / (vAnoFin * 12)
print('Valor da casa: R${} \nQuantidade de Prestação: {:.0f} meses \nValor da prestação por mês: R${:.2f}'.format(vCasa,vAnoFin * 12, vPrestacao))
if vPrestacao < vSalario * 30 / 100:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')