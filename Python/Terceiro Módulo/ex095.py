print('-=-' * 50)
print('''Exercício Python 095: 
Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.''')
print('-=-' * 50)

vJogador = {}
vGol = []
vLista = []
while True:
    vJogador['nome'] = str(input('\nDigite o nome do jogador: '))
    vCont = int(input(f'Quantas partidas {vJogador['nome']} jogou? '))
    for i in range(0, vCont):
        vGol.append(int(input(f'Quantos gols na partida {i+1}? ')))
    vJogador['gols'] = vGol.copy()
    vJogador['total'] = sum(vGol)
    vLista.append(vJogador.copy())
    vGol.clear()
    vJogador.clear()
    while True:
        vOpcao = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if vOpcao in 'SN':
            break
        print('Opção inválida! ')
    if vOpcao in 'N':
        break
print('-=-' * 50)
print('CÓD NOME                       GOLS                      TOTAL')
print('-'*62)
for k, v in enumerate(vLista):
    print(f'{k:>3} {v['nome']:<26} {str(v['gols']):<25} {v['total']:<5}')
print('-=-' * 50)
while True:
    vOpcao = int(input('\nMostrar dados de qual jogador? (999 para sair) '))
    if vOpcao == 999:
        break
    elif vOpcao >= len(vLista):
        print('Opção inválida! ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADO {vLista[vOpcao]['nome']} :')
        for k, v in enumerate(vLista[vOpcao]['gols']):
            print(f'   No jogo {k+1} fez {v} gols.')
        