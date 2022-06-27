idade=int(input('Qual sua idade:'))
if idade <18:
    print('Ainda faltam {} anos para você se alistar.'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já se passaram {} anos do seu alistamento.'.format(idade-18))