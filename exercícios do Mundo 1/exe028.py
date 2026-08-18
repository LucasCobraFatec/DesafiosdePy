import random

numero = random.randint(0,5)
chute = int(input('Chute qual o valor que o computador escolheu dentre 0 a 5: '))
if numero == chute:
    print('Voce acertou')
else:
    print("Que pena você errou")

print('O número escolhido foi {}, o seu numero foi {}'.format(numero,chute))




