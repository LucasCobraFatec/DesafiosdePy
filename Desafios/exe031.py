viagem = float(input('Quantos quilometros ira percorrer nessa viagem: '))

if viagem <=200:
    viagem = viagem * 0.50
    print("valor da viagem: R$ {:.2f}".format(viagem))
else:
    viagem = viagem * 0.45
    print("valor da viagem: R$ {:.2f}".format(viagem))

