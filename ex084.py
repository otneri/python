pessoas=[]
pesados=[]
leves=[]
while True:
    nome=str(input('Cadastre uma pessoa:'))
    pessoas.append(nome)
    peso=float(input('Peso:'))
    if peso >= 70:
        pesados.append([nome,peso])
    else:
        leves.append([nome,peso])
    resp=str(input('Quer continuar S/N:')).upper()
    if resp == 'N':
        break
print('#'*40)
print(f'Você cadastrou {len(pessoas)} pessoas. Os mais leves foram {leves} e os mais pesados foram {pesados}.')

