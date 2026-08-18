


from datetime import date

ano = int(input('digite um ano completo, digite 0 para o ano atual: '))
if ano == 0:

if ano == 0:
    ano = date.today().year

if ano%4 ==0 and ano%100 != 0 or ano%400 == 0:
    print("Ano de {} é bissexto".format(ano))
else:
    print('Ano de {} não é bissexto'.format(ano))


