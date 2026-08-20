peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual pe a sua altura: '))


imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC {:.2f}, abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC {:.2f}, peso ideal.'.format(imc))
elif imc >=25 and imc <30:
    print('IMC {:.2f}, sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC {:.2f}, Obesidade.'.format(imc))
else:
    print('IMC {:.2f}, Obesidade mórbida.'.format(imc))