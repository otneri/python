r=0
maior=menor=media=cont=soma=0

while r != 'N':
    n= int(input('Digite um valor:'))
    r=str(input('Quer continuar(S/N):')).upper()
    cont+=1
    soma+=n
    media=soma/cont
    if cont == 1:
        maior= n
        menor= n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor= n

print(f'A média dos valores foi de {media}. O maior valor digitado foi {maior}, o menor valor foi {menor}.')

