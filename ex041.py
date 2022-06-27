print('!!!'*20)
print('Saiba sua categoria para começar aulas de natação!')
print('!!!'*20)
idade=int(input('Digite sua idade:'))

if idade <= 9:
    print('Você é Mirim!')
elif 10 <= idade <= 14:
    print('Você é Infantil!')
elif 15 <= idade <= 19:
    print('Você é Junior!')
elif idade == 20 :
    print('Você é Senior')
else:
    print('Você é Master!')