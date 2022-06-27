n=soma=num=0
while True:
    n= int(input('Digite um valor (999 para interromper):'))
    if n == 999:
        break
    else:
        soma+=n
        num+=1
print(f'Você digitou {num} valores e a soma entre eles é de {soma}.')