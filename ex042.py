print('#*'*20)
print('VALIDADOR DE TRIÂNGULOS')
print('#*'*20)
a=float(input('Digite o tamanho da primeira reta (cm):'))
b=float(input('Digite o tamanho da segunda reta (cm):'))
c=float(input('Digite o tamanho da terceira reta (cm):'))
if b<a+c and a<b+c and c<b+a:
    print('Você pode formar um triângulo',end='. ')
    if a == b and b == c:
        print('Seu triângulo é EQUILATERO!')
    elif a != b != c != a :
        print('Seu triângulo é ESCALENO.')
    else:
        print('Seu triângulo é ISOSCELES')
else:
    print('Você não pode formar triangulo')
