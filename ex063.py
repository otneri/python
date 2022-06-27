n=0
soma=dig=0
while n != 999:
    n= int(input('Digite um número:'))
    if n != 999:
        soma+=n
        dig+=1
print(f'FIM. Voce digitou {dig} números e a soma entre eles é de {soma}.')