n=0
while True:
    n= int(input('Digite um número para ver sua tabuada:'))
    if n < 0:
        break
    for c in range (0,11):
        r= c*n
        print(f'{c} X {n} = {r}')
print('FIM;')