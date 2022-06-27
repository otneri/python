print('#*'*20)
print('VALIDADOR DE TRIÂNGULOS')
print('#*'*20)
a=float(input('Digite o tamanho da primeira reta (cm):'))
b=float(input('Digite o tamanho da segunda reta (cm):'))
c=float(input('Digite o tamanho da terceira reta (cm):'))
if b-c<a<b+c or a-c<b<a+c or b-a<c<b+a:
    print('Você pode formar um triângulo')
else:
    print('Você n pode formar triangulo')
