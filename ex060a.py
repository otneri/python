n=int(input('Digite um número :'))
valor=1
for c in range (n,0,-1):
    valor*=c

print(f'Seu fatorial é: {valor}')
