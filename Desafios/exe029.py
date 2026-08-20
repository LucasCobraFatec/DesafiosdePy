vel = float(input('Qual a velocidade do carro? '))
if vel < 80:
    print("Dentro do limite permitido")
else:
    valor = (vel - 80)* 7.00
    print ('Ultrapassou a velocidade permitida que é de 80 km/h, você esta à {:.0f} Km/h, isso vai lhe custar R$ {:.2f} de multa '.format(vel, valor))