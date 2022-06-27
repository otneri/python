def alt (*num):
    cont=0
    print('\nAnalisando valores passados')
    print(alt)
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram analisados {cont} valores.')
    print(f'O maio analisado foi {maior}')
alt (3,8,1,5,4)
alt (9,1,0,8,44,1)
alt(0,1)
alt(0)
alt()