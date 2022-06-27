casa= float(input('Qual valor da casa que deseja comprar R$:'))
salario= float(input('Qual o seu salário mensal R$:'))
anos= int(input('Em quantos anos deseja pagar:'))
parcela = casa/(anos*12)

if parcela >= (salario*0.3):
    print('Infelizmente não podemos financiar esta casa para você. '
          'Aumente o prazo de pagamento ou escolha outra.')
else:
    print('Empréstimo liberado!')
print(f'O valor das parcelas mensais que você irá pagar é de R${parcela}.')
