v=float(input('Qual sua velocidade em Km/h:'))
if v >80:
    m=(v-80)*7
    print(f'Você foi multado em R$ {m:.2f}')
else:
    print('Você está dentro do limite de velocidade.')