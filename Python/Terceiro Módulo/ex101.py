print('-=-' * 50)
print('''Exercício Python 101: 
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.''')
print('-=-' * 50)


def voto(ano=0):
    from datetime import date
    v_ano = date.today().year
    v_idade = v_ano - ano
    print(f'Com {v_idade} anos: ', end='')
    if v_idade < 16:
        print('Voto Negado')
    elif 16 < v_idade < 18 or v_idade > 65:
        print('Voto Opcional')
    else:
        print('Voto Obrigatário')


voto(int(input("Digite o ano de nascimento: ")))
