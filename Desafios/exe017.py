import math

co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))

# math.hypot já calcula a raiz da soma dos quadrados
hipotenusa = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hipotenusa))
