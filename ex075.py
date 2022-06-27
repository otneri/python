#guardar 05 numeros do teclado em tupla,
n=tuple(int(input('Digite um número:')) for c in range (4))
print(f'Os números digitados foram: {n}')
#qntas vezes aparece o 9
if 9 in n :
    nove= n.count(9)
    print(f'O valor nove apareceu {nove} vezes.')
else:
    print('Não há número nove.')
#posição do três
if 3 in n:
    print(f'O número três apareu a primeira vez na {n.index(3)+1}a posição')
else:
    print('Não há número três.')
#quais números pares:
print('Os números pares foram:',end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
