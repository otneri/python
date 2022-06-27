print('GERADOR DE PA')
print('=-'*10)
a = int(input('Digite o 1 valor da PA:'))
r = int(input('Digite a razão:'))
c = n = 1
total = 0
mais = 10
while mais != 0:
    total+=mais
    while c <= total:
        print(f'{a} => ', end=' ')
        a+=r
        c += 1
    print('PAUSA.')
    mais=int(input('Quantos termos a mais vc quer ver:'))
print(f'VOCÊ VISUALIZOU {total} TERMOS DA PA.')
print('FIM')
print('=-'*10)