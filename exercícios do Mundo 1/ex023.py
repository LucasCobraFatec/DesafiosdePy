num = (input('Digite um numero entre 0 e 9999: '))


valores = num.split()

print('unidade: {}'.format(valores[0][3]))
print('dezena: {}'.format(valores[0][2]))
print('centena: {}'.format(valores[0][1]))
print('milhar: {}'.format(valores[0][0]))