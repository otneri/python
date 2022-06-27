medid=0
idadevelho=0
nomevelho=0
mmenor=0
for c in range (0,4):
    nome = str(input('Digite seu nome:')).strip()
    idade = int (input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo [M/F]:')).upper()
    medid += idade/4
    if c == 1 and sexo == 'M':
        idadevelho = idade
        nomevelho = nome
    if sexo == 'M' and  idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if idade <= 21 and sexo == 'F':
        mmenor+=1

print(f'A média de idade do grupo é de {medid}')
print(f'O homem mais velho é o {nomevelho} com {idadevelho} anos.')
print(f'Existem {mmenor} mulheres menores de idade.')
