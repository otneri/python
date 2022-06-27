familia=list()
pessoa=dict()
soma=media=0

while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome:'))
    while True:
        pessoa['sexo']= str(input('Sexo (M/F):')).upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite um sexo válido.')
    pessoa['idade']= int(input('Idade:'))
    soma+=pessoa['idade']
    familia.append(pessoa.copy())
    while True:
        next=str(input('Quer continuar (S/N):')).upper()
        if next in 'SN':
            break
        else:
            print('ERRO! DIGITE S ou N.')
    if next == 'N':
        break
print(familia)
print('#'*50)
#pessoas cadastradas
print(f'Foram cadastradas {len(familia)} pessoas.')
#media idade
media= soma/len(familia)
print(f'A média de idade da família é {media}.')
#lista com mulheres
for p in familia:
    if p['sexo'] in 'Ff':
        print(f'As mulheres são {p["nome"]}',end=', ')
        print()
#lista idades acima da média
for i in familia:
    if pessoa['idade'] >= media:
        print(f'As pessoas com idade acima da média foram {pessoa["nome"]}.')
