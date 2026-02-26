import math
angulo = float(input('Digite um angulo: '))

angulograus = math.radians(angulo)


sen = math.sin(angulograus)
co = math.cos(angulograus)
tan = math.tan(angulograus)

print('O angulo {} tem o valor {} seno, {} cosseno e {} tangente'.format(angulo,sen,co,tan))
