numeros=[]
impar=[]
par=[]
while True:
    n=(int(input('Digite um valor:')))
    numeros.append(n)
    r=str(input('Quer continuar (SN):')).upper()
    if r == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('@'*50)
print(f'Sua lista de números: {numeros}'
      f'Lista de números pares: {par}'
      f'lista de números ímpares: {impar}')