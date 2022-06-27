matriz= [[],[],[],
         [],[],[],
         [],[],[]]
somaterceira=[matriz[6],matriz[7],matriz[8]]
pares=0
terceiracol=0
for c in range (0,9):
    valor=int(input('Digite o valor:'))
    matriz[c].append(valor)
    if valor % 2 ==0:
        pares+=valor
#for l in range (0,3):
    #terceiracol += matriz[4], matriz[5], matriz [6]

print('#'*50)
print(matriz[0],matriz[1],matriz[2])
print(matriz[3],matriz[4],matriz[5])
print(matriz[6],matriz[7],matriz[8])
print('#'*50)
#soma dos pares
print(f'A soma dos pares é {pares}')
print(f'A soma da terceira coluna {somaterceira} ')

#o maior da 2 linha
maior= matriz[3]
if matriz[4] > matriz [3]:
    maior=matriz[4]
    if matriz [5] > matriz [4]:
        maior=matriz[5]
print(f'O maior valor da segunda linha é: {maior}')
