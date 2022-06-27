alunos=list()
ficha=[]
while True:
    nome= str(input('Nome aluno:'))
    n1=float(input('Nota prova 1:'))
    n2=float(input('Nota prova 2:'))
    media=(n1+n2)/2
    ficha.append([nome,[n1,n2],media])
    resp=str(input('Quer continuar (S/N):')).upper()
    if resp == 'N':
        break
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for i, a in enumerate (ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}' )

while True:
    opc=int(input('Quer exibir notas de qual aluno (999 interrompe):'))
    if opc == 999:
        print('PROCESSO FINALIZADO')
        break
    elif opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha [opc][1]}')