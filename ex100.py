from random import randint
n=()
def sorteia (lista):
    for c in range (0,5):
        n=randint(0,9)
        lista.append(n)

def somapar (lista):
    soma=0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Os valores sorteados foram {num} e a soma dos pares é {soma}')
num= list()
sorteia(num)
somapar(num)

