num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('O Primeiro valor {} é maior que o Segundo valor {}'.format(num1,num2))

elif num1 < num2:
    print('O Segundo valor {} é maior que o Primeiro valor {}'.format(num2,num1))

else:
    print('Não existe valor maior, os dois são iguais')