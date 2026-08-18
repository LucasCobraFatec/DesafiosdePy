nome = str(input('Digite seu nome completo: ')).strip()

nomediv = nome.split()

print("Muito prazer {}".format(nome))
print('Seu primeiro nome é {}'.format(nomediv[0]))
print('Seu ultimo nome é {}'.format(nomediv[-1]))
