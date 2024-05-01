print('-=-' * 50)
print('''Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.''')
print('-=-' * 50)

vExpressao = str(input('Digite um expressão: ')).strip()
vLista = []
for i in vExpressao:
    vLista.append(i)
if vLista.count('(') == vLista.count(')'):
    print('Essa expressão é VALIDA')
else:
    print('Expressão invalida!!!')
print(f'( = {vLista.count('(')} \n) = {vLista.count(')')}')