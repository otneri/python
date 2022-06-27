lista=[]
while True:
    n=int(input('Digite um valor:'))
    lista.append(n)
    r=str(input('Quer continuar (S/N:')).upper()
    if r == 'N':
        break
print('#='*50)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
  print('A lista contem o numero 5.')
else:
    print('A lista não tem número 5.')
