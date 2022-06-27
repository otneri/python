from time import sleep
n=int(input('Digite um número :'))
c = n
f = 1
print(f'Calculando {n}! = ', end=' ')
sleep(1)
while c > 0:
    print(c, end=' ')
    print(' X ' if c >1 else ' = ', end=' ' )
    f*=c
    c-=1
sleep(1)
print(f)