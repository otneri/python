n = [[], []]

for c in range(1, 8):
    valor= int(input(f'Digite o {c} valor:'))
    if valor % 2 == 0:
        n[0].append(c)
    else:
        n[1].append(c)
n[1].sort()
n[0].sort()
print(f'Os números pares foram {n[0]}')
print(f'Os números ímpares foram {n[1]}')