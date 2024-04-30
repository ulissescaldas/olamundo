print('-=-' * 50)
print('''Exercício Python 080: 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.''')
print('-=-' * 50)

vLista = []

for i in range(0, 5):
    vNumero = int(input(f'Digite o {i+1}º valor: '))
    if i == 0 or vNumero > vLista[-1]:
        vLista.append(vNumero)
        print('Valor adicionado no final da lista')
    else:
        cont = 0
        while cont < len(vLista):
            if vNumero <= vLista[cont]:
                vLista.insert(cont, vNumero)
                print(f'Valor adicionado na posição {cont+1} da lista')
                break
            cont +=1
print(f'\nVocê digitou os valores {vLista}')