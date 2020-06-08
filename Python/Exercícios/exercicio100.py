from random import randint
from time import sleep

numeros = []

def sorteia():
    print ('Sorteando os números: ', end=' ')
    for c in range (0,5):
        num = randint(1,100)
        print (num, end = ' ')
        numeros.append(num)
        sleep(0.5)
    print('Pronto!')

def somaPar():
    par = 0
    for c in numeros:
        if c % 2 == 0:
            par += c
            #print (c,end = ' ')
    print (par)
    #print (f'A soma dos valores pares é {par}')


sorteia()
print (f'Somando os valores pares de {numeros}, temos: ', end = '')
somaPar()


