def fatorial(num, show=0):
    num = o valor que será multiplicado por fatorial
    show (opcional) = FALSE para não ver o processo
    show (opcional) = TRUE para ver o processo
    
    #soma = 0
    inicio = 1
    fim = num
    if show == True:
        print (f'{num}', end = ' ')
        for c in range(inicio, fim):
            print (f'x {fim - c}', end = ' ')
            multi = c * num
            num =  multi
        print ('=',end =' ')
        print (num)
    else:
        for c in range(inicio, fim):
            multi = c * num
            num =  multi        
        print (f'O fatorial de {fim} é {num}')
        
num = int(input('Qual valor será calculado o fatorial: '))
fatorial(num)


'''
O professor Guanabara fez o código para fatorial que eu ainda não tinha compreendido:

def fatorial(n, show=False):
	f = 1
	for c in range (n, 0, -1):
		f *= c
	return f
    
print(fatorial(5,show = True))
'''