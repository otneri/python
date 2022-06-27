from random import randint
itens= ('Pedra', 'Papel', 'Tesoura')
pc= randint(1,3)
print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador= int(input('Qual sua jogada:'))
print('=-'*15)
print(f'computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogador]}')
print('=-'*15)
if pc == 1: #pc joga pedra
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador ganha')
    elif jogador == 3:
        print('PC ganha')
    else:
        print('Inválido')
elif pc == 2:  # pc joga papel
    if jogador == 2:
        print('EMPATE')
    elif jogador == 1:
        print('PC ganha')
    elif jogador == 3:
        print('Jogador ganha')
    else:
        print('Inválido')
elif pc == 3: #pc joga tesoura
    if jogador == 3:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador ganha')
    elif jogador == 2:
        print('PC ganha')
    else:
        print('Inválido')