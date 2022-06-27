s=float(input('Digite seu salário:'))
if s > 1250:
    aumento= s+(s*0.1)
elif s<=1250:
    aumento= s+(s*0.15)
print(f'Seu novo salário é de R${aumento}')