#Código do Guanabara

def leiaDinheiro(msg):
	válido = False
	while not válido:
		entrada = str(input(msg)),replace(',','.').strip()
		if entrada.isalpha() or entrada =='':
			print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
		else:
			válido = True
			return float(entrada)
'''
MINHA TENTATIVA
def leia_dinheiro():
    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric() == True:
            break
        elif valor.isnumeric() == False:
            if "," in valor:
                valor = valor.replace(",",".")
                valor = float(valor)
        else:
            print('ERRO! Por favor, digite um valor númerico')

    print (f'{valor} é número')
'''