print('{} LOJAS ABC'.format('='*40))
valor= float(input('Qual o valor da compra:'))
print('''Selecione a forma de pagamento:
        [1] à vista cheque ou dinheiro
        [2] à vista no cartão
        [3] 2 x no cartão
        [4] 3 x ou mais no cartão.''')
pagamento= (int(input('Forma de pagamento:')))

if pagamento == 1:
    total= valor-(valor*0.1)
elif pagamento == 2:
    total=valor - (valor * 0.05)
elif pagamento == 3:
    total=valor
    print(f'Sua compra será dividida em 2x SEM JUROS de R${total/2}')
elif pagamento == 4:
    parcela= int(input('Em quantas parcelas deseja pagar:'))
    total= valor + (valor * 0.2)
    totparc= total/parcela
    print(f'Sua compra será parcelada em {parcela}x de {totparc}')
print(f'Sua compra será de R${total}')