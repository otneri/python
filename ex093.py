jogador=dict()
jogador['nome']=str(input('NOME:'))
partidas=int(input(f'QUANTAS PARTIDAS {jogador["nome"]} JOGOU:'))
gols= []
for c in range (0,partidas):
    gol=int(input(f'    Quantos gols na partida {c}:'))
    gols.append(gol)
jogador['gols']=gols[:]
jogador['total']= sum(gols)
print('#'*50)
print(jogador)
print('#'*50)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('#'*50)
print(f'O jogador {jogador["nome"]} jogou {partidas} jogos:')
for i, v in enumerate(gols):
    print(f'    =>Na partida {i}, fez {v} gols.')

print(f'Fez um total de {jogador["gols"]} gols.')