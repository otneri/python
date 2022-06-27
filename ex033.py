a=int(input('Primeiro número:'))
b=int(input('Segundo número:'))
c=int(input('Terceiro número:'))
menor=a
if b<c and b<a:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>c and b>a:
    maior=b
if c>a and c>b:
    maior=c
print(f'O maior valor é {maior} e o menor valor é {menor}')