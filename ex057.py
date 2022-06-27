s = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
while s != 'M' and s != 'F':
    #if s != 'F':
    print('Favor digitar um sexo válido.')
    s = str(input('Digite seu sexo [M/F]:')).upper()

print(f'Sexo {s} registrado.')
