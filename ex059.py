n1= int (input('Digite o primeiro número:'))
n2= int (input('Digite o segundo número:'))
opcao=0
while opcao != 5:
    opcao= int (input(f'''Digite a opção que você quer fazer com {n1} e {n2}:
        [1] Somar 
        [2] Multiplicar 
        [3] Maior 
        [4] Digitar novos números 
        [5] Sair
        Digite:'''))

    if opcao == 1:
        print(f'A soma dos valores é: {n1+n2}')
    elif opcao == 2:
        print(f'A multiplicação dos valores é: {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é: {n1}')
        elif n1 == n2:
            print('Os dois são iguais.')
        else:
            print(f'O maior número é: {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))
    elif opcao != 5:
        print('OPÇÁO INVÁLIDA.')
print('FIM.')

