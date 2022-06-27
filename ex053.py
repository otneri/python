#palindromo
frase=str(input('Digite uma frase:')).strip().upper()
palavras= frase.split()
junto= ''.join(palavras)
inverso= junto [::-1]
if junto == inverso:
    print('PALÍNDROMO!')
else:
    print('NAO È UM PALINDROMO')
print(junto, inverso)
