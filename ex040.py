p1=float(input('Digite sua nota na P1:'))
p2=float(input('Digite sua nota da P2:'))
media= (p1+p2)/2
if media < 5.0:
    print('Você foi reprovado. Tchau!')
elif 5.0 <= media <= 6.9:
    print('Você está de recuperação. Estude!')
else:
    print('Você foi aprovado. Parabéns!')