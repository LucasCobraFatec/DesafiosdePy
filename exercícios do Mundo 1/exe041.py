from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SENIOR')

else:
    print('Categoria: MASTER')