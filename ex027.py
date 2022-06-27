nome = str(input('Digite seu nome completo')).strip()
s = nome.split()
print(f'Seu primeiro nome é:{s[0]}')
print(f'Seu ultimo nome é:{s[-1]}')