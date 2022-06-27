print('@@@'*20)
print('BLITZ DO ÍNDICE DE MASSA CORPORAL!!!')
print('@@@'*20)
peso=float(input('Digite seu peso:'))
h=float(input("Digite sua altura:"))
imc= peso/(h**2)

print(f'Seu IMC é de: {imc:.2f}')
if imc <18.5:
    print('Seu IMC é baixo.')
elif 18.5<=imc<25.0:
    print('Seu peso é Ideal!')
elif 25<=imc<30:
    print('Você está em sobrepeso.')
elif 30<=imc<40:
    print('Você é OBESO!')
else:
    print("Você tem OBESIDADE MÓRBIDA!")