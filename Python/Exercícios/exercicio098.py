import time

def contador():
    ini = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    while True:
        if passo == 0:
            "Digite um valor inteiro"
        else:
            break
    if ini > fim:
        passo = passo*-1
    if ini == fim:
        print ("Valores igual para início e fim")
    for c in range (ini,fim,passo):
        print (f'{c} ')
        time.sleep(0.05)
    print (f'{"-"*10}fim do programa{"-"*10}')

    #c = 1

contador()

