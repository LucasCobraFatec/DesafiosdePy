import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
ordem = random.sample(lista,k=4)



print('A ordem de apresentação: 1° {}, 2° {}, 3° {} e 4° {}'.format(ordem[0],ordem[1],ordem[2],ordem[3]))