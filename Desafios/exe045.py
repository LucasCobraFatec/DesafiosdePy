import random

minhamao = int(input('''
[1] - Papel
[2]- Tesoura
[3] - Pedra 
digite o número referente sua escolha: '''))

robo = random.randint(1,3)

if minhamao == robo:
    print('Empate')
    print('Voce {}'.format(minhamao))
    print('robo {}'.format(robo))
elif minhamao == 1 and robo == 2 or minhamao == 2 and robo == 3 or minhamao == 3 and robo == 1:
    print('Você perdeu')
    print('Voce {}'.format(minhamao))
    print('robo {}'.format(robo))
else:
    print('Você ganhou')
    print('Voce {}'.format(minhamao))
    print('Robo {}'.format(robo))
