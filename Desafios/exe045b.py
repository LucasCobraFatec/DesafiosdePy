from random import randint
itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada: '))
print('-='*15)
print('Computador jogou: {}.'.format(itens[computador]))
print('Jogador jogou: {}.'.format(itens[jogador]))
print('-='*15)

if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('Parabens o jogador ganhou!')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('Infelismente o computador ganhou!')
else:
    print('Empate')
