from datetime import date
while True:
    pessoa={'nome':str(input('NOME:'))}
    nascimento = int(input('ANO NASCIMENTO:'))
    pessoa['idade']= (date.today().year) - (nascimento)
    pessoa['ctps']= int(input('CARTEIRA TRABALHO:'))

    if pessoa['ctps'] == 0:
        break

    else:
        pessoa['emprego']= int(input('ANO CONTRATAÇÃO:'))
        pessoa['salario']= int(input('SALARIO R$:'))

        #idade primeiro emprego
        idadeprimeiro= pessoa['emprego'] - nascimento
        #idade para se aposentar
        idadeapos = idadeprimeiro+35
        print('#'*50)
        print(pessoa)
        for k, v in pessoa.items():
            print(f'PARA {k} TEMOS {v}.')
        print(f'VOCÊ VAI SE APOSENTAR COM {idadeapos} ANOS.')

        break