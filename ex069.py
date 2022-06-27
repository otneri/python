#cadastrar pessoas e mostrar: quantos +18; qntas mulheres -20 e qntos homens total
print('-'*20)
print('CADASTRO DE USERS')
print('-'*20)
sexo=cont=homens=f20=maiores=0

while True:
    print('CADASTRE UMA PESSOA')
    idade=int(input('Idade:'))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Sexo (M/F):')).strip().upper()[0]
    cont=' '
    while cont not in 'SN':
        cont=str(input('Quer continuar (S/N):')).strip().upper()[0]
    if idade >= 18:
        maiores+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        f20+=1
    if cont == 'N':
        break
print(f'FIM DOS CADASTROS. HOMENS CADASTRADOS: {homens}, '
      f'PESSOAS MAIORES DE 18: {maiores}, '
      f'MULHERES COM MENOS DE 20: {f20}.')