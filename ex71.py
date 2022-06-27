n50=n20=n10=n1=cont=0
print( '{:=^30}'.format('BANCO MARBA'))
valor= int(input('BOM DIA. DIGITE O VALOR QUE VOCÊ DESEJA SACAR: '))
total=valor
ced=50
totced=0
while True:

    if total >= ced:
        total-=ced
        totced+=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced=0
        if total == 0:
            break