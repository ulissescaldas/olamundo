print('Aula 15 – Interrompendo repetições while')

vCont = 0
while True:
    print(f'{vCont}', end=' -> ')
    vCont += 1
    if vCont == 999:
        break
print('Fim')


