print('-=-'*50)
print('''Exercício Python 57: 
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.''')
print('-=-'*50)

vSexo = str(input('Digite seu sexo [M/F]: ').strip())[0]
while vSexo not in('F,f,M,m'):
   vSexo = str(input('Dados invávilos. Por Favor, digite seu sexo [M/F]: ').strip())[0]
print('Sexo {} registrado com sucesso!!!'.format(vSexo.upper()))