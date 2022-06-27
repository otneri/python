from random import randint
n= tuple(randint(0,10) for i in range (5))
print(sorted(n))
print(max(n))
print(min(n))