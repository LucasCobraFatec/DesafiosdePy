salario = float(input('Digite o seu salario: '))

if salario <= 1250:
    print("O aumento foi de 15%, seu salario sera {:.2f}.".format(salario + (salario *0.15)))
else:
    print("O aumento foi de 10%, seu salario sera {:.2f}.".format(salario + (salario * 0.1)))