a = float(input("Digite o valor da largura do primeiro lado do triangulo: "))
b = float(input("Digite o valor da largura do segundo lado do triangulo: "))
c = float(input("Digite o valor da largura do terceiro lado do triangulo: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Sim é possivel formar um triangulo.")
    if a == b and b == c and a == c:
        print('Esse triâgulo é Equilátero.')
    elif a == b or a == c or b == c:
        print('Esse triângulo é Isósceles.')
    elif a != b and b != c and b != c and a != c:
        print('Esse triângulo pe Escaleno.')

else:
    print("Não é possivel formar um triangulo.")
