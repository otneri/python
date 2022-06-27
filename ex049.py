#refazer tabuada usando laço for
n= int(input('Digite um número:'))
for c in range (0,11):
    print(f'{n} X {c:2} = {n*c}')