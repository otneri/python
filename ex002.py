nome = input('Qual é o seu nome!')
cor={'rosa':'\033[34m',
     'verde': '\033[32m',
     'limpa':'\033[m',
     'negativo':'\033[7;30m',
                       'fundo':'\033[46m' }
print('{} É{} {}um prazer{} {}te  conhecer,{} {}{}{}'.format(cor['rosa'],cor['limpa'],cor['verde'],cor['limpa'], cor['fundo'], cor['limpa'],cor['negativo'],nome,cor['limpa']))
