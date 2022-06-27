#Fibonatti => F5=F4+F3
print('-'*20)
print('GERADOR FIBONACCI')
print('-'*20)
t1=0
t2=1
cont=2
termos=int(input('Quantos termos Fibonacci quer ver:'))
print('~'*20)
print(f'{t1} => {t2} => ', end=' ')
while cont < termos:
    t3=t1+t2
    print(f'{t3} => ', end=' ')
    t1=t2
    t2=t3
    cont+=1
print('FIM.')