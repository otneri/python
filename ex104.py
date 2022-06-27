def LeiaInt (num):
    while num not in int:
        num=int(input())

n = LeiaInt('Digite um número:')
print(f'O número digitado foi {n}')
