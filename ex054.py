#maioridade
from datetime import date
a=date.today().year
maiores=0
menores=0
for c in range (1,8):
    n= int(input(f'ANO DE NASCIMENTO DA {c}@ PESSOA:'))
    idade= a-n
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'São {maiores} maiores de idade e {menores} menores de idade.')


