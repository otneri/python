from random import randint
from operator import itemgetter
from time import sleep
jogada={'jogador 1':(randint(1,6)),'jogador 2':(randint(1,6)),'jogador 3':(randint(1,6)),
        'jogador 4':(randint(1,6))}
ranking=()
print('$'*30)
print('JOGADAS:')
for k,v in jogada.items():
        print(f'O {k} tirou {v}.')
        sleep(1)

print('RANKING:')
ranking= sorted(jogada.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate (ranking):
        print(f'{i+1}o lugar: {v[0]} com {v[1]}.')
        sleep(1)