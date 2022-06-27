from random import choice
pedra = 1
papel = 2
tesoura = 3
lista= [pedra,papel,tesoura]
print('=-'*15)
print('JOKENPO')
print('=-'*15)
print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogada= int(input('Qual sua jogada:'))
print('JOKENPO!')
pc= choice(lista)
print(f'O COMPUTADOR ESCOLHEU {pc}.')
if pc==jogada:
    print('EMPATE!')
elif jogada == 1:
    if pc == 2:
        print('Você perdeu. Tente novamente.')
    else:
        print('Você venceu!')
elif jogada == 2:
    if pc == 1:
        print('Você venceu!')
    else:
        print('Você perdeu. Tente novamente.')
elif jogada == 3:
    if pc == 1:
        print('Você perdeu. Tente novamente.')
    else:
        print('Você venceu!')