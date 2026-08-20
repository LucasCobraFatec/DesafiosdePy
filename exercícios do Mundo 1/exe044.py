valorProduto = float(input('Digite o valor do produto: '))
formaPagamento = int(input('''Forma de pagamento
[1] - dinheiro/PIX 
[2] - à vista no cartão
[3] - até 2x no cartão 
[4] - 3x ou mais
 Digite a forma de pagamento: '''))

if formaPagamento == 1:
    valorProduto = valorProduto - (valorProduto * 0.10)
    print('À vista no dinheiro/pix sai à R${:.2f} com 10% de desconto'.format(valorProduto))
elif formaPagamento == 2:
    valorProduto = valorProduto - (valorProduto * 0.05)
    print('À vista no cartão R$ {:.2f} com 5% de desconto'.format(valorProduto))
elif formaPagamento == 3:
    parcela = valorProduto / 2
    print('Em até 2x no cartão valor será R${:.2f}, pode ser parcelado em 2x de R$ {:.2f}'.format(valorProduto,parcela))
elif formaPagamento == 4:
    valorProduto = valorProduto + (valorProduto * 0.20)
    parcela = valorProduto / 3
    print('3x ou mais no cartão no valor de RS{:.2f} com 20% de juros, que pode ser parcelado em 3x de R$ {:.2f}'.format(valorProduto,parcela))
else:
    print('Não selecionada opção valida')