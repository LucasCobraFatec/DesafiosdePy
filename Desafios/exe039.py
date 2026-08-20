from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - anoNascimento

falta = 18 - idade

passou = idade - 18

if idade < 18:
    print('Você ainda vai se alistar pois hoje ainda tem {} anos, falta {} anos para você se alistar'.format(idade, falta))
elif idade == 18:
    print('Chegou a hora de se alistar')

else:
    print('Já passou a hora de se alistar, {} anos se passaram'.format(passou))
