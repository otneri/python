txt=''
def linhas(txt):
    tam= len (txt) + 4
    print('!'*tam)
    print(f'  {txt}  ')
    print('!' * tam)

linhas(txt=str(input('Digite uma mensagem:')))



print(txt)
