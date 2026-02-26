kmpercorrido = float(input('Quantos Km foi percorrido pelo carro: '))
diasalugado = float(input('Quantos dias ele foi alugado: '))

valortotal = (kmpercorrido * 0.15) + (diasalugado * 60)

print('Você pagará de aluguel : R${:.2f}'.format(valortotal))