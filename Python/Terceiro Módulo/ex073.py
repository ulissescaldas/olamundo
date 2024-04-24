print('-=-'*50)
print('''Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Flamengo.
Tabela BRASILEIRÃO SÉRIE A - 24/04/2024 07:09''')
print('-=-'*50)

vtabela = ('Bragantino', 'Flamengo', 'Botafogo', 'Athletico - PR', 'Grêmio', 'Internacional', 'Atlético - MG',
           'Fortaleza', 'Bahia', 'Fluminense', 'Palmeiras', 'Cruzeiro', 'Juventude', 'São Paulo', 'Vasco')
vtabelaAlf = sorted(vtabela)

print('-=-'*10)
print('Tabela com os 5 primerios colocados:')
for i in range(0, 6):
    print(f'{i+1}º colocado: {vtabela[i]}')

print('-=-'*10)
print('Tabela com os 4 últimos colocados:')
for i in range(len(vtabela)-4, len(vtabela)):
    print(f'{i}º colocado: {vtabela[i]}')

print('-=-'*10)
print('Tabela em ordem alfabética:')
for i in vtabelaAlf:
    print(f'{i}')

print('-=-'*10)
print(f'O Flamengo está em {vtabela.index('Flamengo') + 1}º lugar na tabela')
