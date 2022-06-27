print('#'*20)
print('JOGO DO PAR OU IMPAR')
print('#'*20)
from random import randint
userpi=resposta=acertos=0
while userpi == resposta:
    usernum=int(input('Digite um numero:'))
    userpi=' '
    while userpi not in 'PI':
        userpi=str(input('P/I:')).upper().strip()[0]
    compnum= randint(0,100)
    n= usernum+compnum
    if n % 2 == 0:
        resposta = 'P'
    else:
        resposta= 'I'
    print(f'Soma igual a {n}')
    if userpi == resposta:
        acertos+=1
        print('VOCÊ ACERTOU! CONTINUE.')
print(f'''FIM DO PROGRAMA...
      VOCÊ ACERTOU {acertos} VEZES!!!''')