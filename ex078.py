numeros= []
mai=men=0
for n in range (0,5):
    numeros.append(int(input(f'Digite um número na posição {n}:')))
    if n == 0:# para numero na posição zero
        mai=men=numeros[n]
    else:
        if numeros[n] > mai:
            mai=numeros[n]
        if numeros [n] < men:
            men = numeros [n]
print('#-'*50)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor foi {mai} nas posições', end='' )
for i, v in enumerate (numeros):
    if v == mai:
        print(f' {i}...', end='' )
print()
print(f'O menor valor foi {men} nas posições', end='')
for i, v in enumerate(numeros):
    if v == men:
        print(f' {i}...', end='' )
print()

print('~'*50)



