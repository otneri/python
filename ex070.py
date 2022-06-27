print('LOJÃO DO BRAS')
caro=preco=barato=cont=total=0
while True:
    produto= str(input('PRODUTO:')).upper().strip()
    valor= float(input('VALOR:'))
    resp=' '
    while resp not in 'SN':
        resp= str(input('CADASTRAR MAIS UM (S/N):')).upper().strip()[0]
    cont+=1
    total+=valor
    if cont == 1 or valor < preco:
        preco = valor
        barato = produto
    #else:
        #if valor < barato:
            #barato=valor
    if valor > 50:
        caro+=1
    if resp == 'N':
        break
print('{:!^40}'.format('FIM DAS COMPRAS'))
print(f'TOTAL= R${total:.1f}'
      f'O produto mais barato foi {barato} que custou R${preco:.2f}. '
      f'Você comprou {caro} produtos com valor acima de R$50 ' )
