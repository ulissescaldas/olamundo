print('Aula 18 – Listas (Parte 2)')
teste = []
teste.append('Ulisses')
teste.append(29)
print(teste)
galera = []
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 18
print(teste)
galera .append(teste)
print(galera)

#fazendo copia da lista
print('=-='*20)
teste = []
teste.append('Ulisses')
teste.append(29)
print(teste)
galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 18
print(teste)
galera .append(teste[:])
print(galera)

#Estrututa da lista composta
print('=-='*20)
galera = [['Ulisses', 29], ['Maria', 19], ['Miguel', 30], ['Fulana', 45]]
print(galera)
print(galera[3])
print(galera[3][0])
print(galera[0][0])
print(galera[1][0])
print(galera[2][0])
for p in galera:
    print(p)
    print(f'{p[0]} tem {p[1]} anos.')
print('=-='*20)
galera = []
dado = []
maior = menor = 0
for i in range(0, 3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'temos {maior} maiores e {menor} menores de idade.')




