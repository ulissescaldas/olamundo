print('-=-' * 50)
print('''Exercício Python 093: 
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
 incluindo o total de gols feitos durante o campeonato.''')
print('-=-' * 50)

vJogador = {}
vGol = []

vJogador['nome'] = str(input('Digite o nome do jogador: '))
vCont = int(input(f'Quantas partidas {vJogador['nome']} jogou? '))
for i in range(0, vCont):
    vGol.append(int(input(f'Quantos gols na partida {i+1}? ')))
vJogador['gols'] = vGol.copy()
vJogador['total'] = sum(vGol)
vGol.clear()
print('-=-' * 25)
print(vJogador)
print('-=-' * 25)
for k, v in vJogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 25)
print(f'O jogador {vJogador['nome']} jogou {vCont} partidas:')
for i, v in enumerate(vJogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Total de {vJogador['total']} gols ')
