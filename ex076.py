#listagem de precos
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*50)
lista=('Arroz',12.50,
       'Feijão',18.00,
       'Pão',9.90,
       'Carne',35.50)
for pos in range (0,len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-'*50)
