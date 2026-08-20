numero = int(input('Digite um número para ser convertido: '))
base = int(input('[1] - binario \n[2] - octal \n[3] - hexadecimal \n Digite o némero da base que quer converter : '))

if base == 1:
    convertido = bin(numero)
    print('O número {}, em binario fica {}'.format(numero, convertido))
elif base == 2:
    convertido = oct(numero)
    print('O número {}, em octal fica {}'.format(numero, convertido))
elif base == 3:
    convertido = hex(numero)
    print('O número {}, em  hexadecimal fica {}'.format(numero, convertido))

else:
    print('Numero de base invalido')