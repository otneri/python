d=int(input('Digite a distância da sua viagem em Km:'))
if d < 200:
    p = d*0.5
else:
    p = d*0.45
print(f'Sua viagem custará R${p}.')
