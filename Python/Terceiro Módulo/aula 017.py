print('Aula 17 – Listas (Parte 1)')

num = [1, 2, 3, 4, 5]
print(num)

print('troca de valores')
num[3] = 9
num[4] = 8

print('adicionar novo itens')
num.append(7)
print(num)

print('ordernar a lista')
num.sort()
print(num)

num.sort(reverse=True)
print(num)

print('apagar itens')
print('o último')
num.pop()
print(num)
print('por index')
num.pop(2)
print(num)
print('pelo o primeiro elemento')
num.remove(3)
print(num)
if 8 in num:
    num.remove(8)
    print(num)
else:
    print('Valor não encontrado!')
num.append(1)
num.append(2)
num.append(3)
num.append(4)
num.append(5)
print(num)

print('for para mostrar o index e o item da lista')
for i, v in enumerate(num):
    print(f'Na posição {i} encontrei o valor {v}')

print('ligação de lista')
num2 = num
print(num)
print(num2)

print('uma lista altera a outra')
num2[0] = 0
print(num)
print(num2)

print('copia de uma lista')
num3 = num[:]
num3[1] = 9
print(num)
print(num3)

num3.pop(1)
print(num3)
