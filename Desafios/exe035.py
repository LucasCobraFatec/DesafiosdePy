a = float(input("Digite o valor da largura do primeiro lado do triangulo: "))
b = float(input("Digite o valor da largura do segundo lado do triangulo: "))
c = float(input("Digite o valor da largura do terceiro lado do triangulo: "))


if (a + b) > c and (a+ c) > b and (b + c) > a:
        print("Sim é possivel formar um triangulo.")
else:
    print("Não é possivel formar um triangulo.")

