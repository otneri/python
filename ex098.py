from time import sleep
def contador (i,f,p):
    if p < 0:
        p*=-1
    if p==0:
        p=1

    if i < f:
        cont=i
        while cont <= f:
            print(cont, end=' ')
            cont+=p
            sleep(0.3)
    else:
        if i > f:
            cont=i
            while cont >=f:
                print(cont, end=' ')
                cont-=p
                sleep(0.3)

print(contador(i= int(input('Início:')),f= int(input('Fim:')),p= int(input('Passos:'))))