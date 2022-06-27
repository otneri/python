from random import choice
sorte= [0,1,2,3,4,5]
nn=choice(sorte)
n = int(input('Pensei em um número de 0 a 5 . Adivinhe qual é:'))
if nn == n:
    print(f'Você acertou! Parabéns')
else:
    print('Você errouuuuu!')
