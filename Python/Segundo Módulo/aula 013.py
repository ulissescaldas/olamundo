print('Aula 13 – Estrutura de repetição for')

for i in range(0, 6):
    print('Oi')
print('Fim')

for i in range(0, 6):
    print(i)
print('Fim')

for i in range(6, 0, -1):
    print(i)
print('Fim')

i = int(input('início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

s = 0
for i in range(0, 4):
    n = int(input('Digite o número {}: '.format(i+1)))
    s = s+n
print('O somatório de todos os valores é {}'.format(s))
print('Fim')

