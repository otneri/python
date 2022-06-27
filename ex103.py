def ficha(nome='desconhecido', gols=0):
    nome = input('Nome do jogador:')
    if nome =='':
       nome='desconhecido'
    gols = input('Gols marcados:')
    if gols == '':
       gols=0

    print(f'O jogador {nome} marcou {gols} gols no campeonato.')


print(ficha())
