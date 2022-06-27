from random import randint
from time import sleep
n=int(input('Quantos jogos você quer que eu sorteie:'))
for c in range (0,n):
    jogo =[]
    while len(jogo) < 6:
        num= randint(1,60)
        if num not in jogo:
            jogo.append(num)
    print(jogo)
