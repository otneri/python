a = int(input('Digite o 1 valor da PA:'))
r = int(input('Digite a razão:'))
for c in range (1,11):
    n=a+(c-1)*r
    print(f'O valor de sua PA em {c} = {n}')