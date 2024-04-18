print('-=-'*50)
print('''Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.''')
print('-=-'*50)

from random import randint

print('''<><><><> Bem vindo ao jogo do Palpite <><><><>
<><><><><><> Sou o seu computador <><><><><><>
  Acabei de pensar em um número entre 0 e 10
   Sé que você consegue adivinhar qual foi?''')
vCont = 1
vComputador = randint(0,10)
vPalpite = int(input('Qual seu palpite? '))
while vPalpite != vComputador:
    vCont += 1
    if vPalpite > vComputador:
        vPalpite = int(input('Menos... Tente mais uma vez. '))
    else:
        vPalpite = int(input('Mais... Tente mais uma vez. '))
print('Acertou com {} tentativas. Parabéns!'.format(vCont))