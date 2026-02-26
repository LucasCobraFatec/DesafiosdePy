nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())

semespaco = nome.replace(' ','')
contagem = len(semespaco)

print('Total de letras sem espaço é {}'.format(contagem))

divido = nome.split()

print('O primeiro nome tem {} letras'.format(len(divido[0])))
