import random

numeros = []

def sorteia():
    for c in range (0,5):
        num = random.randint(1,100)
        print (num)
        numeros.append(num)
def somaPar():
    par = 0
    for c in numeros:
        if c % 2 == 0:
            par += c
            print (c,end = ' ')
    print (f'A soma dos valores pares é {par}')

sorteia()
somaPar()
print (numeros)


