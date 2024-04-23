print('Aula 16 – Tuplas')

vLanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(vLanche)
print(vLanche[0])
print(vLanche[1])
print(vLanche[2])
print(vLanche[3])
print(vLanche[:2])
print(vLanche[2:])
print(vLanche[0:2])
print(vLanche[2:5])
print(vLanche[-1])
print(vLanche[-2])
print(vLanche[-3])
print(vLanche[-4])
print(vLanche[-0])

#Tuplas são imutáveis

for c in vLanche:
    print(f'Meu Lance é {c}')

vNumero1 = (1,3,5,7,9)
vNumero2 = (0,2,4,6,8)
vNumero3 = vNumero1 + vNumero2
print(vNumero3)
print(vNumero3.count(9))
print(len(vNumero3))

