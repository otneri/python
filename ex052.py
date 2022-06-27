tot=0
n=int(input('Digite um número:'))

for c in range (1,n+1):
    print(c)
    if n % c == 0:
        tot+=1
print(f'O número {n} foi divisível {tot} vezes.')
if tot == 2:
    print(f'O número {n} é PRIMO.')
else:
    print(f'O número {n} não é PRIMO.')