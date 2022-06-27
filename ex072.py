tupla=0
b=' '
n=(0,1,2,3,4,5,6,7,8,9,10)
while b not in n:
    b= int(input('Digite um número entre 0 e 10:'))
tupla= ('zero','um','dois','três', 'quatro','cinco', 'seis','sete','oito', 'nove','dez')
print(f'Você digitou o número {tupla[b]}')
