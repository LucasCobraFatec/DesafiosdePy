produto = float(input('Digite o valor do produto: '))

precofinal = produto -(produto * 5 / 100)

print('O preco final do produto com desconto é : R$ {:.2f}'.format(precofinal))