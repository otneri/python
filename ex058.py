from random import randint
sorte= randint (0,10)
nn= sorte
n = int(input('Pensei em um número de 0 a 10 . Adivinhe qual é:'))
tentativas=0
while nn != n:
    print(f'NÃO. TENTE NOVAMENTE.')
    n = int(input('Digite outro número:'))
    tentativas += 1
if tentativas == 0:
    print('VC É O CARA! ACERTOU DE PRIMA.')
else:
    print(f'Acertou! Você precisou de {tentativas} tentativas.')
