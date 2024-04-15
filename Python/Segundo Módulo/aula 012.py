vNome = str(input('Digite um nome: '))
if vNome == 'Ulisses':
    print('Qua lindo nome!!!')
elif vNome == 'Ana' or vNome == 'Maria':
    print('Seu nome é comum')
elif vNome in 'Enzo, Valentina':
    print('Seu nome é nutella')
else:
    print('Legal não pe comum!!!')
print('Tenha um Bom Dia, {}!'.format(vNome))