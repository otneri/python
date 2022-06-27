frase=str(input('Digite uma frase')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('Primeira ocorrencia na posição {}'.format(frase.find('A')+1))
print('A ultima ocorrencia na posição {}'.format(frase.rfind('A')+1))
