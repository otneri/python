time=list()
jogador=dict()
while True:
    jogador.clear()
    jogador['nome']=str(input('NOME:'))
    partidas=int(input(f'QUANTAS PARTIDAS {jogador["nome"]} JOGOU:'))
    gols= []
    for c in range (0,partidas):
        gol=int(input(f'    Quantos gols na partida {c}:'))
        gols.append(gol)
    jogador['gols']=gols[:]
    jogador['total']= sum(gols)
    time.append(jogador.copy())
    resp=input('Quer continuar S/N: ').upper()
    if resp == 'N':
        break
print('-'*50)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
print('-'*50)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
print('#'*50)
while True:
    estat=int(input('Quer ver os dados de qual jogador. 999 parar: '))
    if estat == 999:
        break
    if estat > len(time):
        print('ERRO! Valor invalido.')
    else:
        print(f'Levantamento jogador {time[estat]["nome"]} :')
        for i, v in enumerate(time[estat]['gols']):
            print(f'    =>Na partida {i}, fez {v} gols.')
        print(f'Fez um total de {time[estat]["total"]} gols.')