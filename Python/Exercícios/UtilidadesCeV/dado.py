#Código do Guanabara

def leiaDinheiro(msg):
	válido = False
	while not válido:
		entrada = str(input(msg)).replace(',','.').strip()
		if entrada.isalpha() or entrada =='':
			print (f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
		else:
			válido = True
			return float(entrada)

def leiaOpcao(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print (f'\033[0;31mERRO: \"{entrada}\" Por favor, digite um valor inteiro entre 1 e 3\033[m')
        elif int(entrada) <1 or int(entrada) > 3:
            print (f'\033[0;31mERRO: \"{entrada}\" Não é uma opção válida\033[m') 
        elif int(entrada) == 1:
            from UtilidadesCeV import cadastros
            #from cadastros import mostrar_cadastros
            cadastros.mostrar_cadastros()
            válido = True
        elif int(entrada) == 2:
            from UtilidadesCeV import cadastros
            #from cadastros import cadastrar
            cadastros.cadastrar()
        elif int(entrada) == 3:
            return ("FIM DO PROGRAMA. Até uma próxima!")
            break
        else:
            válido = True
            return (f'OPÇÃO {int(entrada)}')
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

#leiaOpcao("faça sua esolha: ")