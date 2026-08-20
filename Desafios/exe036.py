valorCasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anosPagar = int(input('Digite quantos anos deseja pagar: '))

parcela = valorCasa / (anosPagar*12)

if parcela > salario *0.3:
    print('Emprestimo negado, devido a parcela execeder a 30% do salario atual')
    print('Salario atual {:.2f}, Valor da parcela R$ {:.2f}. em  {} anos'.format(salario,parcela,anosPagar))
else:
    print('Aprovado!,  valor da parcela R$ {:.2f}, paga em {} anos'.format(parcela,anosPagar))



