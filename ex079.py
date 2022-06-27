n=[]
while True:
    numero=int(input('Digite um novo número:'))
    if numero not in n:
        n.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado')
    r=str(input('Quer continuar (S/N):')).upper()
    if r == 'N':
        break

print('#-'*50)
print(f'Você adicionou em sua lista os valores {sorted(n)} !')